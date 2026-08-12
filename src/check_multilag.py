#!/usr/bin/env python3
"""Exact arithmetic for the optimized pressure-supporting-line experiment.

The arithmetic is conditional on interval certification of the auxiliary local
certificate in experiments/multilag/candidate.json and on acceptance of the
continuous banded-Gram analytic profile. No floating-point value is used in the
proof checks below.
"""
from fractions import Fraction

q = 6
m = 312
n = m - q

H = Fraction(336094079, 500000000)
B = Fraction(93, 23000)
eps0 = Fraction(79107, 10000000)
eps1 = Fraction(9021, 1000000)  # optimized auxiliary target 0.009021
c = Fraction(6, 5)               # auxiliary total-pressure multiplier
T = Fraction(7, 6)

A0 = eps0 * n
A1 = eps1 * n
assert A0 == Fraction(12103371, 5000000)
assert A1 == Fraction(1380213, 500000)

# Base: S + P >= A0.
# Auxiliary: S + c P >= A1.  The optimized auxiliary pressure distribution has
# the same exact total c*B, so translated pressure bookkeeping gives this line.
Sx = (c * A0 - A1) / (c - 1)
assert Sx == Fraction(451197, 625000)
assert 0 < Sx < T < A0 < A1

# On 0<=S<=Sx the base pressure line is active and g_6(S)=S, so
# g_6(S)+P >= A0 identically.  On Sx<=S<=A1 the auxiliary pressure
# line is active and g_6(S)+(A1-S)/c is concave, hence its minimum is
# at Sx or A1.  The following exact square witness proves g_6(A1)>A0.
square_gap = T * A1 - ((A0 + T) / 2) ** 2
assert square_gap == Fraction(2919038927231, 900000000000000)
assert square_gap > 0

# Therefore the two supporting lines plus the continuous banded profile give
# Delta + P >= A0: the scalar Gram discount disappears entirely.
R = A0
eta = Fraction(1)

bound = (m * H - B * n) / (m - R)
assert bound == Fraction(199798509242, 296680187225)

safe = Fraction(6734474287, 10000000000)
assert safe < bound < safe + Fraction(1, 10000000000)

# m=313 is beyond the full no-loss endpoint for the same exact targets.
n_next = 313 - q
A0_next = eps0 * n_next
A1_next = eps1 * n_next
next_square_gap = T * A1_next - ((A0_next + T) / 2) ** 2
assert next_square_gap < 0

print("multilag_exact_arithmetic_verified=True")
print("m=", m)
print("A0=", A0)
print("A1=", A1)
print("supporting_line_intersection=", Sx)
print("g_A1_over_A0_square_gap=", square_gap)
print("m313_square_gap_negative=True", next_square_gap)
print("R_equals_A0=True")
print("eta=1")
print("bound_fraction=", f"{bound.numerator}/{bound.denominator}")
print("bound=", float(bound))
print("percent=", float(bound * 100))
print("safe_decimal_floor=", float(safe))
