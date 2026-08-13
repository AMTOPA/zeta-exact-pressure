#!/usr/bin/env python3
"""Exponent bookkeeping for a theta>1/2 extension of Bui--Heath-Brown.

This is a formal analysis of their Section 3 bound.  It does not prove a new
estimate.  It records the effect of replacing the fixed long-factor threshold
R=y*T^(1/2) by a dyadic threshold R optimized in Q,K,D.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isclose


@dataclass(frozen=True)
class Block:
    theta: float   # y=T^theta
    alpha: float   # Q=T^alpha
    kappa: float   # K=T^kappa
    delta: float   # D=T^delta

    @property
    def gap(self) -> float:
        return self.kappa - self.delta

    @property
    def x_exp(self) -> float:
        """Exponent x in X=KQT/D=T^x (constants ignored)."""
        return 1.0 + self.alpha + self.gap

    @property
    def q3_exp(self) -> float:
        return 3.0 * self.alpha

    def validate(self) -> None:
        assert self.delta <= self.kappa + 1e-12
        assert self.kappa + self.alpha <= self.theta + 1e-12


def published_exponents(b: Block) -> dict[str, float]:
    """Power exponents before the final D<=K and Q<=y relaxations."""
    g = b.gap
    return {
        # Pólya--Vinogradov long-factor disposal with R=y*T^(1/2)
        "long_fixed": 2.0 * b.alpha - b.theta + 0.5,
        # Q*T^(1/2) branch, retaining sqrt(D/K)
        "two_block_A": b.alpha + 0.5 - g / 2.0,
        # y^(1/2)*T^(3/4) branch, retaining sqrt(D/K)
        "two_block_B": b.theta / 2.0 + 0.75 - g / 2.0,
        # (KQT/D)^(2/3) balancing branch
        "two_block_C": 5.0 / 6.0 + b.alpha / 3.0 - g / 6.0,
    }


def optimal_threshold_exp(b: Block) -> float:
    """rho for R_opt=T^rho balancing Q^2*T/R and sqrt(D/K)T^(1/2)R^(1/2)."""
    return 4.0 * b.alpha / 3.0 + 1.0 / 3.0 + b.gap / 3.0


def optimized_exponents(b: Block) -> dict[str, float]:
    rho = optimal_threshold_exp(b)
    g = b.gap
    long_or_R = 2.0 * b.alpha + 1.0 - rho
    same_from_factorization = 0.5 - g / 2.0 + rho / 2.0
    assert isclose(long_or_R, same_from_factorization, rel_tol=0.0, abs_tol=1e-12)
    return {
        "R_exp": rho,
        "long_and_R_branch": long_or_R,
        "two_thirds_branch": 5.0 / 6.0 + b.alpha / 3.0 - g / 6.0,
    }


def is_critical(b: Block, tol: float = 1e-12) -> bool:
    """Region not power-saved by the optimized old argument."""
    return b.alpha >= 0.5 - tol and b.gap <= 2.0 * b.alpha - 1.0 + tol


def conductor_admissible(b: Block, tol: float = 1e-12) -> bool:
    """X<=Q^3 in exponent notation."""
    return b.x_exp <= b.q3_exp + tol


def check_equivalence() -> None:
    # On alpha>=1/2, gap<=2alpha-1 iff 1+alpha+gap<=3alpha.
    for alpha in (0.5, 0.502, 0.505, 0.5107780534895243):
        for gap in (0.0, 0.002, 0.01, 0.02, 0.03):
            theta = 0.5107780534895243
            if alpha > theta or gap > theta - alpha:
                continue
            b = Block(theta=theta, alpha=alpha, kappa=gap, delta=0.0)
            b.validate()
            assert is_critical(b) == conductor_admissible(b)


def main() -> None:
    check_equivalence()
    theta = 0.5107780534895243  # formal 71% length
    print(f"theta_71 = {theta:.12f}")
    print(f"top-modulus width theta-1/2 = {theta-0.5:.12f}")
    print(f"max critical gap 2theta-1 = {2*theta-1:.12f}")
    print()
    print("At alpha=theta and gap=0 (Q~y, K~D~1):")
    b = Block(theta=theta, alpha=theta, kappa=0.0, delta=0.0)
    for key, value in optimized_exponents(b).items():
        print(f"  {key:24s} {value:.12f}")
    print(f"  X exponent               {b.x_exp:.12f}")
    print(f"  Q^3 exponent             {b.q3_exp:.12f}")
    print(f"  conductor admissible     {conductor_admissible(b)}")
    print()
    print("Interpretation: after optimizing R, the unresolved alpha>=1/2 region")
    print("is exactly X<=Q^3; X>Q^3 is already power-saved by the old method.")


if __name__ == "__main__":
    main()
