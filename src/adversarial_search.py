#!/usr/bin/env python3
"""Floating-point adversarial search for the six-gap local functional.

This is a discovery tool, not a certificate. It scores the complete integer
lattice {0,...,R}^6, selects the lowest starts, and polishes them with an
analytic gradient. Exact coefficients are loaded from candidate.json.
"""
from __future__ import annotations

import argparse

import numpy as np
from scipy.optimize import differential_evolution, minimize

from candidate_data import load_candidate


def sinc(z):
    z = np.asarray(z, dtype=float)
    small = np.abs(z) < 1e-5
    z2 = z * z
    series = 1 - z2 / 6 + z2 * z2 / 120 - z2 * z2 * z2 / 5040
    return np.where(small, series, np.sin(z) / z)


def sinc_prime(z):
    z = np.asarray(z, dtype=float)
    small = np.abs(z) < 1e-4
    z2 = z * z
    series = -z / 3 + z * z2 / 30 - z * z2 * z2 / 840 + z * z2 * z2 * z2 / 45360
    return np.where(small, series, (z * np.cos(z) - np.sin(z)) / z2)


class LocalFunctional:
    def __init__(self, candidate: dict):
        window = candidate["window"]
        den = float(window["denominator"])
        self.coeff = np.array(window["numerators"], dtype=float) / den
        self.omega = np.array(
            [np.sqrt(2.0)] + [2 * j * np.pi for j in range(1, len(self.coeff))],
            dtype=float,
        )

        pair = candidate["pair_weights"]
        pden = float(pair["denominator"])
        self.pairs = [(int(i), int(j), float(n) / pden) for i, j, n in pair["entries"]]
        pressure = candidate["position_pressure"]
        self.pressure = np.array(pressure["numerators"], dtype=float) / float(pressure["denominator"])
        self.k0 = float(self.kernel(np.array([0.0]))[0])

    def kernel(self, x):
        x = np.asarray(x, dtype=float)
        out = np.zeros_like(x)
        for c, w in zip(self.coeff, self.omega):
            out += c * (sinc(w / 2 - np.pi * x) + sinc(w / 2 + np.pi * x)) / 2
        return out

    def kernel_prime(self, x):
        x = np.asarray(x, dtype=float)
        out = np.zeros_like(x)
        for c, w in zip(self.coeff, self.omega):
            left = w / 2 - np.pi * x
            right = w / 2 + np.pi * x
            out += c * np.pi * (sinc_prime(right) - sinc_prime(left)) / 2
        return out

    def weight(self, x):
        k = self.kernel(x)
        return (k / self.k0) ** 2

    def weight_prime(self, x):
        k = self.kernel(x)
        kp = self.kernel_prime(x)
        return 2 * k * kp / (self.k0 * self.k0)

    def many(self, gaps):
        gaps = np.asarray(gaps, dtype=float)
        prefix = np.concatenate([np.zeros((len(gaps), 1)), np.cumsum(gaps, axis=1)], axis=1)
        out = gaps @ self.pressure
        for i, j, a in self.pairs:
            out += a * self.weight(prefix[:, j] - prefix[:, i])
        return out

    def value_grad(self, gaps):
        g = np.asarray(gaps, dtype=float)
        prefix = np.r_[0.0, np.cumsum(g)]
        value = float(g @ self.pressure)
        grad = self.pressure.copy()
        for i, j, a in self.pairs:
            d = np.array([prefix[j] - prefix[i]])
            value += a * float(self.weight(d)[0])
            slope = a * float(self.weight_prime(d)[0])
            grad[i:j] += slope
        return value, grad


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--radius", type=int, default=8)
    parser.add_argument("--polish", type=int, default=220)
    parser.add_argument("--de-runs", type=int, default=0)
    args = parser.parse_args()

    candidate = load_candidate()
    f = LocalFunctional(candidate)
    shape = (args.radius + 1,) * 6
    lattice = np.indices(shape, dtype=np.int16).reshape(6, -1).T.astype(float)
    scores = f.many(lattice)
    keep = min(args.polish, len(scores))
    chosen = np.argpartition(scores, keep - 1)[:keep]
    chosen = chosen[np.argsort(scores[chosen])]

    minima: list[tuple[float, np.ndarray]] = []
    for idx in chosen:
        start = lattice[idx]
        result = minimize(
            lambda x: f.value_grad(x),
            start,
            method="L-BFGS-B",
            jac=True,
            bounds=[(0.0, None)] * 6,
            options={"ftol": 1e-15, "gtol": 1e-11, "maxiter": 1000},
        )
        minima.append((float(result.fun), result.x.copy()))

    for seed in range(args.de_runs):
        upper = (6.0, 10.0, 16.0)[seed % 3]
        result = differential_evolution(
            lambda x: f.value_grad(x)[0],
            [(0.0, upper)] * 6,
            seed=1000 + seed,
            popsize=12,
            maxiter=300,
            polish=True,
            tol=1e-10,
        )
        minima.append((float(result.fun), result.x.copy()))

    minima.sort(key=lambda item: item[0])
    print(f"lattice_points={len(lattice)}")
    print(f"lattice_best={scores.min():.17g}")
    print(f"polished_starts={keep}")
    if args.de_runs:
        print(f"differential_evolution_runs={args.de_runs}")
    for rank, (value, gaps) in enumerate(minima[:10], 1):
        coords = ", ".join(f"{x:.12g}" for x in gaps)
        print(f"rank={rank} F={value:.17g} gaps=[{coords}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
