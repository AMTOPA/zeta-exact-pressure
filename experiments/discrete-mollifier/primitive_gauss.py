#!/usr/bin/env python3
"""Sanity/exact arithmetic checks for the squarefree primitive-Gauss collapse.

The proof is written in primitive_gauss_collapse.md.  This script verifies the
primitive-orthogonality formula numerically for many squarefree moduli and checks
additive reciprocity exactly with Fractions.
"""

from __future__ import annotations

import argparse
import cmath
import math
from fractions import Fraction


def factor(n: int) -> list[int]:
    ps=[]
    p=2
    while p*p<=n:
        if n%p==0:
            ps.append(p)
            while n%p==0: n//=p
        p+=1
    if n>1: ps.append(n)
    return ps


def is_squarefree(n: int) -> bool:
    p=2
    while p*p<=n:
        if n%(p*p)==0: return False
        p+=1
    return True


def divisors(n: int) -> list[int]:
    out=[1]
    for p in factor(n):
        out += [d*p for d in list(out)]
    return sorted(out)


def mobius_squarefree(n: int) -> int:
    if not is_squarefree(n): return 0
    return -1 if len(factor(n))%2 else 1


def phi(n: int) -> int:
    out=n
    for p in factor(n): out=out//p*(p-1)
    return out


def primitive_orthogonality(q: int, n: int) -> int:
    """Sum_{chi mod q primitive} chi(n), for gcd(n,q)=1."""
    if math.gcd(n,q)!=1: return 0
    total=0
    for d in divisors(q):
        if (n-1)%d==0:
            total += phi(d)*mobius_squarefree(q//d)
    return total


def lhs_via_orthogonality(q: int, c: int) -> complex:
    z=0j
    for x in range(q):
        if math.gcd(x,q)!=1: continue
        n=(c*pow(x,-1,q))%q
        z += cmath.exp(2j*math.pi*x/q)*primitive_orthogonality(q,n)
    return z


def rhs_divisor_formula(q: int, c: int) -> complex:
    z=0j
    for r in divisors(q):
        e=q//r
        if r==1:
            phase=1.0+0j
        else:
            phase=cmath.exp(2j*math.pi*((c*pow(e,-1,r))%r)/r)
        z += phi(r)*phase
    return z


def reciprocity_difference(a: int, b: int) -> Fraction:
    """Return abar/b + bbar/a - 1/(ab), which must be an integer."""
    if math.gcd(a,b)!=1: raise ValueError("a,b must be coprime")
    term1=Fraction(0) if b==1 else Fraction(pow(a,-1,b),b)
    term2=Fraction(0) if a==1 else Fraction(pow(b,-1,a),a)
    return term1+term2-Fraction(1,a*b)


def bhb_phase_difference(m: int,d: int,k: int,r: int,e: int) -> Fraction:
    """Check -md*(ke)^-1/r == md*r^-1/(ke)-md/(ker) mod 1."""
    a=k*e
    if math.gcd(a,r)!=1: raise ValueError("ke and r must be coprime")
    left=Fraction(0) if r==1 else -Fraction(m*d*pow(a,-1,r),r)
    right_first=Fraction(0) if a==1 else Fraction(m*d*pow(r,-1,a),a)
    right=right_first-Fraction(m*d,a*r)
    return left-right


def checks() -> None:
    for q in range(2,121):
        if not is_squarefree(q): continue
        for c in range(1,q):
            if math.gcd(c,q)!=1: continue
            err=abs(lhs_via_orthogonality(q,c)-rhs_divisor_formula(q,c))
            assert err<1e-8,(q,c,err)

    for a in range(1,30):
        for b in range(1,30):
            if math.gcd(a,b)==1:
                assert reciprocity_difference(a,b).denominator==1

    for q in (6,10,15,30,42,70):
        for r in divisors(q):
            e=q//r
            for k in (1,11,13):
                if math.gcd(k,q)!=1: continue
                diff=bhb_phase_difference(7,5,k,r,e)
                assert diff.denominator==1,(q,r,e,k,diff)


def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument("--check",action="store_true")
    args=p.parse_args()
    checks()
    if args.check:
        print("primitive-Gauss/reciprocity checks: PASS")
    else:
        print("squarefree primitive-Gauss formula checked for q<=120")
        print("BHB reciprocity phase checked exactly on sample squarefree blocks")
        print("See primitive_gauss_collapse.md for the exact proof and trust boundary.")


if __name__=="__main__":
    main()
