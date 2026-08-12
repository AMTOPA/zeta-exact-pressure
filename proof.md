# Current deduction outline

> **Status:** the current 15-term local target `0.005401` is interval-certified in this repository. The analytic interface in §1 remains imported from the lineage repositories, and independent reproduction of the new local certificate is still requested.

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

## 2. Robust 15-term window

Use

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

High-precision evaluation gives

$$
H(v)=0.672333886657942\ldots,
$$

and direct interval arithmetic verifies the working floor

$$
\boxed{H(v)>0.6723338}.
$$

## 3. Certified local seven-point inequality

For six nonnegative consecutive gaps, the exact pair weights recorded in `candidate.json`, and the position-pressure vector

$$
\frac1{2300000000}(831522,1096590,1071888,1071888,1096590,831522),
$$

the repository-native interval verifier proves

$$
\boxed{F(g_1,\ldots,g_6)\ge0.005401}\qquad(g_i\ge0).
$$

The successful 4000-grid / 50-digit run reports

```text
VERIFIED=true
nodes=3171002
pruned=1585573
splits=1585429
convex=1776812
tangent=751200
max_depth=62
```

The exact table hashes and provenance are in `candidate.json` and `certificates/latest-verification.txt`.

The pressure total is exactly

$$
B=\sum_{r=1}^6b_r=\frac3{1150}.
$$

## 4. Exact pressure multiplicity

For an $m$-point block, summing the seven-point inequality over the $m-6$ local windows gives total pressure charge

$$
(m-6)B.
$$

Averaging over shifted block partitions retains this exact charge, rather than replacing it by the coarser $B(m-1)$.

## 5. Spectral conversion

Set

$$
A_m=\varepsilon(m-6),\qquad R_m=h_m(A_m),\qquad \eta_m=R_m/A_m.
$$

Then

$$
\Delta(M)\ge\frac{R_m}{m}S-\frac{\eta_mB(m-6)}{m}N-o(N),
$$

and substitution into the imported counting inequality yields

$$
\boxed{
\frac SN\ge\frac{mH-\eta_mB(m-6)}{m-R_m}-o(1)
}.
$$

## 6. Final arithmetic

Use the interval-certified working values

$$
H=0.6723338,\qquad \varepsilon=0.005401,\qquad B=3/1150.
$$

The integer scan selects

$$
m=204
$$

and gives

$$
\frac SN\ge0.6733305982879586830508445665\ldots-o(1).
$$

Therefore the safely truncated research-draft candidate is

$$
\boxed{
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
>0.6733305982
}.
$$

Numerically this corresponds to **67.3330598288%** before decimal truncation.

## Trust boundary

The new numerical ingredients in §§2–3 and the arithmetic in §§4–6 are checked in this repository. The analytic interface in §1 remains imported. The new local certificate has not yet received an independent second implementation/reproduction, so the result remains a research-draft candidate rather than a publication-ready theorem.
