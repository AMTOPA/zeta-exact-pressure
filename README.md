# Zeta exact-pressure optimization

> [!IMPORTANT]
> **Current interval-certified research-draft record: 67.3406216299%.**
>
> **Active joint-pressure discovery:** a seven-point / six-gap candidate with variable total pressure projects above the certified record. Its window and exact combinatorics are checked; its full six-dimensional local interval certificate is being tested separately. Until that returns `VERIFIED=true`, it is not the certified record.

This is a research project, not a peer-reviewed theorem and not a proof of the Riemann hypothesis.

## Current interval-certified record

The current certified construction uses eight points / seven gaps and a re-optimized rational 15-term window

\[
v(s)=\sum_{j=0}^{14}c_j\cos(\omega_js),\qquad
\omega_0=\sqrt2,\quad \omega_j=2j\pi\ (1\le j\le14),
\]

with denominator \(10^9\) and numerator vector

```text
1000000000
   7862237
 -11036157
   3734450
   1402396
  -1412889
   3402026
  -1739485
   4930665
  -4255468
   3101956
  -2601879
    146498
    398565
   -271068
```

Direct interval arithmetic gives

\[
H(v)=0.6723405451213867420089258981185\ldots
\]

and verifies the conservative floor

\[
\boxed{H(v)>0.672340545}.
\]

The exact eight-point pressure vector remains

\[
\frac1{2300000000}(474488,829921,1102531,1186120,1102531,829921,474488),
\qquad B=\frac3{1150}.
\]

For every pair span \(s=1,\ldots,7\), the exact pair weights in [`candidate.json`](candidate.json) have total capacity exactly 2.

The hardened seven-dimensional outward-rounded verifier proves

\[
\boxed{F_8(g_1,\ldots,g_7)\ge0.005515}\qquad(g_i\ge0).
\]

The successful run used a 4000 grid, 50-digit interval tables, and `-ffp-contract=off`, and reported

```text
VERIFIED=true
nodes=66686224
pruned=33343136
splits=33343088
convex=27190260
tangent=12043940
max_depth=86
```

The exact table hashes, workflow run `31598015611`, artifact `9142888339`, and artifact digest are recorded in [`candidate.json`](candidate.json) and [`certificates/latest-verification.txt`](certificates/latest-verification.txt).

With

\[
H=0.672340545,\qquad \varepsilon_8=0.005515,\qquad B=3/1150,
\]

the exact-pressure scan selects \(m=203\) and gives

\[
\boxed{0.67340621629894866656\ldots},
\]

hence the safe decimal floor

\[
\boxed{0.6734062162},
\]

i.e. **67.3406216299%** before truncation.

The immediately previous interval-certified state is frozen under [`archive/2026-08-12-certified-6733781954/`](archive/2026-08-12-certified-6733781954/).

## Active joint-pressure discovery

[`discovery_candidate.json`](discovery_candidate.json) releases a parameter previously held fixed during position-pressure optimization: the total local pressure \(B=\sum b_r\). The local-to-global proof uses \(B\) symbolically through

\[
E_B+B\,\operatorname{span}(B)\ge A,
\]

so changing \(B\) is admissible provided the exact pressure total is used in the final penalty, all pressure coefficients remain nonnegative, and every pair-span capacity remains at most 2.

The current discovery candidate uses seven points / six gaps with

\[
B=\frac{93}{23000}=0.004043478260869565\ldots,
\]

a different rational 15-term window, and proposed local target

\[
\varepsilon=0.007887.
\]

Its exact structural checks give all six pair-span capacities equal to 2 and the declared pressure total exactly. Interval arithmetic encloses

\[
H(v)=0.67219990266757577542126938448\ldots
\]

and verifies positivity of the window. The floating adversarial minimum is approximately

\[
0.00788781935047,
\]

so the proposed target has about \(8.19\times10^{-7}\) floating margin.

The machine-readable discovery file currently uses the deliberately loose floor `H=0.6721998` and therefore records a conditional projection of **67.3412981907%**. The already-computed interval enclosure supports the tighter safe floor

\[
H_{\rm floor}=0.6721999026,
\]

which would raise the same `epsilon=0.007887` projection to approximately **67.3413085287%** if the full local certificate closes.

A dedicated workflow, [`.github/workflows/discovery-certificate.yml`](.github/workflows/discovery-certificate.yml), runs the hardened full six-dimensional interval test. No joint-pressure percentage is promoted until that run produces `VERIFIED=true`.

## Reproduction and trust boundary

Run

```bash
sh run.sh
```

for the current certified structural checks, interval \(H\) verification, window positivity, exact multiplicity bookkeeping, final arithmetic, and verifier smoke test.

Checked directly in this repository: exact pair-span capacities, exact declared pressure totals, interval window bounds/positivity, the current seven-dimensional local certificate, and final exact-pressure arithmetic. Imported from the lineage: the explicit-formula / trace interface, finite-\(m\) Gram spectral profile, normalized-gap bookkeeping, and analytic link from \(H(v)\) to the zero count.

Independent reproduction of the latest local certificate remains requested before publication-quality use. Historical certified states remain under `archive/` in accordance with [`REPOSITORY_POLICY.md`](REPOSITORY_POLICY.md).

Original repository material is MIT-licensed. Third-party analytic inputs are referenced rather than vendored; see [`THIRD_PARTY.md`](THIRD_PARTY.md).
