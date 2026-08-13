#!/usr/bin/env python3
"""Finite-height discovery probe for a Feng-type arithmetic-shape mollifier.

This script is NOT a proof and its output is NOT an asymptotic simple-zero bound.
It compares a scalar polynomial mollifier subspace with the same subspace enlarged
by one genuinely arithmetic two-prime direction.
"""

import argparse
import math
from typing import List, Tuple

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
        p = 3 if p == 2 else p + 2
    if x > 1:
        primes.append(x)
    mu = -1 if len(primes) % 2 else 1
    return mu, primes


def build_coefficients(y: float):
    logy = math.log(y)
    rows = []
    for n in range(1, int(y) + 1):
        mu, primes = factor_squarefree(n)
        if mu == 0:
            continue
        u = math.log(y / n) / logy
        logs = [math.log(p) / logy for p in primes]
        e2 = sum(
            logs[i] * logs[j]
            for i in range(len(logs))
            for j in range(i + 1, len(logs))
        )
        rows.append((n, mu, u, e2))
    return rows


def rayleigh(first: np.ndarray, second: np.ndarray) -> float:
    return float(np.vdot(first, np.linalg.solve(second, first)).real)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zeros", type=int, default=200)
    parser.add_argument("--theta", type=float, default=0.49)
    parser.add_argument("--scalar-degree", type=int, default=3)
    parser.add_argument("--dps", type=int, default=25)
    args = parser.parse_args()

    if not (0.0 < args.theta < 0.5):
        raise SystemExit("theta must lie in (0, 1/2)")
    if args.zeros < 2:
        raise SystemExit("need at least two zeros")
    if args.scalar_degree < 1:
        raise SystemExit("scalar-degree must be positive")

    mp.mp.dps = args.dps

    zero_data: List[Tuple[float, complex]] = []
    for index in range(1, args.zeros + 1):
        rho = mp.zetazero(index)
        derivative = mp.diff(mp.zeta, rho)
        zero_data.append((float(mp.im(rho)), complex(derivative)))

    T = zero_data[-1][0]
    y = T ** args.theta
    coeffs = build_coefficients(y)

    # Scalar subspace: mu(n) * u^k, 1 <= k <= degree.
    # Arithmetic direction: mu(n) * u(1-u) * E2(n;y), where
    # E2 is the normalized elementary symmetric sum over two distinct prime factors.
    dim = args.scalar_degree + 1
    mollifier_values = np.zeros((args.zeros, dim), dtype=np.complex128)
    zprime = np.empty(args.zeros, dtype=np.complex128)

    for row, (gamma, derivative) in enumerate(zero_data):
        rho = 0.5 + 1j * gamma
        zprime[row] = derivative
        for n, mu, u, e2 in coeffs:
            phase = n ** (-rho)
            for power in range(1, args.scalar_degree + 1):
                mollifier_values[row, power - 1] += mu * (u ** power) * phase
            mollifier_values[row, -1] += mu * u * (1.0 - u) * e2 * phase

    X = mollifier_values * zprime[:, None]
    first = X.sum(axis=0)
    second = X.conj().T @ X

    d = args.scalar_degree
    scalar_value = rayleigh(first[:d], second[:d, :d]) / args.zeros
    arithmetic_value = rayleigh(first, second) / args.zeros

    print(f"zeros={args.zeros}")
    print(f"T={T:.12f}")
    print(f"theta={args.theta:.6f}")
    print(f"y={y:.12f}")
    print(f"squarefree_coefficients={len(coeffs)}")
    print(f"scalar_degree={args.scalar_degree}")
    print(f"scalar_subspace_finite_rayleigh={scalar_value:.12f}")
    print(f"scalar_plus_E2_finite_rayleigh={arithmetic_value:.12f}")
    print(f"finite_arithmetic_gain={arithmetic_value - scalar_value:.12f}")
    print(f"full_matrix_condition={np.linalg.cond(second):.6e}")
    print("DISCOVERY_ONLY=true")


if __name__ == "__main__":
    main()
