#!/usr/bin/env python3
"""Exact arithmetic for the four-supporting-line pressure-frontier candidate.

The c=6/5 target 0.009021 and c=2 local target 0.01118 are kept separate from
the root record until their hardened interval runs close.  This script checks
only the exact global consequences if those two local inequalities hold and if
the continuous banded-Gram profile is accepted.
"""
from fractions import Fraction

q = 6
m = 500
n = m - q

H = Fraction(336094079, 500000000)
B = Fraction(93, 23000)
T = Fraction(7, 6)

eps0 = Fraction(79107, 10000000)
eps12 = Fraction(9021, 1000000)
eps16 = Fraction(11129, 1000000)
eps20 = Fraction(559, 50000)

c0 = Fraction(1)
c12 = Fraction(6, 5)
c16 = Fraction(8, 5)
c20 = Fraction(2)

A0 = eps0 * n
A1 = eps12 * n
A2 = eps16 * n
A3 = eps20 * n
assert A0 == Fraction(19539429, 5000000)
assert A1 == Fraction(2228187, 500000)
assert A2 == Fraction(2748863, 500000)
assert A3 == Fraction(138073, 25000)

# The active pressure envelope is base -> c=6/5 -> c=8/5 -> c=2.
S01 = (c12 * A0 - A1) / (c12 - c0)
S12 = (c12 * A2 - c16 * A1) / (c12 - c16)
S23 = (c16 * A3 - c20 * A2) / (c16 - c20)
assert S01 == Fraction(728403, 625000)
assert S12 == Fraction(666159, 500000)
assert S23 == Fraction(107939, 20000)
assert S01 < T < S12 < S23

# The direct nonadjacent intersections lie between the adjacent switches, so
# no supporting line is skipped by the stated active-envelope order.
S02 = (c16 * A0 - A2) / (c16 - c0)
S03 = (c20 * A0 - A3) / (c20 - c0)
S13 = (c20 * A1 - c12 * A3) / (c20 - c12)
assert S01 < S02 < S12
assert S12 < S03 < S23
assert S12 < S13 < S23

# On [S01,T], g(S)=S and the c=6/5 branch increases away from the base-line
# equality point.  This exact gap is the small low-energy margin that requires
# epsilon_1.2=0.009021 rather than 0.009017 at m=500.
f_T = T + (A1 - T) / c12
assert f_T - A0 == Fraction(2291, 11250000) > 0

# On each nonlinear segment, g plus an affine pressure branch is concave, so
# only its endpoints need checking.  At S12, S23 and A3 convert g >= R into
# exact positive square witnesses.
p12 = (A1 - S12) / c12
R12 = A0 - p12
sq12 = T * S12 - ((R12 + T) / 2) ** 2
assert p12 == Fraction(130169, 50000)
assert R12 == Fraction(6522529, 5000000)
assert sq12 == Fraction(24927893997431, 900000000000000) > 0

p23 = (A2 - S23) / c16
R23 = A0 - p23
sq23 = T * S23 - ((R23 + T) / 2) ** 2
assert p23 == Fraction(12597, 200000)
assert R23 == Fraction(2403063, 625000)
assert sq23 == Fraction(245946774779, 14062500000000) > 0

sq_end = T * A3 - ((A0 + T) / 2) ** 2
assert sq_end == Fraction(5072384185631, 900000000000000) > 0

# Therefore Delta + P >= A0 throughout, i.e. R=A0 and eta=1.
bound = (m * H - B * n) / (m - A0)
assert bound == Fraction(38421109085, 57050593133)
safe = Fraction(3367283929, 5000000000)  # 0.6734567858
assert safe < bound < safe + Fraction(1, 10**10)

# m=501 is already beyond the first-switch linear-band condition for the same
# targets, so m=500 is a genuine full-no-loss plateau edge.
n_next = 501 - q
A0n = eps0 * n_next
A1n = eps12 * n_next
S01n = (c12 * A0n - A1n) / (c12 - c0)
assert S01n - T == Fraction(853, 750000) > 0

print("pressure_bundle4_exact_arithmetic_verified=True")
print("m=", m)
print("S01=", S01)
print("S12=", S12)
print("S23=", S23)
print("low_energy_margin=", f_T - A0)
print("switch12_square_gap=", sq12)
print("switch23_square_gap=", sq23)
print("end_square_gap=", sq_end)
print("bound_fraction=", f"{bound.numerator}/{bound.denominator}")
print("bound=", float(bound))
print("percent=", float(bound * 100))
print("safe_decimal_floor=", float(safe))
