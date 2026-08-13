#!/usr/bin/env python3
"""Exact exponent bookkeeping for the entire-weight smoothing proposal.

This script checks the *consequence* of the candidate kernel remainder
    E_kernel ~ T^(2-sigma)/H^2 + T^(-sigma)
after summing the Bui--Heath-Brown coefficient ranges.  It does not prove the
stationary-phase kernel estimate itself.
"""

from __future__ import annotations

import argparse
from fractions import Fraction


def balanced_h(theta: Fraction) -> Fraction:
    """Balance transform-error exponent 1+theta-h with boundary exponent h."""
    if not 0 < theta < 1:
        raise ValueError("theta must lie in (0,1)")
    return (1 + theta) / 2


def transform_error_exp(theta: Fraction, h: Fraction) -> Fraction:
    """Exponent in y*T/H = T^(1+theta-h)."""
    return 1 + theta - h


def relative_boundary_exp(h: Fraction) -> Fraction:
    """Exponent of H/T."""
    return h - 1


def weight_curvature_exp(h: Fraction) -> Fraction:
    """Exponent of the relative stationary-phase curvature term T/H^2."""
    return 1 - 2 * h


def exact_checks() -> None:
    for theta in (
        Fraction(1, 2),
        Fraction(251, 500),
        Fraction(51, 100),
        Fraction(3, 5),
        Fraction(7, 10),
    ):
        h = balanced_h(theta)
        assert h > theta
        assert h < 1
        assert h > Fraction(1, 2)
        assert transform_error_exp(theta, h) == h
        assert transform_error_exp(theta, h) < 1
        assert relative_boundary_exp(h) < 0
        assert weight_curvature_exp(h) < 0

    # First endpoint-crossing milestone.
    theta = Fraction(251, 500)  # 0.502
    h = balanced_h(theta)
    assert h == Fraction(751, 1000)
    assert transform_error_exp(theta, h) == Fraction(751, 1000)
    assert relative_boundary_exp(h) == Fraction(-249, 1000)
    assert weight_curvature_exp(h) == Fraction(-251, 500)

    # Even the 71% formal theta has enormous Gate-A room if the kernel lemma holds.
    # Use a rational upper proxy theta=0.511.
    theta = Fraction(511, 1000)
    h = balanced_h(theta)
    assert h == Fraction(1511, 2000)
    assert transform_error_exp(theta, h) == h < 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    exact_checks()

    if args.check:
        print("analytic-smoothing exponent checks: PASS")
        return

    for theta in (
        Fraction(251, 500),
        Fraction(511, 1000),
        Fraction(53, 100),
        Fraction(3, 5),
    ):
        h = balanced_h(theta)
        print(
            f"theta={float(theta):.6f}  h={float(h):.6f}  "
            f"transform_error=T^{float(transform_error_exp(theta,h)):.6f}  "
            f"H/T=T^{float(relative_boundary_exp(h)):.6f}  "
            f"T/H^2=T^{float(weight_curvature_exp(h)):.6f}"
        )

    print("NOTE: these are bookkeeping consequences, not a proof of the kernel lemma.")


if __name__ == "__main__":
    main()
