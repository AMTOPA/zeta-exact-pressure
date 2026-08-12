# Zeta exact-pressure optimization

> [!IMPORTANT]
> **Current interval-certified research-draft candidate: 67.3378195478%.**
>
> The current local construction uses eight consecutive points / seven gaps. The target \(\varepsilon_8=0.005482\) is closed by the repository-native outward-rounded interval verifier compiled with `-ffp-contract=off`. The 15-term window has the interval-verified floor \(H>0.6723338866\). The inherited analytic interface remains imported from the lineage repositories, and independent reproduction is still requested before publication-quality use.

This is a research project, not a peer-reviewed theorem and not a proof of the Riemann hypothesis.

## Current construction

The analytic window remains

$$
v(s)=\sum_{j=0}^{14}c_j\cos(\omega_js),\qquad
\omega_0=\sqrt2,\quad \omega_j=2j\pi\ (1\le j\le14),
$$

with denominator $10^9$ and numerator vector

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

Direct interval arithmetic verifies

$$
\boxed{H(v)>0.6723338866}.
$$

The local functional now uses seven nonnegative gaps. Its exact pair weights are reflection-symmetric, nonnegative, and satisfy

$$
\sum_i a_{i,i+s}=2\qquad(1\le s\le7),
$$

while the exact position-pressure vector is

$$
\frac1{2300000000}(474488,829921,1102531,1186120,1102531,829921,474488),
$$

with total

$$
B=\frac3{1150}.
$$

These are the same capacity and pressure conditions used by the predecessor local-to-global argument, now with seven gap positions and therefore $m-7$ local windows per $m$-point block.

## Seven-dimensional local certificate

The exact rational weights were obtained by a reflection-symmetric trust-region optimization. Discovery hardening included unscreened polishing of all 8,320 reflection representatives of `{1,2,3,4}^7`, an additional `{1,2,3,5}^7` stress family, and multi-range differential evolution. The lowest observed floating basin is approximately

$$
0.005482799831021096\ldots.
$$

The promoted rigorous target is

$$
\boxed{\varepsilon_8=0.005482=2741/500000}.
$$

The hardened 4000-grid / 50-digit interval run reports

```text
VERIFIED=true
nodes=56348888
pruned=28174468
splits=28174420
convex=21755661
tangent=9522833
max_depth=83
```

It started from 48 interval boxes with component pattern `1,2,2,3,2,2,1`. The six exact table hashes, workflow run `31594502822`, artifact `9141284166`, and artifact digest are recorded in [`candidate.json`](candidate.json) and [`certificates/latest-verification.txt`](certificates/latest-verification.txt).

## Exact-pressure projection

For $Q=7$ gaps set

$$
A_m=\varepsilon_8(m-7),\qquad R_m=h_m(A_m),\qquad \eta_m=R_m/A_m,
$$

where

$$
h_m(E)=
\begin{cases}
E,&E\le m/(m-1),\\
E/m+2\sqrt{(m-1)E/m}-1,&E\ge m/(m-1).
\end{cases}
$$

Exact shifted-pressure averaging gives

$$
\frac{N_0^s(T,2T)}{N(T,2T)}\ge
\frac{mH-\eta_mB(m-7)}{m-R_m}-o(1).
$$

Using

$$
H=0.6723338866,\qquad \varepsilon_8=0.005482,\qquad B=3/1150,
$$

the integer scan selects $m=204$ and gives

$$
0.67337819547776013737165417055\ldots,
$$

so the safe decimal floor is

$$
\boxed{0.6733781954},
$$

i.e. **67.3378195478%** before decimal truncation.

The previous **67.3331466374%** seven-point record is frozen under [`archive/2026-08-12-certified-6733314663/`](archive/2026-08-12-certified-6733314663/). Earlier records remain under `archive/`.

## Next numerical direction

The current eight-point certificate is not the end of the search. A separate discovery-level window–basin exchange, still unpromoted, has already found a rationalized 15-term window with floating eight-point minimum about `0.00551171006` and $H\approx0.67234331014$. Conservative inputs `H=0.6723433`, `epsilon=0.005510` project roughly **67.340575%**. That candidate must pass the same rigorous seven-dimensional interval process before it can replace the current record.

## Reproduction and trust boundary

Run

```bash
sh run.sh
```

for structural consistency, interval $H$ verification, window positivity, exact pressure multiplicity, final arithmetic, and verifier compilation/smoke testing. Heavy full-certificate workflows are kept on `main` and invoked as needed under [`REPOSITORY_POLICY.md`](REPOSITORY_POLICY.md).

Checked directly here: exact span capacities, exact pressure total, interval $H$, the seven-gap local inequality, shifted-pressure multiplicity, and final arithmetic. Still imported: the explicit-formula / trace interface, finite-$m$ Gram spectral profile, normalized-gap bookkeeping, and the analytic link from $H(v)$ to the zero count.

Original repository material is MIT-licensed. Third-party analytic inputs are referenced rather than vendored; see [`THIRD_PARTY.md`](THIRD_PARTY.md).
