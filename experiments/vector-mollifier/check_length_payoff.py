#!/usr/bin/env python3
from fractions import Fraction as F


def r(theta: F) -> F:
    return theta * (theta * theta + 3 * theta + 3) / (1 + theta) ** 3


def required_savings(theta: F):
    excess = theta - F(1, 2)
    return excess, excess / 2


def main() -> None:
    targets = [F(1, 2), F(51, 101), F(17, 33), F(6, 11), F(4, 7)]
    for theta in targets:
        value = r(theta)
        print(
            f"theta={theta}={float(theta):.12f} "
            f"R={value}={100*float(value):.10f}%"
        )
        if theta > F(1, 2):
            d1, d2 = required_savings(theta)
            print(f"  required delta1>{d1}, delta2>{d2}")

    assert r(F(1, 2)) == F(19, 27)
    assert required_savings(F(51, 101)) == (F(1, 202), F(1, 404))
    assert required_savings(F(17, 33)) == (F(1, 66), F(1, 132))
    assert required_savings(F(6, 11)) == (F(1, 22), F(1, 44))
    assert required_savings(F(4, 7)) == (F(1, 14), F(1, 28))
    print("LENGTH_PAYOFF_CHECK=true")


if __name__ == "__main__":
    main()
