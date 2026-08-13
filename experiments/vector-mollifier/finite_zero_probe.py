#!/usr/bin/env python3
"""Finite-height discovery probe for arithmetic-shape mollifier directions.

This script is NOT a proof and its output is NOT an asymptotic simple-zero bound.
It is only a go/no-go diagnostic for whether a new coefficient direction is worth
an analytic main-term derivation.
"""

import argparse
import math
from typing import Dict, List, Tuple

import mpmath as mp
import numpy as np


def factor_squarefree(n: int) -> Tuple[int, List[int]]:
    """Return (mu(n), prime divisors) for squarefree n, else (0, [])."""
    if n == 1:
        return 1, []
    x = n
    primes: List[int] = []
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            primes.append(p)
            if x % p == 0:
                return 0, []
            while x % p == 0:
                x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        primes.append(x)
    mu = -1 if len(primes) % 2 else 1
    return mu, primes


def optimal_scalar_weight(u: float, theta: float) -> float:
    return -theta * u * u + (1.0 + theta) * u


def build_coefficients(y: float, theta: float):
    logy = math.log(y)
    rows = []
    for n in range(1, int(y) + 1):
        mu, primes = factor_squarefree(n)
        if mu == 0:
            continue
        u = math.log(y / n) / logy
        r2 = sum((math.log(p) / logy) ** 2 for p in primes)
        base = mu * optimal_scalar_weight(u, theta)
        # Vanishes at both cutoff endpoints.  R2 is genuinely prime-shape data:
        # unlike R1=log(n)/log(y), it is not determined by u alone.
        shape = mu * u * (1.0 - u) * r2
        rows.append((n, base, shape))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zeros", type=int, default=200)
    parser.add_argument("--theta", type=float, default=0.49)
    parser.add_argument("--dps", type=int, default=25)
    args = parser.parse_args()

    if not (0.0 < args.theta < 0.5):
        raise SystemExit("theta must lie in (0, 1/2)")
    if args.zeros < 2:
        raise SystemExit("need at least two zeros")

    mp.mp.dps = args.dps

    zero_data: List[Tuple[float, complex]] = []
    for index in range(1, args.zeros + 1):
        rho = mp.zetazero(index)
        derivative = mp.diff(mp.zeta, rho)
        zero_data.append((float(mp.im(rho)), complex(derivative)))

    T = zero_data[-1][0]
    y = T ** args.theta
    coeffs = build_coefficients(y, args.theta)

    mollifier_values = np.zeros((args.zeros, 2), dtype=np.complex128)
    zprime = np.empty(args.zeros, dtype=np.complex128)

    for row, (gamma, derivative) in enumerate(zero_data):
        rho = 0.5 + 1j * gamma
        zprime[row] = derivative
        for n, base, shape in coeffs:
            phase = n ** (-rho)
            mollifier_values[row, 0] += base * phase
            mollifier_values[row, 1] += shape * phase

    X = mollifier_values * zprime[:, None]
    first = X.sum(axis=0)
    second = X.conj().T @ X

    scalar = (abs(first[0]) ** 2 / second[0, 0].real) / args.zeros
    vector = (
        np.vdot(first, np.linalg.solve(second, first)).real / args.zeros
    )

    print(f"zeros={args.zeros}")
    print(f"T={T:.12f}")
    print(f"theta={args.theta:.6f}")
    print(f"y={y:.12f}")
    print(f"squarefree_coefficients={len(coeffs)}")
    print(f"scalar_finite_rayleigh={scalar:.12f}")
    print(f"scalar_plus_R2_finite_rayleigh={vector:.12f}")
    print(f"finite_gain={vector - scalar:.12f}")
    print("DISCOVERY_ONLY=true")


if __name__ == "__main__":
    main()
