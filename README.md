# Zeta exact-pressure optimization

> [!IMPORTANT]
> **Current interval-certified research-draft record: 67.3413085287%.**
>
> The current construction jointly optimizes the total local pressure, the rational 15-term window, pair weights, and position-pressure distribution. The six-gap target `epsilon = 0.007887` is closed by the hardened outward-rounded interval verifier. A same-parameter upward epsilon tightening is now the active experiment.

This is a research project, not a peer-reviewed theorem and not a proof of the Riemann hypothesis.

## Current joint-pressure certified record

The local construction returns to seven points / six gaps, but releases a parameter held fixed in earlier positioned-pressure searches: the total local pressure

\[
B=\sum_{r=1}^{6}b_r.
\]

The predecessor block argument uses this quantity symbolically through

\[
E_B+B\,\operatorname{span}(B)\ge A,
\]

and carries the same \(B\) into the global pressure penalty. Thus \(B\) may itself be optimized provided the position pressures remain nonnegative, the exact new total is used globally, and every pair-span capacity remains at most 2.

### Analytic window

We use

\[
v(s)=\sum_{j=0}^{14}c_j\cos(\omega_js),\qquad
\omega_0=\sqrt2,\quad \omega_j=2j\pi\ (1\le j\le14),
\]

with denominator \(10^9\) and numerator vector

```text
1000000000
  12948011
 -12114181
   3684033
   5911261
  -1663892
   5928575
  -7167828
   6229914
  -5147758
   -756341
    440544
   -311207
    237969
   -190433
```

Direct interval arithmetic gives

\[
H(v)=0.6721999026675757754212693844824\ldots
\]

and verifies the tighter conservative floor

\[
\boxed{H(v)>0.6721999026}.
\]

The same 4096-cell interval subdivision gives a window lower bound above `0.7616106600`.

### Exact local weights and pressure

The exact position-pressure vector is

\[
\frac1{46000000000}
(22420713,32878293,37700994,37700994,32878293,22420713),
\]

with

\[
\boxed{B=\frac{93}{23000}=0.004043478260869565\ldots}.
\]

For every span \(s=1,\ldots,6\), the exact pair weights in [`candidate.json`](candidate.json) sum to exactly 2. All pair and pressure coefficients are nonnegative.

### Certified local inequality

Adversarial exchange over \(B\), the window, pair weights, and pressure distribution produced an observed floating minimum near

\[
0.0078878193504693\ldots.
\]

The hardened six-dimensional interval verifier proves

\[
\boxed{F(g_1,\ldots,g_6)\ge0.007887}\qquad(g_i\ge0).
\]

The successful 4000-grid / 50-digit run, compiled with `-ffp-contract=off`, reports

```text
VERIFIED=true
nodes=3424276
pruned=1712170
splits=1712106
convex=1756299
tangent=801918
max_depth=71
```

It begins from 64 boxes with component counts `2,2,2,2,2,2`. Exact table hashes, workflow run `31603343875`, artifact `9144421792`, and artifact digest are recorded in [`candidate.json`](candidate.json) and [`certificates/latest-verification.txt`](certificates/latest-verification.txt).

## Exact-pressure projection

For an \(m\)-point block,

\[
A_m=\varepsilon(m-6),\qquad
R_m=h_m(A_m),\qquad
\eta_m=R_m/A_m,
\]

and exact shifted-pressure bookkeeping gives

\[
\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\frac{mH-\eta_mB(m-6)}{m-R_m}-o(1).
\]

Using only certified conservative inputs

\[
H=0.6721999026,\qquad
\varepsilon=0.007887,\qquad
B=\frac{93}{23000},
\]

the integer scan selects

\[
\boxed{m=145}
\]

and gives

\[
\boxed{0.6734130852868493916709\ldots}.
\]

Therefore the safe decimal floor is

\[
\boxed{0.6734130852},
\]

i.e. **67.3413085287%** before truncation.

The immediately previous interval-certified state, **67.3406216299%**, is frozen under [`archive/2026-08-12-certified-6734062162/`](archive/2026-08-12-certified-6734062162/).

## Active epsilon tightening

The observed floating minimum remains above the certified target by about \(8.19\times10^{-7}\). The current interval-table range also has enough length to test a modest upward ladder without changing the window or weights. The active hardened workflow therefore probes

```text
0.0078875
0.0078874
0.0078873
0.0078872
```

in descending order until one closes. These values are not promoted until the verifier returns `VERIFIED=true`.

## Reproduction and trust boundary

Run

```bash
sh run.sh
```

for structural checks, interval \(H\) verification, window positivity, exact pressure multiplicity, final arithmetic, and verifier smoke testing. Heavy full-certificate workflows run on `main`.

Checked directly in this repository: exact pair-span capacities, exact declared pressure totals, interval window bounds/positivity, the current six-dimensional local certificate, and final exact-pressure arithmetic. Imported from the lineage: the explicit-formula / trace interface, finite-\(m\) Gram spectral profile, normalized-gap bookkeeping, and analytic link from \(H(v)\) to the zero count.

Independent reproduction of the latest local certificate remains requested before publication-quality use. Historical certified states remain under `archive/` in accordance with [`REPOSITORY_POLICY.md`](REPOSITORY_POLICY.md).

Original repository material is MIT-licensed. Third-party analytic inputs are referenced rather than vendored; see [`THIRD_PARTY.md`](THIRD_PARTY.md).
