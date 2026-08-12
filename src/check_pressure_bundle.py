#!/usr/bin/env python3
"""Exact arithmetic for the pressure-supporting-line frontier bundle.

This file checks only rational consequences of the proposed continuous
banded-Gram profile.  Local numerical certification status is read from the
candidate files but the c=8/5 line and the c=6/5 bundle target remain separate
from the root record until their hardened interval runs close.
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
base = json.loads((ROOT / "candidate.json").read_text())
c12 = json.loads((ROOT / "experiments" / "multilag" / "candidate.json").read_text())
c16 = json.loads((ROOT / "experiments" / "pressure-frontier" / "c16.json").read_text())


def rat(node: dict) -> Fraction:
    return Fraction(int(node["numerator"]), int(node["denominator"]))


H = rat(base["window"]["projection_h_floor"])
B = rat(base["position_pressure"]["total"])
eps0 = rat(base["local_certificate"]["target"])
assert base["local_certificate"]["verified"] is True
assert H == Fraction(336094079, 500000000)
assert B == Fraction(93, 23000)
assert eps0 == Fraction(79107, 10000000)

assert c12["local_certificate"]["verified"] is True
assert rat(c12["local_certificate"]["target"]) == Fraction(9015, 1000000)
eps12_bundle = rat(c12["local_search"]["next_bundle_target"])
assert eps12_bundle == Fraction(9017, 1000000)

c12_scale = rat(c12["local_search"]["pressure_total_scale"])
c16_scale = rat(c16["local_search"]["pressure_total_scale"])
eps16 = rat(c16["local_search"]["candidate_target_for_certification"])
assert c12_scale == Fraction(6, 5)
assert c16_scale == Fraction(8, 5)
assert eps16 == Fraction(11129, 1000000)

T = Fraction(7, 6)

# ---------------------------------------------------------------------------
# Single auxiliary line c=8/5: full no-Gram-loss block through m=464.
# ---------------------------------------------------------------------------
m_single = 464
n = m_single - 6
A0 = eps0 * n
A2 = eps16 * n
S02 = (c16_scale * A0 - A2) / (c16_scale - 1)
assert A0 == Fraction(18115503, 5000000)
assert A2 == Fraction(2548541, 500000)
assert S02 == Fraction(8748487, 7500000)
assert T - S02 == Fraction(1513, 7500000) > 0

# On the auxiliary-line region, concavity reduces the check to the endpoint
# g_6(A2) >= A0.  Squaring is legitimate because all quantities are positive.
single_square_gap = T * A2 - ((A0 + T) / 2) ** 2
assert single_square_gap == Fraction(190015244512919, 900000000000000)
assert single_square_gap > 0

single_bound = (m_single * H - B * n) / (m_single - A0)
assert single_bound == Fraction(891374752772, 1323583585775)
single_safe = Fraction(6734555810, 10**10)
assert single_safe < single_bound < single_safe + Fraction(1, 10**10)

# m=465 already loses the linear-band intersection condition for the same
# exact target, so 464 is the last full no-loss block for this single line.
n_next = 465 - 6
A0_next = eps0 * n_next
A2_next = eps16 * n_next
S02_next = (c16_scale * A0_next - A2_next) / (c16_scale - 1)
assert S02_next - T == Fraction(35177, 15000000) > 0

# ---------------------------------------------------------------------------
# Three-line bundle c=1, 6/5, 8/5 at m=496.
# ---------------------------------------------------------------------------
m_bundle = 496
n = m_bundle - 6
A0 = eps0 * n
A1 = eps12_bundle * n
A2 = eps16 * n
assert A0 == Fraction(3876243, 1000000)
assert A1 == Fraction(441833, 100000)
assert A2 == Fraction(545321, 100000)

# Pairwise intersections of P >= (Ai-S)/ci.  Since slopes are ordered
# -1 < -5/6 < -5/8, the ordered intersections certify the active envelope:
# base line, then c=6/5, then c=8/5.
S01 = (c12_scale * A0 - A1) / (c12_scale - 1)
S02 = (c16_scale * A0 - A2) / (c16_scale - 1)
S12 = (c12_scale * A2 - c16_scale * A1) / (c12_scale - c16_scale)
assert S01 == Fraction(72863, 62500)
assert S12 == Fraction(131369, 100000)
assert S01 < S02 < S12
assert S01 < T < S12

# On [S01,T], g(S)=S and the c=6/5 branch is increasing; its value at T
# remains strictly above A0.
f1_T = T + (A1 - T) / c12_scale
assert f1_T - A0 == Fraction(161, 1125000) > 0

# On [T,S12], g(S)+(A1-S)/(6/5) is concave.  At S12, prove its value
# exceeds A0 via an exact square witness for g(S12).
p12 = (A1 - S12) / c12_scale
R12 = A0 - p12
assert p12 == Fraction(1617, 625)
assert R12 == Fraction(1289043, 1000000)
switch_square_gap = T * S12 - ((R12 + T) / 2) ** 2
assert switch_square_gap == Fraction(900390297359, 36000000000000)
assert switch_square_gap > 0

# On [S12,A2], the c=8/5 branch is concave.  The switch endpoint was just
# checked, and the far endpoint reduces to g(A2) >= A0.
end_square_gap = T * A2 - ((A0 + T) / 2) ** 2
assert end_square_gap == Fraction(156378844559, 36000000000000)
assert end_square_gap > 0

bundle_bound = (m_bundle * H - B * n) / (m_bundle - A0)
assert bundle_bound == Fraction(952844063308, 1414855801375)
bundle_safe = Fraction(6734566606, 10**10)
assert bundle_safe < bundle_bound < bundle_safe + Fraction(1, 10**10)

# m=497 is beyond this full no-loss bundle plateau: both the first switch and
# the c=8/5 far-end square check have crossed their exact boundaries.
n_next = 497 - 6
A0_next = eps0 * n_next
A1_next = eps12_bundle * n_next
A2_next = eps16 * n_next
S01_next = (c12_scale * A0_next - A1_next) / (c12_scale - 1)
end_square_gap_next = T * A2_next - ((A0_next + T) / 2) ** 2
assert S01_next - T == Fraction(2851, 1875000) > 0
assert end_square_gap_next == Fraction(-9483938701321, 3600000000000000) < 0

print("pressure_bundle_exact_arithmetic_verified=True")
print("single_c16_m=", m_single)
print("single_c16_bound=", float(single_bound))
print("single_c16_percent=", float(single_bound * 100))
print("single_c16_safe_floor=", float(single_safe))
print("bundle_m=", m_bundle)
print("bundle_switch_01=", S01)
print("bundle_switch_12=", S12)
print("bundle_switch_square_gap=", switch_square_gap)
print("bundle_end_square_gap=", end_square_gap)
print("bundle_bound=", float(bundle_bound))
print("bundle_percent=", float(bundle_bound * 100))
print("bundle_safe_floor=", float(bundle_safe))
