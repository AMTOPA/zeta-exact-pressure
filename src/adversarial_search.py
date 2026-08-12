#!/usr/bin/env python3
"""Unscreened floating-point adversarial search for the six-gap local functional.

This is a discovery tool, not a certificate.  Every resonance template in
{1,...,R}^6 is locally polished; templates are never discarded because their
unpolished score looks too high.  This policy was adopted after interval
verification exposed a deep basin reachable from (1,1,1,3,1,1) that the old
top-k integer-score screening had missed.
"""
from __future__ import annotations

import argparse
import itertools

import numpy as np
from scipy.optimize import differential_evolution, minimize

from candidate_data import load_candidate


def sinc(z):
    z = np.asarray(z, dtype=float)
    out = np.ones_like(z)
    mask = np.abs(z) > 1e-7
    q = z[mask]
    out[mask] = np.sin(q) / q
    q = z[~mask]
    out[~mask] = 1 - q**2 / 6 + q**4 / 120 - q**6 / 5040
    return out


def sinc_prime(z):
    z = np.asarray(z, dtype=float)
    out = np.empty_like(z)
    mask = np.abs(z) > 1e-5
    q = z[mask]
    out[mask] = (q * np.cos(q) - np.sin(q)) / q**2
    q = z[~mask]
    out[~mask] = -q / 3 + q**3 / 30 - q**5 / 840 + q**7 / 45360
    return out


class LocalFunctional:
    def __init__(self, candidate: dict):
        window = candidate["window"]
        den = float(window["denominator"])
        self.coeff = np.asarray(window["numerators"], dtype=float) / den
        self.omega = np.asarray(
            [np.sqrt(2.0)] + [2 * j * np.pi for j in range(1, len(self.coeff))],
            dtype=float,
        )

        pair = candidate["pair_weights"]
        pden = float(pair["denominator"])
        entries = [(int(i), int(j), float(n) / pden) for i, j, n in pair["entries"]]
        self.pair_i = np.asarray([x[0] for x in entries], dtype=int)
        self.pair_j = np.asarray([x[1] for x in entries], dtype=int)
        self.pair_a = np.asarray([x[2] for x in entries], dtype=float)

        pressure = candidate["position_pressure"]
        self.pressure = np.asarray(pressure["numerators"], dtype=float) / float(
            pressure["denominator"]
        )
        self.k0 = float(self.kernel(np.asarray([0.0]))[0])

    def basis(self, x):
        x = np.asarray(x, dtype=float).reshape(-1, 1)
        omega = self.omega.reshape(1, -1)
        left = omega / 2 - np.pi * x
        right = omega / 2 + np.pi * x
        value = (sinc(left) + sinc(right)) / 2
        first = np.pi * (sinc_prime(right) - sinc_prime(left)) / 2
        return value, first

    def kernel(self, x):
        value, _ = self.basis(x)
        return value @ self.coeff

    def value_grad(self, gaps):
        g = np.asarray(gaps, dtype=float)
        prefix = np.r_[0.0, np.cumsum(g)]
        distance = prefix[self.pair_j] - prefix[self.pair_i]
        basis, basis_prime = self.basis(distance)
        k = basis @ self.coeff
        kp = basis_prime @ self.coeff
        weight = (k / self.k0) ** 2
        weight_prime = 2 * k * kp / self.k0**2

        value = float(g @ self.pressure + self.pair_a @ weight)
        grad = self.pressure.copy()
        for i, j, a, slope in zip(
            self.pair_i, self.pair_j, self.pair_a, weight_prime
        ):
            grad[i:j] += a * slope
        return value, grad


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--template-max",
        type=int,
        default=4,
        help="polish every template in {1,...,R}^6; default gives 4^6=4096 starts",
    )
    parser.add_argument("--upper-bound", type=float, default=10.0)
    parser.add_argument("--de-runs", type=int, default=9)
    args = parser.parse_args()

    if args.template_max < 1:
        raise SystemExit("--template-max must be positive")

    candidate = load_candidate()
    f = LocalFunctional(candidate)
    templates = itertools.product(
        range(1, args.template_max + 1), repeat=int(candidate["gaps_per_local_window"])
    )

    minima: list[tuple[float, np.ndarray, str]] = []
    count = 0
    for start_tuple in templates:
        count += 1
        start = np.asarray(start_tuple, dtype=float)
        result = minimize(
            f.value_grad,
            start,
            method="L-BFGS-B",
            jac=True,
            bounds=[(0.0, args.upper_bound)] * len(start),
            options={"ftol": 1e-13, "gtol": 1e-9, "maxiter": 500},
        )
        minima.append((float(result.fun), result.x.copy(), f"template={start_tuple}"))

    for seed in range(args.de_runs):
        upper = (6.0, 10.0, 16.0)[seed % 3]
        result = differential_evolution(
            lambda x: f.value_grad(x)[0],
            [(0.0, upper)] * int(candidate["gaps_per_local_window"]),
            seed=2000 + seed,
            popsize=10,
            maxiter=220,
            polish=True,
            tol=1e-9,
        )
        minima.append((float(result.fun), result.x.copy(), f"de_upper={upper:g},seed={seed}"))

    minima.sort(key=lambda item: item[0])
    print(f"template_screening=false")
    print(f"template_starts={count}")
    print(f"differential_evolution_runs={args.de_runs}")
    for rank, (value, gaps, source) in enumerate(minima[:20], 1):
        coords = ", ".join(f"{x:.12g}" for x in gaps)
        print(f"rank={rank} F={value:.17g} gaps=[{coords}] {source}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
