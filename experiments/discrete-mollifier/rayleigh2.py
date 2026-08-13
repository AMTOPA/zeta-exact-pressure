#!/usr/bin/env python3
"""Two-dimensional Rayleigh quotient utility for a future genuine mollifier basis.

Given first-moment vector u=(u0,u1) and positive-definite covariance
Q=[[q00,q01],[q01,q11]], the optimal Cauchy quotient is u^T Q^{-1} u.

The initially proposed (mu, mu*Lambda) basis is rank-one after polynomial
smoothing and should NOT be fed to this utility as if it were independent.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, getcontext

getcontext().prec = 60


def D(x: str) -> Decimal:
    return Decimal(x)


def optimize(u0: Decimal, u1: Decimal, q00: Decimal, q01: Decimal, q11: Decimal):
    det = q00 * q11 - q01 * q01
    if det <= 0:
        raise ValueError("Q must be positive definite: determinant must be positive")

    # alpha = Q^{-1} u; overall scaling is irrelevant.
    a0 = (q11 * u0 - q01 * u1) / det
    a1 = (-q01 * u0 + q00 * u1) / det
    value = u0 * a0 + u1 * a1
    return value, a0, a1, det


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--u0", required=True)
    p.add_argument("--u1", required=True)
    p.add_argument("--q00", required=True)
    p.add_argument("--q01", required=True)
    p.add_argument("--q11", required=True)
    args = p.parse_args()

    value, a0, a1, det = optimize(
        D(args.u0), D(args.u1), D(args.q00), D(args.q01), D(args.q11)
    )
    print(f"det(Q) = {det}")
    print(f"Q^-1 u  = ({a0}, {a1})")
    print(f"optimum = {value}")


if __name__ == "__main__":
    main()
