# Zeta exact-pressure optimization

> **Current research-draft candidate.** A joint window / exact-pressure refinement of the positioned-pressure method gives the candidate lower bound
>
> \[
> \liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
> \ge 0.67329075601922263576\ldots,
> \]
>
> i.e. **67.3290756019%** of the nontrivial zeros are simple zeros on the critical line, subject to the imported analytic interface and the certified seven-point input described below.

This repository is intended to be **continuously updated** as the window, local certificate, pressure weights, or block deduction improve. The repository name therefore does not contain a numerical suffix.

> [!IMPORTANT]
> This is a research draft, not a peer-reviewed theorem and not a proof of the Riemann hypothesis. The current finite-dimensional certificate has been reproduced in the development environment using an outward-rounded interval branch-and-bound verifier adapted from `sxuff/zeta-positioned-pressure`, but independent reproduction on a separate implementation/machine is still requested.

## Current headline

Using

\[
H_{\rm cert}=0.6724057,\qquad
\varepsilon=0.0052289,\qquad
B=\frac{3}{1150},
\]

and the exact shifted-pressure average, the optimal scanned block length is

\[
m=210,
\]

giving

\[
\boxed{
0.6732907560192226357616716519\ldots
}
\]

or

\[
\boxed{\mathbf{67.3290756019\%}}.
\]

A conservative decimal lower bound is

\[
\frac{6732907560}{10^{10}}=0.6732907560.
\]

## Comparison

| Source | Candidate / reported lower bound |
| --- | ---: |
| Anthropic / Claude, Theorem D | 67.2500703679% |
| `ainta/zeta-simple-zeros` | 67.3008527927% |
| `trmdy/zeta-simple-zeros-673137` | 67.3137630699% |
| `sxuff/zeta-positioned-pressure` | 67.3205978423% |
| `AMTOPA/zeta-exact-pressure-673262` | 67.3262375585% |
| **this repository** | **67.3290756019%** |

The comparison is meaningful only under the same imported analytic interface.

## What changed

The predecessor `AMTOPA/zeta-exact-pressure-673262` retained the exact position-dependent pressure multiplicities through shifted-block averaging. That improvement is retained here.

The new contribution is to **feed the exact-pressure global objective back into the window design**.

The seven-term window is

\[
v(s)=\sum_{j=0}^{6} c_j\cos(\omega_j s),
\]

with

\[
\omega_0=\sqrt2,\qquad \omega_j=2j\pi\quad(1\le j\le6),
\]

and exact rational coefficients

\[
(c_0,\ldots,c_6)=10^{-9}
(1000000000,\,
6907835,\,
-9359173,\,
528441,\,
1509267,\,
-4923883,\,
1358707).
\]

For this window,

\[
H(v)=0.67240570242660302900695918\ldots,
\]

so the repository uses the safe rational value

\[
H_{\rm cert}=\frac{6724057}{10^7}.
\]

The position-dependent pressure weights remain

\[
\frac1{2300000000}
(831522,1096590,1071888,1071888,1096590,831522),
\]

whose exact sum is

\[
B=\frac3{1150}.
\]

The interval branch-and-bound computation certified

\[
F(g_1,\ldots,g_6)\ge
\frac{52289}{10^7}=0.0052289
\]

for all \(g_i\ge0\), using the same pair-weight layout as `sxuff/zeta-positioned-pressure`.

The floating-point search found a slightly higher apparent minimum, but a target of `0.00522895` was **not** accepted by the interval verifier. The published target therefore stops at the proven `0.0052289`.

## Exact-pressure deduction

For an \(m\)-point block, let

\[
A_m=\varepsilon(m-6),\qquad
R_m=h_m(A_m),\qquad
\eta_m=\frac{R_m}{A_m},
\]

where

\[
h_m(E)=
\begin{cases}
E,&0\le E\le m/(m-1),\\[1mm]
E/m+2\sqrt{(m-1)E/m}-1,&E\ge m/(m-1).
\end{cases}
\]

Retaining the exact local pressure multiplicities through all \(m\) shifted partitions gives

\[
\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\frac{mH_{\rm cert}-\eta_mB(m-6)}{m-R_m}
-o(1).
\]

Scanning integer \(m\) selects \(m=210\).

## Reproduction

Python checks:

```bash
python3 src/check_window.py
python3 src/check_multiplicity.py
python3 src/check_final_bound.py
```

or:

```bash
sh run.sh
```

The local seven-point certificate is heavier. See
[`docs/reproduce-local-certificate.md`](docs/reproduce-local-certificate.md).

## Trust boundary

### Checked directly in this repository

- exact pressure-position multiplicity identity;
- the exact shifted-partition global deduction;
- high-precision and interval evaluation of the final bound;
- high-precision / interval evaluation of the new window functional \(H(v)\);
- a subdivision check of positivity of the new window on \([-1/2,1/2]\).

### Certificate record from the current computation

For target

\[
\varepsilon=0.0052289
\]

the adapted interval verifier returned:

```text
VERIFIED=true
nodes=2334226
pruned=1167275
splits=1166951
convex=1407996
tangent=595297
max_depth=77
```

A lower target was also checked in a no-tangent exhaustive mode as an additional robustness check. Independent reproduction remains desirable.

### Imported analytic inputs

This repository does not reprove:

- the explicit-formula / trace inequality underlying the method;
- the finite-\(m\) Gram spectral profile \(h_m\);
- the asymptotic normalized-gap bookkeeping;
- the analytic derivation linking the window functional \(H(v)\) to the zero count.

These belong to the Anthropic / `trmdy` / `sxuff` lineage.

## Repository policy

This repository intentionally has **no numerical suffix**. Future improvements should update:

- `candidate.json`;
- this README headline;
- certificate records;
- parameters / reproduction notes;

rather than creating a new repository for every decimal improvement.

## License and attribution

Original material in this repository is released under the MIT License. Third-party verifiers and analytic inputs are referenced rather than vendored; see [`THIRD_PARTY.md`](THIRD_PARTY.md).
