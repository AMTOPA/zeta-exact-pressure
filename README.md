# Zeta exact-pressure optimization

> [!IMPORTANT]
> **Current status: discovery candidate, not yet a certified lower bound.**
>
> The latest 11-term window search projects
>
> $$
> \frac{N_0^s(T,2T)}{N(T,2T)}\approx 0.673330866624887\ldots,
> $$
>
> i.e. **67.3330866625%**, using floating-point adversarial search. A deliberately conservative certification target, if proved, projects **67.3330085275%**. The required interval certificate for the new local target has **not** yet been completed.

The previous interval-certified research-draft record, **67.3290756019%**, is preserved under [`archive/2026-08-12-certified-6732907560/`](archive/2026-08-12-certified-6732907560/).

This is a research project, not a peer-reviewed theorem and not a proof of the Riemann hypothesis. All statements inherit the same imported analytic interface described in the earlier manuscript and lineage repositories.

## Current discovery candidate

The local method still uses seven consecutive simple zeros, six gaps, the same exact position-pressure vector, and exact shifted-pressure averaging. The new lever is a larger window basis optimized against an adversarial lattice search rather than optimizing the window functional $H$ alone.

The 11-term window is

$$
v(s)=\sum_{j=0}^{10}c_j\cos(\omega_j s),
$$

with

$$
\omega_0=\sqrt2,\qquad \omega_j=2j\pi\quad(1\le j\le10),
$$

and rational coefficients with denominator $10^9$:

```text
1000000000
   8421762
  -9816829
   1448046
   1412305
  -2228329
   2374999
  -4885560
   8393483
  -3137216
   2381462
```

High-precision evaluation gives

$$
H(v)=0.6723307581635602536\ldots
$$

and the arithmetic projection uses the lower working value

$$
H_{\rm floor}=0.6723307.
$$

The pressure coefficients remain

$$
\frac1{2300000000}(831522,1096590,1071888,1071888,1096590,831522),
\qquad B=\frac3{1150}.
$$

## Adversarial local search

Naive multistart searches can miss low lattice-like configurations. The current discovery search therefore used pressure-feasible integer-lattice starts with reflection reduction and local polishing. Across 2,823 adversarial starts, the current observed floating-point minimum is

$$
\varepsilon_{\rm float}\approx0.00540611079920.
$$

The next certification target is intentionally lower:

$$
\varepsilon_{\rm target}=0.005405.
$$

**This target is not yet interval-certified.** It must not be cited as a proved inequality until the branch-and-bound verifier closes all boxes.

## Global projection

For an $m$-point block, retain

$$
A_m=\varepsilon(m-6),\qquad R_m=h_m(A_m),\qquad \eta_m=R_m/A_m,
$$

with

$$
h_m(E)=
\begin{cases}
E,&0\le E\le m/(m-1),\\[1mm]
E/m+2\sqrt{(m-1)E/m}-1,&E\ge m/(m-1).
\end{cases}
$$

and the exact shifted-pressure deduction

$$
\frac{N_0^s(T,2T)}{N(T,2T)}\ge
\frac{mH-\eta_mB(m-6)}{m-R_m}-o(1).
$$

Using the conservative discovery inputs

$$
H=0.6723307,\qquad \varepsilon=0.005405,
$$

an integer scan selects

$$
m=204
$$

and gives the arithmetic projection

$$
0.6733300852750384514\ldots=67.3330085275\ldots\%.
$$

The rational decimal floor

$$
0.6733300852
$$

is therefore an arithmetic floor **conditional on certifying the new local target**, not a currently established mathematical bound.

Using the floating-point discovery values instead gives approximately **67.3330866625%**.

## Reproduction and checks

Run

```bash
sh run.sh
```

for structural consistency, high-precision window evaluation, interval positivity subdivision, exact pressure multiplicity, and final projection arithmetic.

The current self-check deliberately does **not** claim that the new local certificate is verified. See [`candidate.json`](candidate.json) and [`certificates/latest-verification.txt`](certificates/latest-verification.txt) for machine-readable/current status.

## Archive and manuscript

- [`archive/2026-08-12-certified-6732907560/`](archive/2026-08-12-certified-6732907560/) freezes the previous 67.3290756019% record and its certificate statistics.
- [`paper/main.tex`](paper/main.tex) and [`paper/main.pdf`](paper/main.pdf) correspond to the previous certified-baseline manuscript until the 11-term candidate receives a rigorous local certificate and is promoted into the manuscript.

## Trust boundary

Currently checked directly in this repository:

- exact position-pressure total and shifted multiplicity identity;
- high-precision evaluation of the 11-term $H(v)$;
- interval subdivision positivity of the 11-term window;
- arithmetic scan of the conditional final projection.

Not yet checked for the new candidate:

- a rigorous interval proof of $F(g_1,\ldots,g_6)\ge0.005405$ for all $g_i\ge0$;
- independent reproduction of that new certificate.

Imported analytic inputs remain the explicit-formula / trace interface, finite-$m$ Gram spectral profile, normalized-gap bookkeeping, and the analytic link from $H(v)$ to the zero count.

## License and attribution

Original material in this repository is released under the MIT License. Third-party verifiers and analytic inputs are referenced rather than vendored; see [`THIRD_PARTY.md`](THIRD_PARTY.md).
