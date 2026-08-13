#!/usr/bin/env python3
"""Exact endpoint checks for the trace-corrected m=577 banded-Gram test.

The matrix lemma itself is analytic and lives in
experiments/banded-gram/TRACE_CORRECTION.md.  This script checks only its exact
rational consequences for the current pressure-frontier inputs, conditional on
certifying c=21/20 at epsilon=0.0082051.
"""
from fractions import Fraction

m=577
q=6
n=m-q
T=Fraction(7,6)
H=Fraction(336094079,500000000)
B=Fraction(93,23000)

# c, epsilon.  c=11/10 is retained as a certified line but is redundant in the
# active envelope at this block length.
lines=[
    (Fraction(1),Fraction(79107,10_000_000),'base'),
    (Fraction(21,20),Fraction(82051,10_000_000),'c105-tight'),
    (Fraction(11,10),Fraction(8477,1_000_000),'c11'),
    (Fraction(6,5),Fraction(9021,1_000_000),'c12'),
    (Fraction(8,5),Fraction(11129,1_000_000),'c16'),
    (Fraction(2),Fraction(61,5000),'c20'),
]
A=[e*n for c,e,name in lines]
A0=A[0]
assert A0==Fraction(45170097,10_000_000)

# Active envelope: base -> 21/20 -> 6/5 -> 8/5 -> 2.
def inter(i,j):
    ci,cj=lines[i][0],lines[j][0]
    return (cj*A[i]-ci*A[j])/(cj-ci)
S01=inter(0,1)
S13=inter(1,3)
S34=inter(3,4)
S45=inter(4,5)
assert S01==Fraction(11549617,10_000_000)
assert S13==Fraction(7119799,5_000_000)
assert S34==Fraction(1539987,1_000_000)
assert S45==Fraction(781699,200000)
assert S01<T<S13<S34<S45

# c=11/10 is below the active pressure envelope at representative points.
for S in (S01,T,S13):
    p11=(A[2]-S)/lines[2][0]
    penv=max((A[i]-S)/lines[i][0] for i in (0,1,3,4,5))
    assert p11<=penv

# Linear-region margin at T on the c=21/20 branch.
pT=(A[1]-T)/lines[1][0]
linear_margin=T+pT-A0
assert linear_margin==Fraction(351149,630000000)>0

# For E>=T, the trace-corrected profile is
# [E+m(2 sqrt(E/T)-1)] / D, D=1+m/T.
# To prove g_tr(E)+P >= A0, set R=A0-P and rearrange to
# sqrt(E/T) >= Q=(D R-E+m)/(2m).  All Q below are positive, so squaring is exact.
D=Fraction(1)+Fraction(m,1)/T

def witness(E,line_index):
    c=lines[line_index][0]
    P=(A[line_index]-E)/c
    R=A0-P
    Q=(D*R-E+m)/(2*m)
    assert Q>0
    gap=E/T-Q*Q
    return P,R,Q,gap

p13,R13,Q13,sq13=witness(S13,1)
assert sq13==Fraction(1495135357934815799,58728675600000000000000)>0

p34,R34,Q34,sq34=witness(S34,3)
assert sq34==Fraction(40713807727433029391,6525408400000000000000)>0

p45,R45,Q45,sq45=witness(S45,4)
assert sq45==Fraction(42485906007975043217,233050300000000000000)>0

# Far endpoint where c=2 pressure vanishes.
Eend=A[5]
Rend=A0
Qend=(D*Rend-Eend+m)/(2*m)
assert Qend>0
sqend=Eend/T-Qend*Qend
assert sqend==Fraction(44692790542901114993,932201200000000000000)>0

# Hence all active pressure-envelope segments satisfy Delta+P >= A0.
bound=(m*H-B*n)/(m-A0)
assert bound==Fraction(4433753022409,6583554388450)
safe=Fraction(6734588583,10**10)
assert safe<bound<safe+Fraction(1,10**10)

print('trace_banded_gram_exact_arithmetic_verified=True')
print('m=',m)
print('S01=',S01)
print('S13=',S13)
print('S34=',S34)
print('S45=',S45)
print('linear_margin=',linear_margin)
print('switch13_square_gap=',sq13)
print('switch34_square_gap=',sq34)
print('switch45_square_gap=',sq45)
print('end_square_gap=',sqend)
print('bound_fraction=',f'{bound.numerator}/{bound.denominator}')
print('bound=',float(bound))
print('percent=',float(bound*100))
print('safe_decimal_floor=',float(safe))
