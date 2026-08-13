#!/usr/bin/env python3
"""Exact support/factor-count checks for an r=4 generalized Vaughan redesign.

This checks the algebraic support geometry implied by Bui--Heath-Brown Lemma 3.
It does not re-prove all subsequent large-sieve estimates with 11 factors.
"""

from __future__ import annotations

import argparse
from fractions import Fraction


def min_u(theta: Fraction, r: int) -> Fraction:
    return (1 + theta) / r


def max_a2_factors(r: int) -> int:
    # a2 = -Lambda * log * log * b.  In the j=r term of the HB identity,
    # Lambda contributes: one log (from zeta'), r-1 copies of 1 (zeta),
    # and r truncated mu factors.  Add the two external logs and b.
    return 3 + 1 + (r - 1) + r


def exact_checks() -> None:
    theta = Fraction(251, 500)  # 0.502

    assert min_u(theta, 3) == Fraction(751, 1500)
    assert min_u(theta, 3) > Fraction(1, 2)

    assert min_u(theta, 4) == Fraction(751, 2000)
    assert min_u(theta, 4) < Fraction(1, 2)

    u = Fraction(19, 50)  # 0.38
    assert u > min_u(theta, 4)
    assert 4 * u - (1 + theta) == Fraction(9, 500)
    assert u < Fraction(1, 2)

    assert max_a2_factors(3) == 9
    assert max_a2_factors(4) == 11

    # For any fixed theta<1, r=4 leaves a nonempty interval
    # ((1+theta)/4, 1/2) for the truncated-mu exponent u.
    for theta in (Fraction(1, 2), Fraction(251, 500), Fraction(3, 5), Fraction(4, 5), Fraction(99, 100)):
        assert min_u(theta, 4) < Fraction(1, 2)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--check", action="store_true")
    args = p.parse_args()
    exact_checks()
    if args.check:
        print("Gate-B r=4 support checks: PASS")
        return

    theta = Fraction(251, 500)
    print(f"theta={float(theta):.6f}")
    for r in (3, 4, 5):
        print(
            f"r={r}: u must exceed {float(min_u(theta,r)):.9f}; "
            f"max a2 factors={max_a2_factors(r)}"
        )
    u = Fraction(19, 50)
    print(f"chosen r=4 u={float(u):.6f}; support margin={float(4*u-(1+theta)):.6f}")
    print("NOTE: factor grouping/large-sieve estimates still require analytic rechecking.")


if __name__ == "__main__":
    main()
