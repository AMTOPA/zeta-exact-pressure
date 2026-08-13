#!/usr/bin/env python3
"""Exact/formal checks for the Bui--Heath-Brown one-piece mollifier model.

This script proves only algebraic identities inside the published main-term model.
It does NOT extend the analytic range theta < 1/2.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import pow


def kappa(theta: float) -> float:
    """Variational optimum 1 - (1 + theta)^(-3)."""
    return 1.0 - (1.0 + theta) ** -3


def theta_for_target(target: float) -> float:
    """Invert target = 1 - (1 + theta)^(-3)."""
    if not 0.0 < target < 1.0:
        raise ValueError("target must lie in (0,1)")
    return pow(1.0 / (1.0 - target), 1.0 / 3.0) - 1.0


def quadratic_data(theta: Fraction) -> tuple[Fraction, Fraction, Fraction, Fraction, Fraction]:
    """Return I, J, A, D, K for P(x)=-theta*x^2+(1+theta)*x."""
    I = (Fraction(3, 1) + theta) / 6
    J = (theta * theta + 3) / 3
    A = Fraction(1, 2) + theta * I
    D = Fraction(1, 3) + theta * I + theta * theta * I * I + J / (12 * theta)
    K = A * A / D
    return I, J, A, D, K


def exact_variational_checks() -> None:
    # Exact endpoint arithmetic at theta=1/2.
    theta = Fraction(1, 2)
    I, J, A, D, K = quadratic_data(theta)
    assert I == Fraction(7, 12)
    assert J == Fraction(13, 12)
    assert A == Fraction(19, 24)
    assert D == Fraction(57, 64)
    assert K == Fraction(19, 27)

    # Check the closed form K(theta)=1-(1+theta)^(-3) on several rational theta.
    for theta in (Fraction(1, 10), Fraction(1, 4), Fraction(2, 5), Fraction(1, 2), Fraction(3, 5)):
        *_, direct = quadratic_data(theta)
        closed = Fraction(1, 1) - Fraction(1, 1) / (Fraction(1, 1) + theta) ** 3
        assert direct == closed


def factorization(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def mobius(n: int) -> int:
    if n == 1:
        return 1
    fac = factorization(n)
    if any(e > 1 for e in fac.values()):
        return 0
    return -1 if len(fac) % 2 else 1


def divisors(n: int) -> list[int]:
    result = [1]
    for p, e in factorization(n).items():
        result = [d * (p**k) for d in result for k in range(e + 1)]
    return result


def von_mangoldt_log_basis(n: int) -> dict[int, int]:
    """Represent Lambda(n) in the formal basis {log p}; return {p:1} for p^k."""
    if n <= 1:
        return {}
    fac = factorization(n)
    if len(fac) != 1:
        return {}
    p = next(iter(fac))
    return {p: 1}


def mu_convolve_lambda_basis(n: int) -> dict[int, int]:
    coeff: dict[int, int] = {}
    for d in divisors(n):
        for p, c in von_mangoldt_log_basis(d).items():
            coeff[p] = coeff.get(p, 0) + mobius(n // d) * c
    return {p: c for p, c in coeff.items() if c}


def exact_redundancy_check(limit: int = 300) -> None:
    """Verify (mu*Lambda)(n)=-mu(n) log n in a formal prime-log basis."""
    for n in range(1, limit + 1):
        lhs = mu_convolve_lambda_basis(n)
        mu = mobius(n)
        rhs = {p: -mu * e for p, e in factorization(n).items() if mu and e}
        assert lhs == rhs, (n, lhs, rhs)


def print_target_table() -> None:
    targets = [19 / 27, 0.71, 0.72, 0.73, 0.75, 0.80]
    print("formal one-piece target table")
    print(
        "target        theta_required   base_delta_needed   "
        "large_mod_T_exp   large_mod_saving"
    )
    for target in targets:
        theta = theta_for_target(target)
        # Barrier A: y*T^(1/2-delta)=o(T) needs delta > theta-1/2.
        base_delta = max(0.0, theta - 0.5)
        # Barrier B: y^(1/3)*T^beta=o(T) needs beta < 1-theta/3.
        beta = 1.0 - theta / 3.0
        saving = 5.0 / 6.0 - beta
        print(
            f"{100*target:8.4f}%   {theta:14.10f}   {base_delta:17.10f}   "
            f"{beta:15.10f}   {saving:16.10f}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="run assertions with compact output")
    args = parser.parse_args()

    exact_variational_checks()
    exact_redundancy_check()

    if args.check:
        print("discrete-mollifier exact checks: PASS")
        return

    I, J, A, D, K = quadratic_data(Fraction(1, 2))
    print(f"theta=1/2: I={I}, J={J}, A={A}, D={D}, K={K}={float(K):.12f}")
    print("(mu*Lambda)(n)=-mu(n)log(n): exact formal-basis check PASS for n<=300")
    print_target_table()


if __name__ == "__main__":
    main()
