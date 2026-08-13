#!/usr/bin/env python3
"""Exact exponent algebra for the Bui--Heath-Brown critical corner.

This is a research reduction checker, not a proof of the target signed-family
estimate.  It verifies the exponent identities used to isolate the unresolved
X <= Q^3 corner and converts hypothetical Q^{-sigma} savings into formal
mollifier lengths/proportions.
"""

from __future__ import annotations

import argparse
from fractions import Fraction


def K(theta: Fraction) -> Fraction:
    return Fraction(1) - Fraction(1, 1) / (Fraction(1) + theta) ** 3


def e_R(alpha: Fraction, g: Fraction) -> Fraction:
    return 2 * alpha / 3 + Fraction(2, 3) - g / 3


def e_two_thirds(alpha: Fraction, g: Fraction) -> Fraction:
    return Fraction(5, 6) + alpha / 3 - g / 6


def x_minus_q3(alpha: Fraction, g: Fraction) -> Fraction:
    """Exponent of X/Q^3 when X=T^(1+alpha+g), Q=T^alpha."""
    return Fraction(1) - 2 * alpha + g


def sigma_required(theta: Fraction) -> Fraction:
    """Worst-corner modulus saving required after optimizing the old cutoff."""
    if theta <= Fraction(1, 2):
        return Fraction(0)
    return (2 * theta - 1) / (3 * theta)


def theta_from_sigma(sigma: Fraction) -> Fraction:
    """Endpoint satisfying sigma=(2 theta-1)/(3 theta)."""
    if sigma < 0 or 3 * sigma >= 2:
        raise ValueError("sigma must satisfy 0 <= sigma < 2/3")
    return Fraction(1, 1) / (2 - 3 * sigma)


def exact_checks() -> None:
    # The two old exponents cross T^1 on exactly the same hyperplane.
    samples = [
        (Fraction(1, 2), Fraction(0)),
        (Fraction(251, 500), Fraction(0)),
        (Fraction(3, 5), Fraction(1, 5)),
        (Fraction(7, 10), Fraction(2, 5)),
        (Fraction(11, 20), Fraction(1, 20)),
    ]
    for alpha, g in samples:
        h = 2 * alpha - g - 1
        assert e_R(alpha, g) - 1 == h / 3
        assert e_two_thirds(alpha, g) - 1 == h / 6
        assert x_minus_q3(alpha, g) == -h

    # alpha>=1/2 and g>=0 imply the optimized long-factor cutoff
    # R=Q^(4/3) T^(1/3) (K/D)^(1/3) has T-exponent >=1.
    for alpha, g in samples:
        if alpha >= Fraction(1, 2) and g >= 0:
            r_exp = 4 * alpha / 3 + Fraction(1, 3) + g / 3
            assert r_exp >= 1

    # First structural milestone theta=0.502.
    theta_502 = Fraction(251, 500)
    assert sigma_required(theta_502) == Fraction(2, 753)
    assert K(theta_502) == Fraction(1) - Fraction(500, 751) ** 3

    # CLMR's published sixth-moment error saving 11/1196 is ONLY a scale
    # comparison; no transfer to the BHB signed family is asserted here.
    clmr_sigma = Fraction(11, 1196)
    clmr_theta = theta_from_sigma(clmr_sigma)
    assert clmr_theta == Fraction(1196, 2359)
    assert sigma_required(clmr_theta) == clmr_sigma

    # Sanity: a positive fixed saving moves the formal endpoint past 1/2.
    assert clmr_theta > Fraction(1, 2)
    assert K(clmr_theta) > Fraction(19, 27)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    exact_checks()

    if args.check:
        print("critical-corner exact exponent checks: PASS")
        return

    milestones = [
        ("BHB endpoint", Fraction(1, 2)),
        ("first crossing", Fraction(251, 500)),
        ("CLMR-saving scale only", Fraction(1196, 2359)),
    ]
    for label, theta in milestones:
        print(
            f"{label:24s} theta={float(theta):.12f} "
            f"K={100*float(K(theta)):.10f}% "
            f"sigma_req={float(sigma_required(theta)):.10f}"
        )

    print("WARNING: the 2026 Dong--Robles--Zeindler 1/46 application was withdrawn;")
    print("it is intentionally not used as an input to this checker.")


if __name__ == "__main__":
    main()
