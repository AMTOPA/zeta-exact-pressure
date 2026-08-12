#!/usr/bin/env python3
"""Exact arithmetic for the pressure-supporting-line banded-Gram experiment.

The arithmetic is conditional on interval certification of the auxiliary local
certificate in experiments/multilag/candidate.json and on acceptance of the
continuous banded-Gram analytic profile. No floating-point value is used below.
"""
from fractions import Fraction

q = 6
m = 259
n = m - q

H = Fraction(336094079, 500000000)
B = Fraction(93, 23000)
eps0 = Fraction(79107, 10000000)
eps1 = Fraction(17997, 2000000)  # auxiliary target 0.0089985
c = Fraction(6, 5)               # auxiliary pressure multiplier
T = Fraction(7, 6)

A0 = eps0 * n
A1 = eps1 * n
assert A0 == Fraction(20014071, 10000000)
assert A1 == Fraction(4553241, 2000000)

# Base: S + P >= A0.
# Auxiliary: S + c P >= A1.
# Their active pressure lines intersect at Sx.
Sx = (c * A0 - A1) / (c - 1)
assert Sx == Fraction(6253401, 10000000)
assert 0 < Sx < T < A0 < A1

# For 0<=S<=Sx the base line is active and g_6(S)=S, hence
# g_6(S)+P >= S+(A0-S)=A0 exactly.
# For Sx<=S<=A1 the auxiliary line is active. The function
# g_6(S)+(A1-S)/c is concave, so its minimum occurs at Sx or A1.
# At Sx its value is A0. At A1 it is g_6(A1), which exceeds A0
# by the exact square witness below.
square_gap = T * A1 - ((A0 + T) / 2) ** 2
assert square_gap == Fraction(528783848062631, 3600000000000000)
assert square_gap > 0

# Thus the two local supporting lines plus the banded profile prove
# Delta + P >= A0: the scalar Gram discount disappears entirely.
R = A0
eta = Fraction(1)

bound = (m * H - B * n) / (m - R)
assert bound == Fraction(86536866461, 128499296450)

safe = Fraction(6734423366, 10000000000)
assert safe < bound < safe + Fraction(1, 10000000000)

print("multilag_exact_arithmetic_verified=True")
print("m=", m)
print("A0=", A0)
print("A1=", A1)
print("supporting_line_intersection=", Sx)
print("g_A1_over_A0_square_gap=", square_gap)
print("R_equals_A0=True")
print("eta=1")
print("bound_fraction=", f"{bound.numerator}/{bound.denominator}")
print("bound=", float(bound))
print("percent=", float(bound * 100))
print("safe_decimal_floor=", float(safe))
