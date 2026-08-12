#!/usr/bin/env python3
"""Structural and interval checks for discovery_candidate.json.

This script verifies exact combinatorial constraints, the analytic window floor
and positivity, and the conservative exact-pressure projection. It deliberately
does NOT claim to prove the local six-gap inequality; that requires the full
outward-rounded branch-and-bound verifier.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
from mpmath import iv

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = json.loads((ROOT / "discovery_candidate.json").read_text(encoding="utf-8"))

mp.mp.dps = 80
iv.dps = 70


def sinc(z):
    return mp.sin(z) / z if z else mp.mpf(1)


def sinc_interval(z):
    radius = max(abs(float(z.a)), abs(float(z.b)))
    if radius < 0.5:
        value = iv.mpf(1)
        for n in range(1, 32):
            value += (-1 if n & 1 else 1) * z ** (2 * n) / math.factorial(2 * n + 1)
        return value + iv.mpf([-1e-70, 1e-70])
    return iv.sin(z) / z


def C(a, b):
    return (sinc((a - b) / 2) + sinc((a + b) / 2)) / 2


def C_interval(a, b):
    return (sinc_interval((a - b) / 2) + sinc_interval((a + b) / 2)) / 2


def A(a, b):
    return (
        (mp.sin(a / 2) / a + 2 * mp.cos(a / 2) / a**2) * sinc(b / 2)
        - 2 * C(a, b) / a**2
    )


def A_interval(a, b):
    return (
        (iv.sin(a / 2) / a + 2 * iv.cos(a / 2) / a**2) * sinc_interval(b / 2)
        - 2 * C_interval(a, b) / a**2
    )


def frequency(text, interval=False):
    lib = iv if interval else mp
    if text == "sqrt(2)":
        return lib.sqrt(2)
    if text.endswith("*pi"):
        return int(text[:-3]) * lib.pi
    raise ValueError(text)


window = CANDIDATE["window"]
den = int(window["denominator"])
nums = [int(x) for x in window["numerators"]]
freq_text = window["frequencies"]

# Exact pair span capacities.
pair = CANDIDATE["pair_weights"]
pair_den = int(pair["denominator"])
expected = int(pair["span_capacity_numerator"])
q = int(CANDIDATE["gaps_per_local_window"])
for span in range(1, q + 1):
    total = sum(int(n) for i, j, n in pair["entries"] if int(j) - int(i) == span)
    assert total == expected, (span, total, expected)
print("pair_span_capacities_exact=True")

# Exact pressure total.
pressure = CANDIDATE["position_pressure"]
pden = int(pressure["denominator"])
ptotal = sum(int(x) for x in pressure["numerators"])
declared = Fraction(
    int(pressure["total"]["numerator"]),
    int(pressure["total"]["denominator"]),
)
assert Fraction(ptotal, pden) == declared
print("pressure_total_exact=True", declared)

# Point H.
c = [mp.mpf(n) / den for n in nums]
omega = [frequency(x) for x in freq_text]
i1 = sum(ci * sinc(w / 2) for ci, w in zip(c, omega))
i2 = sum(c[i] * c[j] * C(omega[i], omega[j]) for i in range(len(c)) for j in range(len(c)))
J = sum(c[i] * c[j] * A(omega[i], omega[j]) for i in range(len(c)) for j in range(len(c)))
c1 = i1 * i1 / (i2 + J)
H = 2 - 1 / c1
print("H =", mp.nstr(H, 70))

# Interval H.
ci = [iv.mpf(n) / den for n in nums]
oi = [frequency(x, interval=True) for x in freq_text]
i1_iv = iv.mpf(0)
i2_iv = iv.mpf(0)
J_iv = iv.mpf(0)
for a, w in zip(ci, oi):
    i1_iv += a * sinc_interval(w / 2)
for i in range(len(ci)):
    for j in range(len(ci)):
        i2_iv += ci[i] * ci[j] * C_interval(oi[i], oi[j])
        J_iv += ci[i] * ci[j] * A_interval(oi[i], oi[j])
H_iv = 2 - 1 / (i1_iv * i1_iv / (i2_iv + J_iv))
floor = window["projection_h_floor"]
H_floor = iv.mpf(int(floor["numerator"])) / int(floor["denominator"])
print("H_interval =", H_iv)
assert H_iv > H_floor
print("H_floor_interval_verified=True")

# Window positivity.
N = int(window.get("positivity_subdivision_cells", 4096))
global_lo = float("inf")
for k in range(N):
    s = iv.mpf([k / (2 * N), (k + 1) / (2 * N)])
    v = iv.mpf(0)
    for a, w in zip(ci, oi):
        v += a * iv.cos(w * s)
    global_lo = min(global_lo, float(v.a))
print("interval_window_lower_bound =", global_lo)
assert global_lo > 0

# Conservative final projection.
eps_node = CANDIDATE["local_search"]["candidate_target_for_certification"]
eps = mp.mpf(int(eps_node["numerator"])) / int(eps_node["denominator"])
B = mp.mpf(declared.numerator) / declared.denominator
Hsafe = mp.mpf(int(floor["numerator"])) / int(floor["denominator"])


def h_m(E, m):
    threshold = mp.mpf(m) / (m - 1)
    if E <= threshold:
        return E
    return E / m + 2 * mp.sqrt((m - 1) * E / m) - 1


best = None
for m in range(q + 2, 1000):
    Avalue = eps * (m - q)
    R = h_m(Avalue, m)
    eta = R / Avalue
    bound = (m * Hsafe - eta * B * (m - q)) / (m - R)
    if best is None or bound > best[0]:
        best = (bound, m)

assert best is not None
print("best_m =", best[1])
print("conservative_discovery_bound =", mp.nstr(best[0], 70))
assert best[1] == int(CANDIDATE["final_projection"]["block_length"])
print("local_interval_certificate_verified=False")
