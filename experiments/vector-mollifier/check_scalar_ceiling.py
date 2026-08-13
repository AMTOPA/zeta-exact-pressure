#!/usr/bin/env python3
from fractions import Fraction as F


def main() -> None:
    # Formal endpoint theta = 1/2, approached from below in the theorem.
    theta = F(1, 2)

    # Optimal quadratic P(x) = -theta*x^2 + (1+theta)*x.
    # Its integral and Dirichlet energy are exact.
    I = F(1, 2) + theta / 6
    K = 1 + theta * theta / 3

    U = F(1, 2) + theta * I
    Q = F(1, 3) + theta * I + theta * theta * I * I + K / (12 * theta)
    ratio = U * U / Q

    assert I == F(7, 12)
    assert K == F(13, 12)
    assert U == F(19, 24)
    assert Q == F(57, 64)
    assert ratio == F(19, 27)

    # Fixed-I energy minimizer:
    # P_I(x)=(3-6I)x^2+(6I-2)x has
    # integral(P_I'^2)=4(3I^2-3I+1).
    def k_min(i: F) -> F:
        return 4 * (3 * i * i - 3 * i + 1)

    assert k_min(I) == K

    # Closed-form optimum over I for general theta:
    # R_*(theta)=theta(theta^2+3theta+3)/(1+theta)^3.
    r_closed = theta * (theta * theta + 3 * theta + 3) / (1 + theta) ** 3
    assert r_closed == ratio

    # The derivative is exactly 3/(1+theta)^4 > 0,
    # so theta -> 1/2^- is the best point in the RH-only range.
    derivative = F(3, 1) / (1 + theta) ** 4
    assert derivative > 0

    print(f"theta={theta}")
    print(f"I={I}")
    print(f"K={K}")
    print(f"U={U}")
    print(f"Q={Q}")
    print(f"ratio={ratio}={float(ratio):.15f}")
    print(f"dR/dtheta at theta=1/2: {derivative} > 0")
    print("SCALAR_CEILING_CHECK=true")


if __name__ == "__main__":
    main()
