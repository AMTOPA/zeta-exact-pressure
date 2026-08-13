#!/usr/bin/env python3
"""Exponent bookkeeping for Mellin-smoothing of the BHB two-block family.

Assuming a product window of relative width delta=H/T, its Mellin transform has
size delta and frequency width delta^{-1}.  Dyadic hybrid-large-sieve summation
therefore leaves the Q^2 family diagonal unchanged but gains delta^(1/2) on the
mixed family/length term and delta on the pure-length term.

This script checks only that scaling model; it is not a proof of the weighted
hybrid large-sieve reduction.
"""

from __future__ import annotations

import argparse
from fractions import Fraction


def h_balanced(theta: Fraction) -> Fraction:
    return (1 + theta) / 2


def delta_exp(h: Fraction) -> Fraction:
    """delta=H/T=T^(h-1)."""
    return h - 1


def mellin_width_exp(h: Fraction) -> Fraction:
    """delta^{-1}=T^(1-h)."""
    return 1 - h


def mixed_gain_exp(h: Fraction) -> Fraction:
    """Extra exponent on the mixed term from delta^(1/2)."""
    return (h - 1) / 2


def length_gain_exp(h: Fraction) -> Fraction:
    """Extra exponent on the pure-length term from delta."""
    return h - 1


def exact_checks() -> None:
    theta = Fraction(251, 500)
    h = h_balanced(theta)
    assert h == Fraction(751, 1000)
    assert delta_exp(h) == Fraction(-249, 1000)
    assert mellin_width_exp(h) == Fraction(249, 1000)
    assert mixed_gain_exp(h) == Fraction(-249, 2000)
    assert length_gain_exp(h) == Fraction(-249, 1000)

    # The family-diagonal term has no delta factor in the weighted-L1 model.
    diagonal_gain = Fraction(0)
    assert diagonal_gain == 0

    # At every theta<1 with balanced h, the non-diagonal branches gain a power.
    for theta in (Fraction(1, 2), Fraction(251, 500), Fraction(3, 5), Fraction(4, 5)):
        h = h_balanced(theta)
        assert mixed_gain_exp(h) < 0
        assert length_gain_exp(h) < 0
        assert mellin_width_exp(h) > 0


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--check", action="store_true")
    args = p.parse_args()
    exact_checks()
    if args.check:
        print("smooth-family geometry checks: PASS")
        return

    theta = Fraction(251, 500)
    h = h_balanced(theta)
    print(f"theta={float(theta):.6f}, h={float(h):.6f}")
    print(f"delta=H/T = T^{float(delta_exp(h)):.6f}")
    print(f"effective Mellin width = T^{float(mellin_width_exp(h)):.6f}")
    print(f"mixed hybrid branch extra factor = T^{float(mixed_gain_exp(h)):.6f}")
    print(f"pure-length branch extra factor = T^{float(length_gain_exp(h)):.6f}")
    print("family diagonal extra factor = T^0 (no gain)")


if __name__ == "__main__":
    main()
