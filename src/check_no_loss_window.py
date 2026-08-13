#!/usr/bin/env python3
"""Exact arithmetic for experiments/no-loss-window/frontier.json.

This checks the rational pressure-frontier deduction conditional on the
continuous banded-Gram profile.  Local interval certification and the H/window
interval checks are performed separately by the shared workflow.
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
c=json.loads((ROOT/'experiments'/'no-loss-window'/'frontier.json').read_text())

def rat(x): return Fraction(int(x['numerator']),int(x['denominator']))

H=rat(c['window']['projection_h_floor'])
assert H==Fraction(1344361,2000000)
B=Fraction(93,23000)
T=Fraction(7,6)

lines=c['supporting_lines']
cs=[rat(x['scale']) for x in lines]
eps=[rat(x['target']) for x in lines]
assert cs==[Fraction(1),Fraction(21,20),Fraction(6,5),Fraction(8,5),Fraction(2)]
assert eps==[Fraction(3963,500000),Fraction(8231,1000000),Fraction(1129,125000),Fraction(2227,200000),Fraction(13,1000)]

for line,scale in zip(lines,cs):
    p=line['pressure']
    total=Fraction(sum(map(int,p['numerators'])),int(p['denominator']))
    assert total==rat(p['total'])
    assert total==scale*B

# Pair-span capacities stay exactly 2.
p=c['pair_weights']
for s in range(1,7):
    total=sum(int(n) for i,j,n in p['entries'] if int(j)-int(i)==s)
    assert Fraction(total,int(p['denominator']))==2

m=580
n=m-6
A=[e*n for e in eps]
A0=A[0]
assert A0==Fraction(1137381,250000)

def inter(i,j,Avals=A):
    return (cs[j]*Avals[i]-cs[i]*Avals[j])/(cs[j]-cs[i])

S01=inter(0,1)
S12=inter(1,2)
S23=inter(2,3)
S34=inter(3,4)
assert S01==Fraction(262031,250000)
assert S12==Fraction(23534,15625)
assert S23==Fraction(781501,500000)
assert S34==Fraction(42189,20000)
assert S01<T<S12<S23<S34

# The c=21/20 branch increases through the linear part.
pT=(A[1]-T)/cs[1]
assert T+pT-A0==Fraction(12701,2250000)>0

# On nonlinear active intervals, g_6(S)+(A_i-S)/c_i is concave.  Exact
# positive square witnesses at every switch and the far endpoint suffice.
def witness(S,i):
    pressure=(A[i]-S)/cs[i]
    R=A0-pressure
    return pressure,R,T*S-((R+T)/2)**2

p12,R12,sq12=witness(S12,1)
assert p12==Fraction(76629,25000)
assert R12==Fraction(371091,250000)
assert sq12==Fraction(482477471,2250000000000)>0

p23,R23,sq23=witness(S23,2)
assert p23==Fraction(603561,200000)
assert R23==Fraction(1531719,1000000)
assert sq23==Fraction(114517145351,36000000000000)>0

p34,R34,sq34=witness(S34,3)
assert p34==Fraction(107051,40000)
assert R34==Fraction(1873249,1000000)
assert sq34==Fraction(5427114655991,36000000000000)>0

Send=A[4]
sqend=T*Send-((A0+T)/2)**2
assert Send==Fraction(3731,500)
assert sqend==Fraction(1208154897551,2250000000000)>0

bound=(m*H-B*n)/(m-A0)
assert bound==rat(c['projection']['exact_bound'])
assert bound==Fraction(4456752935,6617680474)
safe=rat(c['projection']['safe_decimal_floor'])
assert safe<bound<safe+Fraction(1,10**10)

# m=581 genuinely leaves this full-no-loss regime at the c=21/20 -> 6/5
# nonlinear switch.
n2=581-6
A2=[e*n2 for e in eps]
Sfail=(cs[2]*A2[1]-cs[1]*A2[2])/(cs[2]-cs[1])
pfail=(A2[1]-Sfail)/cs[1]
Rfail=A2[0]-pfail
sqfail=T*Sfail-((Rfail+T)/2)**2
assert Sfail==Fraction(943,625)
assert sqfail==Fraction(-2213089,14400000000)<0

print('no_loss_window_exact_arithmetic_verified=True')
print('m=',m)
print('S01=',S01)
print('S12=',S12)
print('S23=',S23)
print('S34=',S34)
print('switch12_square_gap=',sq12)
print('switch23_square_gap=',sq23)
print('switch34_square_gap=',sq34)
print('end_square_gap=',sqend)
print('m581_square_gap_negative=',sqfail)
print('bound_fraction=',f'{bound.numerator}/{bound.denominator}')
print('bound=',float(bound))
print('percent=',float(bound*100))
print('safe_decimal_floor=',float(safe))
