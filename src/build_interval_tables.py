#!/usr/bin/env python3
"""Build outward-rounded kernel tables for the current discovery candidate.

This is a repository-native implementation driven entirely by candidate.json.
It supports any window term count with frequencies sqrt(2), 2*pi, 4*pi, ...
and writes the binary table interface consumed by the positioned-pressure
branch-and-bound verifier.

The table builder is rigorous at the mpmath.iv level; generation of tables is
not by itself a proof of the six-gap inequality. A separate verifier must close
all boxes at the requested target.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
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


def sinc_triplet(z):
    """Return interval enclosures for sinc(z), sinc'(z), sinc''(z)."""
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
    value = s / z
    first = (z * c - s) / z2
    second = ((2 - z2) * s - 2 * z * c) / (z2 * z)
    return value, first, second


def make_kernel(candidate: dict):
    window = candidate["window"]
    den = int(window["denominator"])
    coeff = [iv.mpf(int(n)) / den for n in window["numerators"]]
    omega = [parse_frequency(x) for x in window["frequencies"]]

    def kernel_triplet(x):
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

    return kernel_triplet


def outward_lower(x: float) -> float:
    return math.nextafter(x, -math.inf)


def outward_upper(x: float) -> float:
    return math.nextafter(x, math.inf)


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
    parser.add_argument(
        "--smoke-cells",
        type=int,
        default=0,
        help="override the full required range and generate only this many cells",
    )
    args = parser.parse_args()

    iv.dps = args.precision
    candidate = load_candidate()
    target = rational(candidate["local_search"]["candidate_target_for_certification"])
    pressure = candidate["position_pressure"]
    pressure_den = int(pressure["denominator"])
    min_pressure = min(Fraction(int(x), pressure_den) for x in pressure["numerators"])

    required = (target * args.grid / min_pressure)
    cell_count = (required.numerator + required.denominator - 1) // required.denominator + 33
    if args.smoke_cells:
        cell_count = args.smoke_cells
    midpoint_count = 2 * cell_count + 1

    kernel = make_kernel(candidate)
    k0 = kernel(iv.mpf(0))[0]
    k0sq = k0 * k0

    w_lower: list[float] = []
    w_second_lower: list[float] = []
    for i in range(cell_count):
        x = iv.mpf([i / args.grid, (i + 1) / args.grid])
        k, kd, kdd = kernel(x)
        w = k * k / k0sq
        wdd = 2 * (kd * kd + k * kdd) / k0sq
        lo = max(0.0, float(w.a))
        w_lower.append(0.0 if lo == 0.0 else outward_lower(lo))
        w_second_lower.append(outward_lower(float(wdd.a)))

    w_mid_lower: list[float] = []
    w_mid_upper: list[float] = []
    w_prime_mid_lower: list[float] = []
    w_prime_mid_upper: list[float] = []
    for i in range(midpoint_count):
        x = iv.mpf(i) / (2 * args.grid)
        k, kd, _ = kernel(x)
        w = k * k / k0sq
        wd = 2 * k * kd / k0sq
        w_mid_lower.append(outward_lower(float(w.a)))
        w_mid_upper.append(outward_upper(float(w.b)))
        w_prime_mid_lower.append(outward_lower(float(wd.a)))
        w_prime_mid_upper.append(outward_upper(float(wd.b)))

    args.output.mkdir(parents=True, exist_ok=True)
    tables = {
        "w_lower.bin": w_lower,
        "w_second_lower.bin": w_second_lower,
        "w_mid_lower.bin": w_mid_lower,
        "w_mid_upper.bin": w_mid_upper,
        "w_prime_mid_lower.bin": w_prime_mid_lower,
        "w_prime_mid_upper.bin": w_prime_mid_upper,
    }
    manifest = {
        "term_count": int(candidate["window"]["term_count"]),
        "grid": args.grid,
        "precision_decimal_digits": args.precision,
        "target": f"{target.numerator}/{target.denominator}",
        "coarse_cells": cell_count,
        "midpoint_values": midpoint_count,
        "smoke_only": bool(args.smoke_cells),
        "files": {},
    }
    for name, values in tables.items():
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
