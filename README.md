# Zeta exact-pressure optimization

> [!IMPORTANT]
> **Current interval-certified research-draft record under the existing scalar Gram interface: 67.3416490971%.**
>
> A new analytic-extension experiment that retains six-band Gram information projects to **67.3423563564%**, but that new matrix lemma is not yet promoted to the root record; it requires independent mathematical review.

This is a research project, not a peer-reviewed theorem and not a proof of the Riemann hypothesis.

## Current certified baseline

The current root construction uses seven points / six gaps, exact total position pressure

\[
B=\frac{93}{23000},
\]

and a second-exchange 17-term analytic window

\[
v(s)=\sum_{j=0}^{16}c_j\cos(\omega_js),
\qquad
\omega_0=\sqrt2,
\quad \omega_j=2j\pi\ (1\le j\le16).
\]

The rational coefficient denominator is \(10^9\), with numerator vector

```text
1000000000
   12378982
  -12602495
    4164033
    5741405
   -1724025
    6219280
   -8047828
    6321519
   -5241981
    -892658
     560544
    -431207
     357969
    -310433
     100000
    -100000
```

Interval arithmetic gives

\[
H(v)=0.67218815811823458516945638772565\ldots
\]

and proves the conservative floor

\[
\boxed{H(v)>0.6721881580}.
\]

The same 4096-cell interval subdivision gives a positive window lower bound above `0.7616418486`.

### Certified local inequality

The local functional has the exact pair and position-pressure coefficients stored in [`candidate.json`](candidate.json). Every pair span \(s=1,\ldots,6\) has exact total capacity 2, and the position pressures sum exactly to \(93/23000\).

Unscreened adversarial exchange found a floating minimum near

\[
0.007911105155226424\ldots.
\]

The hardened six-dimensional outward-rounded verifier proves

\[
\boxed{F(g_1,\ldots,g_6)\ge0.0079107}
\qquad(g_i\ge0).
\]

The successful 4000-grid / 50-digit run, compiled with `-ffp-contract=off`, reports

```text
VERIFIED=true
nodes=3768186
pruned=1884125
splits=1884061
convex=2030240
tangent=936616
max_depth=74
```

Evidence is recorded in `candidate.json`:

```text
workflow run = 31610179703
artifact id = 9147378469
artifact digest sha256 = 871532c739d5a9e8de770cf00675381ea4fd9c81f212d8e46f86403a27a34dc1
```

## Existing scalar-Gram projection

Under the inherited finite-dimensional profile

\[
R_m=h_m(A_m),
\qquad
A_m=\varepsilon(m-6),
\qquad
\eta_m=R_m/A_m,
\]

the shifted-pressure deduction gives

\[
\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\frac{mH-\eta_mB(m-6)}{m-R_m}-o(1).
\]

Using only the certified conservative inputs

\[
H=0.6721881580,
\qquad
\varepsilon=0.0079107,
\qquad
B=\frac{93}{23000},
\]

the integer scan selects

\[
\boxed{m=145}
\]

and gives

\[
\boxed{0.67341649097149929495\ldots}.
\]

Therefore the safe decimal floor is

\[
\boxed{0.6734164909},
\]

i.e. **67.3416490971%** before truncation.

The immediately previous certified state, **67.3415313957%**, is frozen under [`archive/2026-08-12-certified-6734153139/`](archive/2026-08-12-certified-6734153139/).

## New direction: retain band-position information

The scalar profile \(h_m\) is sharp if only total off-diagonal energy is known. The translated local certificate, however, gives more structure: it only uses pairs with index span at most six. The active analytic-extension experiment therefore retains

\[
E_6=2\sum_{1\le j-i\le6}|G_{ij}|^2
\]

instead of immediately relaxing it to the full off-diagonal energy.

A coloring / Frobenius-distance argument gives the proposed continuous banded profile

\[
g_q(E)=
\begin{cases}
E,&E\le(q+1)/q,\\
2\sqrt{\frac{q+1}{q}E}-\frac{q+1}{q},&E\ge(q+1)/q.
\end{cases}
\]

Using the already interval-certified 17-term local input, exact rational arithmetic with this profile selects \(m=165\) and projects to

\[
\boxed{0.6734235635636362491\ldots}
\]

or

\[
\boxed{67.3423563564\%}
\]

with safe floor `0.6734235635`.

This is **not yet the root certified record**: the local numerical certificate is rigorous and the final arithmetic is exact, but the new banded-Gram analytic lemma and its insertion into shifted-block pinching need independent mathematical review. The full proof sketch and machine-readable arithmetic are under [`experiments/banded-gram/`](experiments/banded-gram/).

## Why mixed local geometries were not enough

A same-window 7-point / 8-point mixture was tested first. The interior pair-capacity constraint forces the mixture coefficients to form a convex combination, and after the usual scalar \(A_m\to h_m(A_m)\) compression the optimizer selected an endpoint rather than an interior mixture. This negative result is what motivated changing the Gram step instead of continuing to mix certificates before the scalar bottleneck.

A preliminary five-gap experiment was also tested because its band threshold is larger. Free LP weights initially overfit badly; adversarial exchange pushed the robust local minimum well below the level required to beat the six-gap construction. For now, six gaps appears to be the better geometry for the new banded profile.

## Reproduction and trust boundary

Run

```bash
sh run.sh
```

for root structural checks, interval-window verification, final arithmetic, verifier smoke testing, and the exact arithmetic of the banded-Gram experiment.

Checked directly in this repository: exact pair-span capacities, exact declared pressure totals, interval window bounds/positivity, the current six-dimensional local certificate, existing scalar-Gram final arithmetic, and the rational arithmetic of the new banded experiment. Imported from the lineage: the explicit-formula / trace interface and shifted-block framework. The new banded-Gram matrix inequality is documented locally but still awaits independent review.

Historical certified states remain under `archive/` in accordance with [`REPOSITORY_POLICY.md`](REPOSITORY_POLICY.md). Original repository material is MIT-licensed. Third-party analytic inputs are referenced rather than vendored; see [`THIRD_PARTY.md`](THIRD_PARTY.md).
