# Current deduction outline

> **Status:** the current eight-point / seven-gap local target `0.005482` and the working window floor `H > 0.6723338866` are interval-certified in this repository. The analytic interface in §1 remains imported from the lineage repositories, and independent reproduction of the new seven-dimensional certificate is still requested.

## 1. Imported analytic interface

Let $S=N_0^s(T,2T)$ and $N=N(T,2T)$. The predecessor framework supplies

$$
S\ge HN+\Delta(M)-o(N),
$$

together with

$$
h_m(E)=
\begin{cases}
E,&E\le m/(m-1),\\
E/m+2\sqrt{(m-1)E/m}-1,&E\ge m/(m-1).
\end{cases}
$$

These analytic ingredients are imported.

## 2. Analytic window

The certified eight-point result uses the same rational 15-term window

$$
v(s)=\sum_{j=0}^{14}c_j\cos(\omega_js),\qquad
\omega_0=\sqrt2,\quad\omega_j=2j\pi\ (1\le j\le14),
$$

with denominator $10^9$ and numerator vector

```text
1000000000,
8629738,
-10085378,
1746803,
1125700,
-2203905,
1904615,
-4559603,
7930665,
-3022627,
2165339,
398121,
-255934,
188899,
-148305
```

Direct interval arithmetic verifies

$$
\boxed{H(v)>0.6723338866}.
$$

## 3. Eight-point local functional

Let $g_1,\ldots,g_7\ge0$ be seven consecutive normalized gaps and set

$$
y_0=0,\qquad y_j=g_1+\cdots+g_j.
$$

The local functional is

$$
F_8(g)=\sum_{r=1}^7 b_rg_r+
\sum_{0\le i<j\le7}a_{ij}W(y_j-y_i).
$$

The exact nonnegative pair weights are recorded in `candidate.json` and satisfy, for every index span,

$$
\boxed{\sum_{i=0}^{7-s}a_{i,i+s}=2}\qquad(1\le s\le7).
$$

The position-pressure vector is

$$
\frac1{2300000000}
(474488,829921,1102531,1186120,1102531,829921,474488),
$$

and hence

$$
\boxed{B=\sum_{r=1}^7b_r=\frac3{1150}}.
$$

These are precisely the pair-capacity and total-pressure facts used in the predecessor block deduction. The proof is not tied to six gaps: replacing six by seven simply gives $m-7$ translated local windows in an $m$-point block.

## 4. Certified seven-dimensional inequality

For the exact rational parameters above, the repository-native outward-rounded interval verifier proves

$$
\boxed{F_8(g_1,\ldots,g_7)\ge0.005482}\qquad(g_i\ge0).
$$

The certificate was generated with 4000 cells per normalized unit, 50 decimal digits in the interval-table builder, and C++ compiled with `-ffp-contract=off`. It started from 48 boxes and reports

```text
VERIFIED=true
nodes=56348888
pruned=28174468
splits=28174420
convex=21755661
tangent=9522833
max_depth=83
```

Exact table hashes, workflow run `31594502822`, and artifact `9141284166` are recorded in `candidate.json` and `certificates/latest-verification.txt`.

## 5. Exact pressure multiplicity for seven gaps

For an $m$-point block there are $m-7$ translated eight-point windows. Summing their local inequalities gives total right-hand side

$$
A_m=\varepsilon_8(m-7).
$$

Because each local pressure vector has total $B$, exact shifted-block averaging gives pressure charge

$$
(m-7)B.
$$

The span-capacity identities imply that the summed pair contribution is dominated by the same block pair energy used in the predecessor spectral estimate. Thus the predecessor block argument extends with $6$ replaced by $7$.

## 6. Spectral conversion

Set

$$
A_m=\varepsilon_8(m-7),\qquad
R_m=h_m(A_m),\qquad
\eta_m=R_m/A_m.
$$

Then

$$
\Delta(M)\ge\frac{R_m}{m}S-
\frac{\eta_mB(m-7)}{m}N-o(N),
$$

and therefore

$$
\boxed{
\frac SN\ge
\frac{mH-\eta_mB(m-7)}{m-R_m}-o(1)
}.
$$

## 7. Final arithmetic

Use the certified values

$$
H=0.6723338866,\qquad
\varepsilon_8=0.005482,\qquad
B=3/1150.
$$

The integer scan selects

$$
m=204.
$$

Then

$$
A_{204}=1.079954,
$$

$$
R_{204}=1.0786101804671024521213591572698778\ldots,
$$

and the exact-pressure formula gives

$$
\frac SN\ge
0.6733781954777601373716541705496368620\ldots-o(1).
$$

Hence safely

$$
\boxed{
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
>0.6733781954
}.
$$

Numerically the conservative inputs give **67.3378195478%** before decimal truncation.

## Trust boundary

The window interval bound, exact eight-point span capacities, exact pressure total, seven-dimensional local certificate, shifted-pressure bookkeeping, and final arithmetic are checked in this repository. The explicit-formula / trace interface and finite-$m$ Gram profile remain imported from prior work. Independent reproduction of the new seven-dimensional certificate is requested, so this remains an interval-certified research-draft candidate rather than a publication-ready theorem.
