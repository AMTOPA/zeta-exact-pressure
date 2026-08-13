#!/usr/bin/env python3
"""Exact arithmetic for the five-supporting-line pressure-frontier candidate."""
from fractions import Fraction

q = 6
m = 525
n = m - q
H = Fraction(336094079, 500000000)
B = Fraction(93, 23000)
T = Fraction(7, 6)

# c=1, 11/10, 6/5, 8/5, 2.
cs = [Fraction(1), Fraction(11,10), Fraction(6,5), Fraction(8,5), Fraction(2)]
eps = [
    Fraction(79107, 10000000),
    Fraction(8477, 1000000),
    Fraction(9021, 1000000),
    Fraction(11129, 1000000),
    Fraction(23, 2000),       # tightened c=2 target 0.0115
]
A0,A11,A12,A16,A20 = [e*n for e in eps]
assert A0 == Fraction(41056533,10000000)
assert A11 == Fraction(4399563,1000000)
assert A12 == Fraction(4681899,1000000)
assert A16 == Fraction(5775951,1000000)
assert A20 == Fraction(11937,2000)

c0,c11,c12,c16,c20 = cs
S01 = (c11*A0-A11)/(c11-c0)
S12 = (c11*A12-c12*A11)/(c11-c12)
S23 = (c12*A16-c16*A12)/(c12-c16)
S34 = (c16*A20-c20*A16)/(c16-c20)
assert S01 == Fraction(11665563,10000000)
assert S12 == Fraction(1293867,1000000)
assert S23 == Fraction(1399743,1000000)
assert S34 == Fraction(1001151,200000)
assert S01 < T < S12 < S23 < S34
assert T-S01 == Fraction(3311,30000000) > 0

# Nonadjacent pair intersections lie inside the adjacent switch intervals;
# therefore the active envelope really follows the stated five-line order.
def inter(i,j):
    return (cs[j]*[A0,A11,A12,A16,A20][i] - cs[i]*[A0,A11,A12,A16,A20][j])/(cs[j]-cs[i])
assert S01 < inter(0,2) < S12
assert S12 < inter(1,3) < S23
assert S23 < inter(2,4) < S34

# Linear-band checkpoint on the c=11/10 branch.
fT = T + (A11-T)/c11
assert fT-A0 == Fraction(301,30000000) > 0

# Nonlinear switch/end checkpoints.  Concavity on each active affine branch
# reduces the global check to these exact square witnesses.
def square_witness(S, Aline, c):
    p=(Aline-S)/c
    R=A0-p
    return p,R,T*S-((R+T)/2)**2

p12,R12,sq12=square_witness(S12,A11,c11)
assert p12 == Fraction(8823,3125)
assert R12 == Fraction(12822933,10000000)
assert sq12 == Fraction(36576973497599,3600000000000000) > 0

p23,R23,sq23=square_witness(S23,A12,c12)
assert p23 == Fraction(273513,100000)
assert R23 == Fraction(13705233,10000000)
assert sq23 == Fraction(85320965741399,3600000000000000) > 0

p34,R34,sq34=square_witness(S34,A16,c16)
assert p34 == Fraction(192549,400000)
assert R34 == Fraction(4530351,1250000)
assert sq34 == Fraction(5723611476191,56250000000000) > 0

sq_end=T*A20-((A0+T)/2)**2
assert sq_end == Fraction(50077952179199,3600000000000000) > 0

# Full no-loss conclusion: R=A0, eta=1.
bound=(m*H-B*n)/(m-A0)
assert bound == Fraction(53789366719,79870466494)
safe=Fraction(3367287627,5000000000)  # 0.6734575254
assert safe < bound < safe + Fraction(1,10**10)

# m=526 crosses the first low-energy switch for this exact c=11/10 target.
n2=526-q
A02=eps[0]*n2
A112=eps[1]*n2
S012=(c11*A02-A112)/(c11-c0)
assert S012-T == Fraction(1603,750000) > 0

print('pressure_bundle5_exact_arithmetic_verified=True')
print('m=',m)
print('S01=',S01)
print('S12=',S12)
print('S23=',S23)
print('S34=',S34)
print('linear_margin=',fT-A0)
print('switch12_square_gap=',sq12)
print('switch23_square_gap=',sq23)
print('switch34_square_gap=',sq34)
print('end_square_gap=',sq_end)
print('bound_fraction=',f'{bound.numerator}/{bound.denominator}')
print('bound=',float(bound))
print('percent=',float(bound*100))
print('safe_decimal_floor=',float(safe))
