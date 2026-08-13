#!/usr/bin/env python3
"""Exact endpoint checks for the root-tightened trace-corrected m=576 projection.

The local root target epsilon=0.0079110 is interval-certified separately.  The
matrix step is the trace-corrected banded-Gram lemma in
experiments/banded-gram/TRACE_CORRECTION.md and remains an analytic lemma under
review.  This script checks only the exact rational consequences.
"""
from fractions import Fraction

m = 576
q = 6
n = m - q
T = Fraction(7, 6)
H = Fraction(336094079, 500000000)
B = Fraction(93, 23000)

# c, epsilon, label.  The c=11/10 line remains certified but is redundant in
# the active envelope at this block length.
lines = [
    (Fraction(1), Fraction(7911, 1_000_000), "base-tight"),
    (Fraction(21, 20), Fraction(82051, 10_000_000), "c105-tight"),
    (Fraction(11, 10), Fraction(8477, 1_000_000), "c11"),
    (Fraction(6, 5), Fraction(9021, 1_000_000), "c12"),
    (Fraction(8, 5), Fraction(11129, 1_000_000), "c16"),
    (Fraction(2), Fraction(61, 5000), "c20"),
]
A = [eps * n for c, eps, name in lines]
A0 = A[0]
assert A0 == Fraction(450927, 100000)


def inter(i: int, j: int) -> Fraction:
    ci, cj = lines[i][0], lines[j][0]
    return (cj * A[i] - ci * A[j]) / (cj - ci)


# Active envelope: base -> 21/20 -> 6/5 -> 8/5 -> 2.
S01 = inter(0, 1)
S13 = inter(1, 3)
S34 = inter(3, 4)
S45 = inter(4, 5)
assert S01 == Fraction(115653, 100000)
assert S13 == Fraction(710733, 500000)
assert S34 == Fraction(153729, 100000)
assert S45 == Fraction(78033, 20000)
assert S01 < T < S13 < S34 < S45

# c=11/10 is below the active pressure envelope wherever it could compete.
for S in (S01, T, S13):
    p11 = (A[2] - S) / lines[2][0]
    penv = max((A[i] - S) / lines[i][0] for i in (0, 1, 3, 4, 5))
    assert p11 <= penv

# Linear-region endpoint at E=T on the c=21/20 branch.
pT = (A[1] - T) / lines[1][0]
linear_margin = T + pT - A0
assert linear_margin == Fraction(3041, 6300000) > 0

# For E>=T, use the trace-corrected profile
#   g_tr(E) = [E + m(2 sqrt(E/T)-1)] / D,  D=1+m/T.
# To prove g_tr(E)+P >= A0, put R=A0-P and rearrange to
# sqrt(E/T) >= Q=(D R-E+m)/(2m).  Q is positive at each endpoint, so
# exact squaring is legitimate.
D = Fraction(1) + Fraction(m, 1) / T


def witness(E: Fraction, line_index: int):
    c = lines[line_index][0]
    P = (A[line_index] - E) / c
    R = A0 - P
    Q = (D * R - E + m) / (2 * m)
    assert Q > 0
    gap = E / T - Q * Q
    return P, R, Q, gap


_, _, Q13, sq13 = witness(S13, 1)
assert Q13 == Fraction(1112612161, 1008000000)
assert sq13 == Fraction(65976186910079, 1016064000000000000) > 0

_, _, Q34, sq34 = witness(S34, 3)
assert Q34 == Fraction(38476397, 33600000)
assert sq34 == Fraction(7171661098391, 1128960000000000) > 0

_, _, Q45, sq45 = witness(S45, 4)
assert Q45 == Fraction(955676429, 537600000)
assert sq45 == Fraction(53223023085807959, 289013760000000000) > 0

Eend = A[5]
_, _, Qend, sqend = witness(Eend, 5)
assert Eend == Fraction(3477, 500)
assert Qend == Fraction(653297467, 268800000)
assert sqend == Fraction(3874209691383911, 72253440000000000) > 0

# Hence all active segments satisfy Delta+P >= A0, and eta=1.
bound = (m * H - B * n) / (m - A0)
assert bound == Fraction(61473185536, 91279769375)
safe = Fraction(6734590365, 10**10)
assert safe < bound < safe + Fraction(1, 10**10)

# The same exact targets do not give full no-loss at m=577: the first
# nonlinear active switch (21/20 -> 6/5) has a negative square witness.
m2 = 577
n2 = m2 - q
A2 = [eps * n2 for c, eps, name in lines]
A02 = A2[0]
S13_2 = (
    lines[3][0] * A2[1] - lines[1][0] * A2[3]
) / (lines[3][0] - lines[1][0])
D2 = Fraction(1) + Fraction(m2, 1) / T
P2 = (A2[1] - S13_2) / lines[1][0]
R2 = A02 - P2
Q2 = (D2 * R2 - S13_2 + m2) / (2 * m2)
sq2 = S13_2 / T - Q2 * Q2
assert sq2 == Fraction(-503181768195566329, 3670542225000000000000) < 0

print("trace_root_tightening_exact_arithmetic_verified=True")
print("m=", m)
print("A0=", A0)
print("S01=", S01)
print("S13=", S13)
print("S34=", S34)
print("S45=", S45)
print("linear_margin=", linear_margin)
print("switch13_square_gap=", sq13)
print("switch34_square_gap=", sq34)
print("switch45_square_gap=", sq45)
print("end_square_gap=", sqend)
print("m577_first_nonlinear_square_gap_negative=", sq2)
print("bound_fraction=", f"{bound.numerator}/{bound.denominator}")
print("bound=", float(bound))
print("percent=", float(bound * 100))
print("safe_decimal_floor=", float(safe))
