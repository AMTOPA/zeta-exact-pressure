#!/usr/bin/env python3
"""Algebraic go/no-go checks for a genuine Feng-type k=2 mollifier piece.

This file does NOT provide the mixed zeta'-moment asymptotics.  It checks two
necessary facts before that harder analytic work is attempted:

1. the k=2 prime-factor statistic is genuinely outside the old polynomial-smoothed
   mu(n) space generated only by log n;
2. a future two-piece Rayleigh quotient must gain at least 17/2700 over 19/27
   to reach 71% at theta=1/2.
"""

from __future__ import annotations

import argparse
from fractions import Fraction


BASELINE = Fraction(19, 27)
TARGET_71 = Fraction(71, 100)
TARGET_72 = Fraction(18, 25)
TARGET_73 = Fraction(73, 100)


def exact_independence_check() -> None:
    """Prove e2 is not a polynomial in e1 by exact homogeneous coefficient comparison.

    For two formal prime-log variables x,y,
        e1 = x+y,
        e2 = xy.
    If e2=F(e1) as a universal polynomial identity, homogeneity forces
    F(t)=a*t^2.  Comparing x^2 gives a=0, while comparing xy then gives
    0=1, a contradiction.
    """

    # Coefficients in monomial order x^2, xy, y^2.
    e1_squared = (1, 2, 1)
    e2 = (0, 1, 0)

    # x^2 coefficient forces a=0.
    a = Fraction(e2[0], e1_squared[0])
    assert a == 0
    # Then the xy coefficient cannot match.
    assert a * e1_squared[1] != e2[1]


def schur_gain_targets() -> dict[str, Fraction]:
    return {
        "71%": TARGET_71 - BASELINE,
        "72%": TARGET_72 - BASELINE,
        "73%": TARGET_73 - BASELINE,
    }


def exact_gain_checks() -> None:
    gains = schur_gain_targets()
    assert gains["71%"] == Fraction(17, 2700)
    assert gains["72%"] == Fraction(11, 675)
    assert gains["73%"] == Fraction(71, 2700)
    assert all(g > 0 for g in gains.values())


def schur_gain(u0: Fraction, u1: Fraction, q00: Fraction, q01: Fraction, q11: Fraction) -> Fraction:
    """Exact incremental Rayleigh gain from adding piece 1 to piece 0.

    For real symmetric Q, the improvement is
      (u1-q01*u0/q00)^2 / (q11-q01^2/q00).
    """
    if q00 <= 0:
        raise ValueError("q00 must be positive")
    residual_variance = q11 - q01 * q01 / q00
    if residual_variance <= 0:
        raise ValueError("Q must have positive Schur complement")
    residual_signal = u1 - q01 * u0 / q00
    return residual_signal * residual_signal / residual_variance


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    exact_independence_check()
    exact_gain_checks()

    if args.check:
        print("Feng k=2 rank/gain checks: PASS")
        return

    print("Feng k=2 arithmetic direction passes the algebraic rank test.")
    print("It is not reducible to a universal polynomial in log(n).")
    print(f"BHB one-piece baseline = {BASELINE} = {float(BASELINE):.12f}")
    for label, gain in schur_gain_targets().items():
        print(f"minimum Rayleigh gain for {label}: {gain} = {float(gain):.12f}")
    print("No mixed-moment theorem is claimed; u1, q01 and q11 remain to be derived.")


if __name__ == "__main__":
    main()
