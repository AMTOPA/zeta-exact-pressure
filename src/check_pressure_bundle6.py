#!/usr/bin/env python3
"""Exact arithmetic for the six-supporting-line m=576 pressure-frontier candidate."""
from fractions import Fraction

q=6
m=576
n=m-q
H=Fraction(336094079,500000000)
B=Fraction(93,23000)
T=Fraction(7,6)

# c = 1, 21/20, 11/10, 6/5, 8/5, 2.
cs=[Fraction(1),Fraction(21,20),Fraction(11,10),Fraction(6,5),Fraction(8,5),Fraction(2)]
eps=[Fraction(79107,10_000_000),Fraction(1641,200000),Fraction(8477,1_000_000),Fraction(9021,1_000_000),Fraction(11129,1_000_000),Fraction(61,5000)]
A=[e*n for e in eps]
A0=A[0]
assert A0==Fraction(4509099,1_000_000)

# c=11/10 is exactly redundant at these conservative targets: its line meets
# the c=21/20 and c=6/5 lines at the same point.  The active envelope is
# c=1 -> 21/20 -> 6/5 -> 8/5 -> 2.
active=[0,1,3,4,5]
def inter(i,j):
    return (cs[j]*A[i]-cs[i]*A[j])/(cs[j]-cs[i])
S01=inter(0,1)
S13=inter(1,3)
S34=inter(3,4)
S45=inter(4,5)
assert S01==Fraction(1154079,1_000_000)
assert S13==Fraction(142101,100000)
assert S34==Fraction(153729,100000)
assert S45==Fraction(78033,20000)
assert S01 < T < S13 < S34 < S45
assert inter(1,2)==S13 and inter(2,3)==S13

# Low linear region: equality occurs at S01.  The c=21/20 branch is increasing
# until T, with an exact positive margin there.
pT=(A[1]-T)/cs[1]
assert T+pT-A0==Fraction(37763,63000000)>0

# On every nonlinear active segment, g_6 plus an affine pressure branch is
# concave, so it suffices to check the switch endpoints by exact squaring.
def witness(S,line_index):
    p=(A[line_index]-S)/cs[line_index]
    R=A0-p
    return p,R,T*S-((R+T)/2)**2

p13,R13,sq13=witness(S13,1)
assert p13==Fraction(1938,625)
assert R13==Fraction(1408299,1_000_000)
assert sq13==Fraction(8386339391,36000000000000)>0

p34,R34,sq34=witness(S34,3)
assert p34==Fraction(30039,10000)
assert R34==Fraction(1505199,1_000_000)
assert sq34==Fraction(316384733591,36000000000000)>0

p45,R45,sq45=witness(S45,4)
assert p45==Fraction(61047,40000)
assert R45==Fraction(745731,250000)
assert sq45==Fraction(556085980751,2250000000000)>0

# c=2 far endpoint, where its pressure line reaches zero.
Send=A[5]
sqend=T*Send-((A0+T)/2)**2
assert Send==Fraction(3477,500)
assert sqend==Fraction(2139156873791,36000000000000)>0

# Thus Delta+P >= A0, so R=A0 and eta=1.
bound=(m*H-B*n)/(m-A0)
assert bound==Fraction(122946371072,182559593375)
safe=Fraction(6734588349,10**10)
assert safe < bound < safe+Fraction(1,10**10)

# m=577 fails the c=21/20 -> c=6/5 nonlinear switch for these exact targets.
n2=571
A2=[e*n2 for e in eps]
def inter2(i,j):
    return (cs[j]*A2[i]-cs[i]*A2[j])/(cs[j]-cs[i])
Sfail=inter2(1,3)
pfail=(A2[1]-Sfail)/cs[1]
Rfail=A2[0]-pfail
sqfail=T*Sfail-((Rfail+T)/2)**2
assert Sfail==Fraction(1423503,1_000_000)
assert sqfail==Fraction(-147801794281,3600000000000000)<0

print('pressure_bundle6_exact_arithmetic_verified=True')
print('m=',m)
print('S01=',S01)
print('S13=',S13)
print('S34=',S34)
print('S45=',S45)
print('switch13_square_gap=',sq13)
print('switch34_square_gap=',sq34)
print('switch45_square_gap=',sq45)
print('end_square_gap=',sqend)
print('m577_switch_square_gap_negative=',sqfail)
print('bound_fraction=',f'{bound.numerator}/{bound.denominator}')
print('bound=',float(bound))
print('percent=',float(bound*100))
print('safe_decimal_floor=',float(safe))
