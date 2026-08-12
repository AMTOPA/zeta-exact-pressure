# Zeta exact-pressure optimization

> [!IMPORTANT]
> **Current interval-certified research-draft record: 67.3378195478%.**
>
> **Active discovery target: 67.3412981907%.** The discovery target uses a jointly re-optimized total pressure, 15-term window, pair weights, and position-pressure vector. Its window contribution has been interval-checked, but the new six-gap local target \(F\ge0.007887\) has **not yet** been closed by the full outward-rounded branch-and-bound verifier. It is therefore not promoted to the certified record.

This is a research project, not a peer-reviewed theorem and not a proof of the Riemann hypothesis.

## Current interval-certified record

The certified record remains the eight-point / seven-gap construction with

\[
H>0.6723338866,\qquad
\varepsilon_8=0.005482,\qquad
B=\frac3{1150},
\]

and exact shifted-pressure averaging. The integer scan selects \(m=204\) and gives

\[
\boxed{0.67337819547776013737\ldots}
\]

or

\[
\boxed{\mathbf{67.3378195478\%}}.
\]

The full machine-readable parameters remain in [`candidate.json`](candidate.json). The exact state that was current before the new discovery experiment is frozen under [`archive/2026-08-12-certified-6733781954/`](archive/2026-08-12-certified-6733781954/).

## Active joint-pressure discovery candidate

The new search deliberately releases a parameter that the certified lineage had kept fixed: the **total local pressure**. It then re-optimizes the pressure strength together with the analytic window, pair weights, and position-pressure distribution while preserving all exact local-to-global capacity identities.

The candidate returns to seven points / six gaps so that the finite inequality remains six-dimensional and can reuse the hardened verifier architecture.

### 15-term window

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

High-precision evaluation gives

\[
H(v)=0.67219990266757577542126938448\ldots.
\]

A direct `mpmath.iv` enclosure gives

\[
H(v)\in
[0.67219990266757577542126938448241349658\ldots,
 0.67219990266757577542126938448241349659\ldots],
\]

so the conservative projection uses

\[
\boxed{H_{\rm floor}=0.6721998}.
\]

A 4096-cell interval subdivision of \([0,1/2]\) gives a window lower bound above \(0.76161066\).

### Exact pair and pressure constraints

The exact pair weights are listed in [`discovery_candidate.json`](discovery_candidate.json). They are nonnegative and satisfy, **for every span** \(s=1,\ldots,6\),

\[
\boxed{\sum_i a_{i,i+s}=2}.
\]

The exact position-pressure vector is

\[
\frac1{46000000000}
(22420713,32878293,37700994,37700994,32878293,22420713),
\]

with exact total

\[
\boxed{
B=\frac{93}{23000}=0.004043478260869565\ldots
}.
\]

This is the main new global degree of freedom relative to the previous certified constructions.

### Adversarial local search

The rounded rational candidate has an observed floating local minimum

\[
F_{\min}^{\rm float}\approx0.00788781935
\]

near

\[
(1.042887,\ 1.974405,\ 1.046258,\ 1.972360,\ 1.044510,\ 1.978097).
\]

The proposed rigorous target is deliberately lower:

\[
\boxed{\varepsilon=\frac{7887}{10^6}=0.007887}.
\]

The remaining gap is therefore about \(8.19\times10^{-7}\).

This target is **not yet interval-certified**. It must return `VERIFIED=true` from the full six-dimensional outward-rounded branch-and-bound before the discovery value can replace the current certified record.

## Exact-pressure projection of the pending target

For six gaps,

\[
A_m=\varepsilon(m-6),\qquad
R_m=h_m(A_m),\qquad
\eta_m=\frac{R_m}{A_m},
\]

where

\[
h_m(E)=
\begin{cases}
E,&E\le m/(m-1),\\
E/m+2\sqrt{(m-1)E/m}-1,&E\ge m/(m-1).
\end{cases}
\]

The shifted-pressure deduction is

\[
\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\frac{mH-\eta_mB(m-6)}{m-R_m}-o(1).
\]

Using only the conservative discovery inputs

\[
H=0.6721998,\qquad
\varepsilon=0.007887,\qquad
B=\frac{93}{23000},
\]

the integer scan selects

\[
\boxed{m=145}
\]

and projects

\[
0.67341298190657255729\ldots,
\]

hence, **conditional only on closing the pending finite local certificate**,

\[
\boxed{\mathbf{67.3412981907\%}}.
\]

The stronger floating discovery projection is about **67.34136123%**, but it is not used as a certification target.

## Reproduction and trust boundary

- [`candidate.json`](candidate.json) remains the current interval-certified record.
- [`discovery_candidate.json`](discovery_candidate.json) is the machine-readable active discovery candidate.
- [`src/check_discovery_candidate.py`](src/check_discovery_candidate.py) checks exact span capacities, exact total pressure, the interval window floor/positivity, and the final conservative projection. It does **not** certify the six-gap local inequality.
- The full local interval closure remains pending; until it succeeds, 67.3412981907% must not be described as interval-certified.
- The explicit-formula / trace interface, finite-\(m\) Gram spectral profile, normalized-gap bookkeeping, and analytic link from \(H(v)\) to the zero count remain imported from the existing lineage.

Historical certified states and rejected/superseded experiments remain under `archive/`, in accordance with [`REPOSITORY_POLICY.md`](REPOSITORY_POLICY.md).

Original repository material is MIT-licensed. Third-party analytic inputs are referenced rather than vendored; see [`THIRD_PARTY.md`](THIRD_PARTY.md).
