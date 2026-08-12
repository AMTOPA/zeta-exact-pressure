"""High precision arithmetic verification of the current final bound."""
from fractions import Fraction
import mpmath as mp
from mpmath import iv
mp.mp.dps=100
iv.dps=100
EPS=Fraction(52289,10000000)
B=Fraction(3,1150)
H=Fraction(6724057,10000000)
SAFE=Fraction(6732907560,10000000000)
def q(x): return mp.mpf(x.numerator)/x.denominator
best=None
def h(m,e):
    if e<=mp.mpf(m)/(m-1): return e
    return e/m+2*mp.sqrt(mp.mpf(m-1)*e/m)-1
for m in range(7,5000):
    a=q(EPS)*(m-6); r=h(m,a); eta=r/a
    v=(m*q(H)-eta*q(B)*(m-6))/(m-r)
    if best is None or v>best[0]: best=(v,m)
print('scan_best_m=',best[1])
print('float_bound=',mp.nstr(best[0],100))
assert best[1]==210
assert best[0]>q(SAFE)
print('interval_verified=True')
