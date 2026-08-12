# Current deduction outline

> **Status:** the current eight-point / seven-gap target `0.005515` and working window floor `H > 0.672340545` are interval-certified in this repository. The analytic interface in §1 remains imported from the lineage repositories, and independent reproduction of the seven-dimensional certificate is still requested.

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

## 2. Certified analytic window

Use

$$
v(s)=\sum_{j=0}^{14}c_j\cos(\omega_js),\qquad
\omega_0=\sqrt2,\quad\omega_j=2j\pi\ (1\le j\le14),
$$

with denominator $10^9$ and numerator vector

```text
1000000000,
7862237,
-11036157,
3734450,
1402396,
-1412889,
3402026,
-1739485,
4930665,
-4255468,
3101956,
-2601879,
146498,
398565,
-271068
```

Direct interval arithmetic encloses

$$
H(v)=0.672340545121386742008925898118525\ldots
$$

and proves

$$
\boxed{H(v)>0.672340545}.
$$

The same interval subdivision verifies positivity of the window.

## 3. Eight-point local functional

Let $g_1,\ldots,g_7\ge0$, put $y_0=0$ and $y_j=g_1+\cdots+g_j$, and define

$$
F_8(g)=\sum_{r=1}^7 b_rg_r+
\sum_{0\le i<j\le7}a_{ij}W(y_j-y_i).
$$

The exact nonnegative pair weights in `candidate.json` satisfy

$$
\boxed{\sum_{i=0}^{7-s}a_{i,i+s}=2}\qquad(1\le s\le7),
$$

and the pressure vector is

$$
\frac1{2300000000}
(474488,829921,1102531,1186120,1102531,829921,474488),
$$

so

$$
\boxed{B=\sum_{r=1}^7b_r=\frac3{1150}}.
$$

## 4. Certified seven-dimensional inequality

The hardened outward-rounded verifier proves

$$
\boxed{F_8(g_1,\ldots,g_7)\ge0.005515}\qquad(g_i\ge0).
$$

The 4000-grid / 50-digit run, compiled with `-ffp-contract=off`, reports

```text
VERIFIED=true
nodes=66686224
pruned=33343136
splits=33343088
convex=27190260
tangent=12043940
max_depth=86
```

The table hashes, workflow run `31598015611`, and artifact `9142888339` are recorded in `candidate.json` and `certificates/latest-verification.txt`.

## 5. Exact shifted-pressure deduction

For an $m$-point block there are $m-7$ translated eight-point windows. Set

$$
A_m=\varepsilon_8(m-7),\qquad
R_m=h_m(A_m),\qquad
\eta_m=R_m/A_m.
$$

Exact shifted-block accounting gives total pressure charge $(m-7)B$, while the span-capacity identities control the pair contribution by the predecessor block energy. Hence

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

## 6. Final arithmetic

Use

$$
H=0.672340545,\qquad
\varepsilon_8=0.005515,\qquad
B=3/1150.
$$

The integer scan selects

$$
\boxed{m=203}.
$$

Then

$$
A_{203}=1.08094,
$$

$$
R_{203}=1.07956220302209765100385204312294\ldots,
$$

and

$$
\eta_{203}=0.99872537145641538938687812748436\ldots.
$$

Thus

$$
\frac SN\ge
0.67340621629894866656390422423548\ldots-o(1),
$$

so safely

$$
\boxed{
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
>0.6734062162
}.
$$

The conservative inputs therefore give **67.3406216299%** before decimal truncation.

## 7. Joint-pressure extension under test

The local-to-global argument above actually uses the total pressure only through the symbolic quantity $B=\sum b_r$. In the predecessor proof, summing the local inequalities gives

$$
E_B+B\,\operatorname{span}(B)\ge A,
$$

and the subsequent block deduction carries that same $B$ into the global penalty. Thus the proof does not intrinsically force $B=3/1150$; that value was held fixed in the positioned-pressure predecessor to isolate redistribution as a new lever.

The active `discovery_candidate.json` therefore tests a legitimate further degree of freedom with

$$
B=\frac{93}{23000},\qquad \varepsilon=0.007887,
$$

while preserving nonnegative pressures and exact span capacities 2. Its window and structural constraints are already interval/exact checked. Promotion still requires the dedicated full six-dimensional local verifier to return `VERIFIED=true`.

## Trust boundary

The current window interval bound, exact eight-point span capacities, exact pressure total, seven-dimensional local certificate, shifted-pressure bookkeeping, and final arithmetic are checked in this repository. The explicit-formula / trace interface and finite-$m$ Gram profile remain imported from prior work. Independent reproduction is still requested, so the result remains an interval-certified research-draft candidate rather than a publication-ready theorem.
