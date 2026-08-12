#!/usr/bin/env python3
"""Build outward-rounded kernel tables for the current discovery candidate.

The implementation is driven entirely by candidate.json, supports a variable
window term count, and writes the table interface used by the local verifier.
Table generation is rigorous at the mpmath.iv level; a successful table build
is not itself a proof of the six-gap inequality.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import multiprocessing as mp
import os
import struct
from fractions import Fraction
from pathlib import Path

from mpmath import iv

from candidate_data import load_candidate, rational

SERIES_RADIUS = 0.70
SERIES_TERMS = 28
SERIES_TAIL = 1e-55


def parse_frequency(text: str):
    if text == "sqrt(2)":
        return iv.sqrt(2)
    if text == "2*pi":
        return 2 * iv.pi
    if text.endswith("*pi"):
        return int(text[:-3]) * iv.pi
    raise ValueError(f"unsupported frequency: {text}")


def sinc_value(z):
    radius = max(abs(float(z.a)), abs(float(z.b)))
    if radius < SERIES_RADIUS:
        value = iv.mpf(1)
        for n in range(1, SERIES_TERMS):
            sign = -1 if n & 1 else 1
            value += sign * z ** (2 * n) / math.factorial(2 * n + 1)
        return value + iv.mpf([-SERIES_TAIL, SERIES_TAIL])
    return iv.sin(z) / z


def sinc_triplet(z):
    radius = max(abs(float(z.a)), abs(float(z.b)))
    if radius < SERIES_RADIUS:
        value = iv.mpf(1)
        first = iv.mpf(0)
        second = iv.mpf(0)
        for n in range(1, SERIES_TERMS):
            sign = -1 if n & 1 else 1
            denom = math.factorial(2 * n + 1)
            value += sign * z ** (2 * n) / denom
            first += sign * (2 * n) * z ** (2 * n - 1) / denom
            second += sign * (2 * n) * (2 * n - 1) * z ** (2 * n - 2) / denom
        tail = iv.mpf([-SERIES_TAIL, SERIES_TAIL])
        return value + tail, first + tail, second + tail

    s = iv.sin(z)
    c = iv.cos(z)
    z2 = z * z
    return (
        s / z,
        (z * c - s) / z2,
        ((2 - z2) * s - 2 * z * c) / (z2 * z),
    )


def window_constants(candidate: dict):
    window = candidate["window"]
    den = int(window["denominator"])
    coeff = [iv.mpf(int(n)) / den for n in window["numerators"]]
    omega = [parse_frequency(x) for x in window["frequencies"]]
    return coeff, omega


def kernel_value(x, coeff, omega):
    value = iv.mpf(0)
    for c, w in zip(coeff, omega):
        value += c * (sinc_value(w / 2 - iv.pi * x) + sinc_value(w / 2 + iv.pi * x)) / 2
    return value


def kernel_triplet(x, coeff, omega):
    value = iv.mpf(0)
    first = iv.mpf(0)
    second = iv.mpf(0)
    for c, w in zip(coeff, omega):
        left = w / 2 - iv.pi * x
        right = w / 2 + iv.pi * x
        lv, ld, ldd = sinc_triplet(left)
        rv, rd, rdd = sinc_triplet(right)
        value += c * (lv + rv) / 2
        first += c * iv.pi * (rd - ld) / 2
        second += c * iv.pi**2 * (ldd + rdd) / 2
    return value, first, second


def outward_lower(x: float) -> float:
    return math.nextafter(x, -math.inf)


def outward_upper(x: float) -> float:
    return math.nextafter(x, math.inf)


def coarse_chunk(task):
    start, stop, grid, precision, candidate, lower_only = task
    iv.dps = precision
    coeff, omega = window_constants(candidate)
    if lower_only:
        k0 = kernel_value(iv.mpf(0), coeff, omega)
        k0sq = k0 * k0
        lower: list[float] = []
        for i in range(start, stop):
            x = iv.mpf([i / grid, (i + 1) / grid])
            k = kernel_value(x, coeff, omega)
            w = k * k / k0sq
            lo = max(0.0, float(w.a))
            lower.append(0.0 if lo == 0.0 else outward_lower(lo))
        return start, lower, None

    k0 = kernel_triplet(iv.mpf(0), coeff, omega)[0]
    k0sq = k0 * k0
    lower: list[float] = []
    second_lower: list[float] = []
    for i in range(start, stop):
        x = iv.mpf([i / grid, (i + 1) / grid])
        k, kd, kdd = kernel_triplet(x, coeff, omega)
        w = k * k / k0sq
        wdd = 2 * (kd * kd + k * kdd) / k0sq
        lo = max(0.0, float(w.a))
        lower.append(0.0 if lo == 0.0 else outward_lower(lo))
        second_lower.append(outward_lower(float(wdd.a)))
    return start, lower, second_lower


def midpoint_chunk(task):
    start, stop, grid, precision, candidate = task
    iv.dps = precision
    coeff, omega = window_constants(candidate)
    k0 = kernel_triplet(iv.mpf(0), coeff, omega)[0]
    k0sq = k0 * k0
    wlo: list[float] = []
    whi: list[float] = []
    dlo: list[float] = []
    dhi: list[float] = []
    for i in range(start, stop):
        x = iv.mpf(i) / (2 * grid)
        k, kd, _ = kernel_triplet(x, coeff, omega)
        w = k * k / k0sq
        wd = 2 * k * kd / k0sq
        wlo.append(outward_lower(float(w.a)))
        whi.append(outward_upper(float(w.b)))
        dlo.append(outward_lower(float(wd.a)))
        dhi.append(outward_upper(float(wd.b)))
    return start, wlo, whi, dlo, dhi


def coarse_tasks(length: int, workers: int, grid: int, precision: int, candidate: dict, lower_only: bool):
    chunk = max(1, math.ceil(length / workers))
    return [
        (start, min(length, start + chunk), grid, precision, candidate, lower_only)
        for start in range(0, length, chunk)
    ]


def midpoint_tasks(length: int, workers: int, grid: int, precision: int, candidate: dict):
    chunk = max(1, math.ceil(length / workers))
    return [
        (start, min(length, start + chunk), grid, precision, candidate)
        for start in range(0, length, chunk)
    ]


def write_f64(path: Path, values: list[float]) -> None:
    with path.open("wb") as handle:
        for x in values:
            handle.write(struct.pack("<d", x))


def stream_sha256(values: list[float]) -> str:
    digest = hashlib.sha256()
    for x in values:
        digest.update(struct.pack(">d", x))
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("tables"))
    parser.add_argument("--grid", type=int, default=4000)
    parser.add_argument("--precision", type=int, default=50)
    parser.add_argument("--workers", type=int, default=max(1, os.cpu_count() or 1))
    parser.add_argument("--lower-only", action="store_true", help="generate only w_lower.bin")
    parser.add_argument(
        "--smoke-cells",
        type=int,
        default=0,
        help="override the full required range and generate only this many cells",
    )
    args = parser.parse_args()

    candidate = load_candidate()
    target = rational(candidate["local_search"]["candidate_target_for_certification"])
    pressure = candidate["position_pressure"]
    pressure_den = int(pressure["denominator"])
    min_pressure = min(Fraction(int(x), pressure_den) for x in pressure["numerators"])

    required = target * args.grid / min_pressure
    cell_count = (required.numerator + required.denominator - 1) // required.denominator + 33
    if args.smoke_cells:
        cell_count = args.smoke_cells
    midpoint_count = 2 * cell_count + 1
    workers = max(1, min(args.workers, cell_count))

    context = mp.get_context("spawn")
    with context.Pool(workers) as pool:
        coarse_parts = pool.map(
            coarse_chunk,
            coarse_tasks(cell_count, workers, args.grid, args.precision, candidate, args.lower_only),
        )
    w_lower = [0.0] * cell_count
    w_second_lower = None if args.lower_only else [0.0] * cell_count
    for start, lo, second in coarse_parts:
        w_lower[start : start + len(lo)] = lo
        if w_second_lower is not None and second is not None:
            w_second_lower[start : start + len(second)] = second

    tables: dict[str, list[float]] = {"w_lower.bin": w_lower}
    if not args.lower_only:
        midpoint_workers = max(1, min(args.workers, midpoint_count))
        with context.Pool(midpoint_workers) as pool:
            mid_parts = pool.map(
                midpoint_chunk,
                midpoint_tasks(midpoint_count, midpoint_workers, args.grid, args.precision, candidate),
            )
        w_mid_lower = [0.0] * midpoint_count
        w_mid_upper = [0.0] * midpoint_count
        w_prime_mid_lower = [0.0] * midpoint_count
        w_prime_mid_upper = [0.0] * midpoint_count
        for start, lo, hi, dlo, dhi in mid_parts:
            stop = start + len(lo)
            w_mid_lower[start:stop] = lo
            w_mid_upper[start:stop] = hi
            w_prime_mid_lower[start:stop] = dlo
            w_prime_mid_upper[start:stop] = dhi
        tables.update({
            "w_second_lower.bin": w_second_lower,
            "w_mid_lower.bin": w_mid_lower,
            "w_mid_upper.bin": w_mid_upper,
            "w_prime_mid_lower.bin": w_prime_mid_lower,
            "w_prime_mid_upper.bin": w_prime_mid_upper,
        })

    args.output.mkdir(parents=True, exist_ok=True)
    manifest = {
        "term_count": int(candidate["window"]["term_count"]),
        "grid": args.grid,
        "precision_decimal_digits": args.precision,
        "workers": workers,
        "target": f"{target.numerator}/{target.denominator}",
        "coarse_cells": cell_count,
        "midpoint_values": 0 if args.lower_only else midpoint_count,
        "lower_only": args.lower_only,
        "smoke_only": bool(args.smoke_cells),
        "files": {},
    }
    for name, values in tables.items():
        assert values is not None
        write_f64(args.output / name, values)
        manifest["files"][name] = {
            "length": len(values),
            "sha256_big_endian_float_stream": stream_sha256(values),
        }

    (args.output / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
