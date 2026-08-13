#!/usr/bin/env python3
"""Finite checks of the squarefree primitive Gauss identity.

This is a checker for an exact algebraic identity, not a numerical asymptotic.
It enumerates primitive characters for small odd squarefree moduli by CRT from
nonprincipal characters modulo the prime factors.
"""

import cmath
import math


def factor_squarefree_odd(q):
    primes = []
    n = q
    p = 3
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                raise ValueError("q is not squarefree")
            primes.append(p)
        p += 2
    if n > 1:
        primes.append(n)
    if 2 in primes or math.prod(primes) != q:
        raise ValueError("q must be odd squarefree")
    return primes


def primitive_root_prime(p):
    phi = p - 1
    factors = []
    n = phi
    r = 2
    while r * r <= n:
        if n % r == 0:
            factors.append(r)
            while n % r == 0:
                n //= r
        r += 1
    if n > 1:
        factors.append(n)
    for g in range(2, p):
        if all(pow(g, phi // ell, p) != 1 for ell in factors):
            return g
    raise RuntimeError("no primitive root found")


def local_log_table(p):
    g = primitive_root_prime(p)
    out = {}
    x = 1
    for exponent in range(p - 1):
        out[x] = exponent
        x = (x * g) % p
    return out


def local_character(p, log_table, index, a):
    a %= p
    if a == 0:
        return 0j
    exponent = log_table[a]
    return cmath.exp(2j * math.pi * index * exponent / (p - 1))


def character_tuples(primes):
    tuples = [()]
    for p in primes:
        tuples = [prefix + (j,) for prefix in tuples for j in range(1, p - 1)]
    return tuples


def primitive_gauss_sum_side(q, r):
    primes = factor_squarefree_odd(q)
    logs = {p: local_log_table(p) for p in primes}
    total = 0j
    for indices in character_tuples(primes):
        def chi(a):
            z = 1 + 0j
            for p, j in zip(primes, indices):
                z *= local_character(p, logs[p], j, a)
            return z

        tau_bar = sum(
            chi(a).conjugate() * cmath.exp(2j * math.pi * a / q)
            for a in range(1, q + 1)
        )
        total += tau_bar * chi(r)
    return total


def divisors(n):
    out = []
    for d in range(1, n + 1):
        if n % d == 0:
            out.append(d)
    return out


def phi(n):
    return sum(1 for a in range(1, n + 1) if math.gcd(a, n) == 1)


def divisor_phase_side(q, r):
    total = 0j
    for c in divisors(q):
        if c == 1:
            phase = 1 + 0j
        else:
            h = q // c
            h_inv = pow(h, -1, c)
            phase = cmath.exp(2j * math.pi * ((r * h_inv) % c) / c)
        total += phi(c) * phase
    return total


def main():
    tested = 0
    for q in (3, 5, 7, 15, 21, 35):
        for r in range(1, q):
            if math.gcd(r, q) != 1:
                continue
            left = primitive_gauss_sum_side(q, r)
            right = divisor_phase_side(q, r)
            error = abs(left - right)
            assert error < 1e-9, (q, r, left, right, error)
            tested += 1
    print(f"tested_pairs={tested}")
    print("GAUSS_TRANSFORM_CHECK=true")


if __name__ == "__main__":
    main()
