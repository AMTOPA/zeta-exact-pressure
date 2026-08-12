# Zeta exact-pressure optimization

> [!IMPORTANT]
> **Current research-draft candidate: 67.3330598288%.**
>
> The new seven-point local target
> \(\varepsilon=0.005401\) is closed by the repository-native outward-rounded interval verifier. The window contribution also has an interval-verified floor \(H>0.6723338\). The inherited analytic interface is still imported from the lineage repositories, and independent reproduction of the new local certificate is requested before publication-quality use.

This is a research project, not a peer-reviewed theorem and not a proof of the Riemann hypothesis.

## Current 15-term window

The local method uses seven consecutive simple zeros, six gaps, the established pair weights, the exact position-pressure vector, and exact shifted-pressure averaging. The window is

$$
v(s)=\sum_{j=0}^{14}c_j\cos(\omega_js),\qquad
\omega_0=\sqrt2,\quad \omega_j=2j\pi\ (1\le j\le14),
$$

with common denominator $10^9$ and numerators

```text
1000000000
   8629738
 -10085378
   1746803
   1125700
  -2203905
   1904615
  -4559603
   7930665
  -3022627
   2165339
    398121
   -255934
    188899
   -148305
```

High-precision evaluation gives

$$
H(v)=0.672333886657942\ldots,
$$

and `src/check_window.py` verifies by interval arithmetic that

$$
H(v)>0.6723338.
$$

The position-pressure coefficients remain

$$
\frac1{2300000000}(831522,1096590,1071888,1071888,1096590,831522),
\qquad B=\frac3{1150}.
$$

## Why this candidate replaced the earlier 15-term search

An earlier score-screened search proposed `epsilon = 0.005561`. The interval verifier exposed a missed low basin, and unrestricted local optimization then found still deeper basins. That target was rejected rather than weakened cosmetically.

The counterexamples were fed back into a min-max exchange optimization. The retained window was stress-tested by polishing every template in `{1,2,3,4}^6` without score screening, an additional `{1,2,3,5}^6` family, and multi-range differential evolution. The lowest floating-point basin observed for the rounded rational window was

$$
0.005402429240910082\ldots.
$$

The rigorous target was set below it at

$$
\boxed{\varepsilon=0.005401}.
$$

## Interval certificate

The full run used a 4000 grid and 50 decimal digits for `mpmath.iv` table construction, followed by C++ branch-and-bound with interval Hessian LDL and convex tangent pruning:

```text
VERIFIED=true
nodes=3171002
pruned=1585573
splits=1585429
convex=1776812
tangent=751200
max_depth=62
```

The exact table hashes, workflow run, artifact ID, and full certificate metadata are recorded in [`candidate.json`](candidate.json) and [`certificates/latest-verification.txt`](certificates/latest-verification.txt).

Independent reproduction is still `false`.

## Exact-pressure projection

For an $m$-point block define

$$
A_m=\varepsilon(m-6),\qquad R_m=h_m(A_m),\qquad \eta_m=R_m/A_m,
$$

where

$$
h_m(E)=
\begin{cases}
E,&E\le m/(m-1),\\
E/m+2\sqrt{(m-1)E/m}-1,&E\ge m/(m-1).
\end{cases}
$$

The exact shifted-pressure deduction gives

$$
\frac{N_0^s(T,2T)}{N(T,2T)}\ge
\frac{mH-\eta_mB(m-6)}{m-R_m}-o(1).
$$

Using the certified working inputs

$$
H=0.6723338,\qquad \varepsilon=0.005401,\qquad B=3/1150,
$$

the integer scan selects $m=204$ and yields

$$
0.6733305982879586830\ldots,
$$

hence the safe research-draft decimal floor

$$
\boxed{0.6733305982},
$$

i.e. **67.3330598288%** before the harmless decimal truncation.

The previous interval-certified record, **67.3290756019%**, is frozen under [`archive/2026-08-12-certified-6732907560/`](archive/2026-08-12-certified-6732907560/).

## Reproduction

Run

```bash
sh run.sh
```

for structural checks, interval $H$ verification, window positivity, exact pressure multiplicity, final arithmetic, and verifier compilation/smoke testing. The full local certificate workflow is in `.github/workflows/local-certificate-pilot.yml`.

## Trust boundary

Checked directly in this repository:

- exact pair-span capacities and position-pressure total;
- interval lower bound for the 15-term $H(v)$ and window positivity;
- the global six-gap inequality $F(g_1,\ldots,g_6)\ge0.005401$ by outward-rounded interval branch-and-bound;
- exact shifted-pressure multiplicity bookkeeping and final high-precision arithmetic.

Still imported: the explicit-formula / trace interface, finite-$m$ Gram spectral profile, normalized-gap bookkeeping, and the analytic link from $H(v)$ to the zero count.

Original repository material is MIT-licensed. Third-party analytic inputs are referenced rather than vendored; see [`THIRD_PARTY.md`](THIRD_PARTY.md).
