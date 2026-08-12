#!/usr/bin/env python3
"""Exact arithmetic checks for experiments/banded-gram/candidate.json.

This checks the arithmetic consequences of the new banded-Gram lemma.  It does
not replace mathematical review of the lemma itself.
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

# The q-band graph is properly colored by index modulo q+1.  The analytic
# lemma therefore has the threshold (q+1)/q.
T = Fraction(q + 1, q)
assert T == rat(band["band_energy_threshold"])
assert A < T

# Exact verification that h_m(T) > A, without evaluating the square root.
# h_m(T) = T/m + 2*sqrt((m-1)T/m) - 1 in the nonlinear branch.
assert T > Fraction(m, m - 1)
inner = Fraction(m - 1, m) * T
rhs = (A + 1 - T / m) / 2
assert rhs > 0
square_gap = inner - rhs * rhs
witness = band["h_threshold_square_witness"]
assert inner == rat(witness["inner"])
assert rhs == rat(witness["comparison_rhs"])
assert square_gap == rat(witness["positive_square_gap"])
assert square_gap > 0

# With the banded-Gram lemma and h_m(T)>A, the block deduction uses R=A and
# eta=1 instead of the scalar relaxation R=h_m(A), eta=R/A.
assert projection["R_equals_A"] is True
assert rat(projection["eta"]) == 1
bound = (m * H - B * (m - q)) / (m - A)
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
print("h_threshold_square_gap=", square_gap)
print("exact_bound_fraction=", f"{bound.numerator}/{bound.denominator}")
print("bound=", value)
print("percent=", value * 100)
print("safe_decimal_floor=", Decimal(safe.numerator) / Decimal(safe.denominator))
