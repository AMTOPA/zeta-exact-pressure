#!/usr/bin/env python3
"""Exact arithmetic for the two-certificate multi-lag banded-Gram experiment.

The arithmetic is conditional on interval certification of the auxiliary local
certificate in experiments/multilag/candidate.json and on acceptance of the
continuous banded-Gram analytic profile.  No floating-point value is used in
the proof checks below.
"""
from fractions import Fraction

q = 6
m = 173
n = m - q

H = Fraction(336094079, 500000000)
B = Fraction(93, 23000)
eps0 = Fraction(79107, 10000000)
eps1 = Fraction(15889, 2000000)  # 0.0079445 auxiliary target
delta = Fraction(1, 25)
T = Fraction(7, 6)

A0 = eps0 * n
A1 = eps1 * n

# The base certificate gives S+P >= A0.  The tilted certificate gives
# (26/25)E_odd + (24/25)E_even + P >= A1.  Since E_odd-E_even <= S,
# it implies (26/25)S + P >= A1.
Sx = (A1 - A0) / delta
assert Sx == Fraction(28223, 200000)
assert 0 < Sx < T < A0

# Rational floor below g_6(A0)=2*sqrt(T*A0)-T.
R = Fraction(131628967, 100000000)
square_gap = T * A0 - ((R + T) / 2) ** 2
assert square_gap == Fraction(2718616199, 360000000000000000)
assert square_gap > 0

# Choose eta so the two active pressure lines meet the target R exactly at Sx.
# Because Sx<T, g_6(Sx)=Sx.
eta = (R - Sx) / (A0 - Sx)
assert eta == Fraction(117517467, 117997190)

# Other endpoint in the first pressure regime is strictly above R.
assert eta * A1 > R
# At the other endpoint, g_6(A0)>R by the square witness above.
# On each interval the banded profile plus the relevant affine pressure term is
# concave, so the interval minimum occurs at an endpoint.

bound = (m * H - eta * B * n) / (m - R)
assert bound == Fraction(93944445751924037, 139502543089048315)

safe = Fraction(6734246105, 10000000000)
assert safe < bound < safe + Fraction(1, 10000000000)

print("multilag_exact_arithmetic_verified=True")
print("m=", m)
print("A0=", A0)
print("A1=", A1)
print("S_intersection=", Sx)
print("R_floor=", R)
print("band_profile_square_gap=", square_gap)
print("eta=", eta)
print("bound_fraction=", f"{bound.numerator}/{bound.denominator}")
print("bound=", float(bound))
print("percent=", float(bound * 100))
print("safe_decimal_floor=", float(safe))
