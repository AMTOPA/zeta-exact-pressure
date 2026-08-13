#!/usr/bin/env python3
"""Exact/formal checks for the Bui--Heath-Brown one-piece mollifier model.

This script does not prove an extension beyond theta < 1/2.  It only evaluates the
published main-term functional and quantifies the exponent improvement needed to
support longer mollifiers.
"""

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


def exact_half_check() -> None:
    theta = Fraction(1, 2)
    value = Fraction(1, 1) - Fraction(1, 1) / (Fraction(1, 1) + theta) ** 3
    expected = Fraction(19, 27)
    assert value == expected
    print(f"theta=1/2 => kappa={value} = {float(value):.12f}")


def quadratic_data(theta: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Return I, J and kappa for P(x)=-theta*x^2+(1+theta)*x."""
    # For P_a(x)=a x^2+(1-a)x with a=-theta:
    # I=(3-a)/6=(3+theta)/6 and J=(a^2+3)/3.
    I = (Fraction(3, 1) + theta) / 6
    J = (theta * theta + 3) / 3
    A = Fraction(1, 2) + theta * I
    D = Fraction(1, 3) + theta * I + theta * theta * I * I + J / (12 * theta)
    K = A * A / D
    return I, J, K


def print_target_table() -> None:
    targets = [19 / 27, 0.71, 0.72, 0.73, 0.75, 0.80]
    print("\nformal target table")
    print("target        theta_required   b_required_if_a=1/3   a_required_if_b=5/6")
    for target in targets:
        theta = theta_for_target(target)
        # If an error has shape y^a T^b, lower order requires a*theta+b<1.
        b_required = 1.0 - theta / 3.0
        a_required = (1.0 - 5.0 / 6.0) / theta
        print(
            f"{100*target:8.4f}%   {theta:14.10f}   "
            f"{b_required:19.10f}   {a_required:19.10f}"
        )


def main() -> None:
    exact_half_check()
    I, J, K = quadratic_data(Fraction(1, 2))
    assert K == Fraction(19, 27)
    print(f"P_theta at theta=1/2: I={I}, J={J}, K={K}")
    print_target_table()


if __name__ == "__main__":
    main()
