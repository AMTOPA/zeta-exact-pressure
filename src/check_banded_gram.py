#!/usr/bin/env python3
"""Exact arithmetic checks for experiments/banded-gram/candidate.json.

This checks the arithmetic consequences of the continuous banded-Gram profile.
It does not replace mathematical review of the analytic profile itself.
"""
from __future__ import annotations

import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = json.loads(
    (ROOT / "experiments" / "banded-gram" / "candidate.json").read_text(encoding="utf-8")
)


def rat(node: dict) -> Fraction:
    return Fraction(int(node["numerator"]), int(node["denominator"]))


local = CANDIDATE["local_input"]
band = CANDIDATE["banded_gram"]
projection = CANDIDATE["projection"]

assert local["verified"] is True
q = int(local["gaps"])
m = int(band["block_length"])
assert q == int(band["bandwidth"])
assert int(band["color_count"]) == q + 1

H = rat(local["h_floor"])
epsilon = rat(local["epsilon"])
B = rat(local["pressure_total"])
A = epsilon * (m - q)
assert A == rat(band["A"])

# Proper coloring of the q-band graph by residues modulo q+1 gives the
# operator-norm constant q/(q+1), hence T=(q+1)/q in the analytic profile.
T = Fraction(q + 1, q)
assert T == rat(band["band_energy_threshold"])
assert A > T  # the selected optimum is in the square-root branch

# The continuous profile is
#   g_q(A) = 2*sqrt(T*A) - T   for A >= T.
# We use a rational R_floor below g_q(A).  Verify this without floating point:
# T*A > ((R_floor + T)/2)^2.
R = rat(band["R_floor"])
rhs = (R + T) / 2
square_gap = T * A - rhs * rhs
witness = band["R_floor_square_witness"]
assert rhs == rat(witness["comparison_rhs"])
assert square_gap == rat(witness["positive_square_gap"])
assert square_gap > 0

eta = R / A
assert eta == rat(projection["eta"])

# Shifted-block arithmetic with the strengthened banded profile.
bound = (m * H - eta * B * (m - q)) / (m - R)
assert bound == rat(projection["exact_bound"])

safe = rat(projection["safe_decimal_floor"])
assert safe < bound
assert bound - safe < Fraction(1, 10**10)

getcontext().prec = 80
value = Decimal(bound.numerator) / Decimal(bound.denominator)
print("banded_gram_arithmetic_verified=True")
print("q=", q)
print("m=", m)
print("A=", A)
print("band_threshold=", T)
print("R_floor=", R)
print("R_floor_square_gap=", square_gap)
print("eta=", eta)
print("exact_bound_fraction=", f"{bound.numerator}/{bound.denominator}")
print("bound=", value)
print("percent=", value * 100)
print("safe_decimal_floor=", Decimal(safe.numerator) / Decimal(safe.denominator))
