# Current deduction outline

> **Status:** the current seven-point / six-gap joint-pressure target `0.007887` and working window floor `H > 0.6721999026` are interval-certified in this repository. The analytic interface in §1 remains imported from the lineage repositories, and independent reproduction of the new six-dimensional certificate is still requested.

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

## 2. Joint-pressure analytic window

Use

$$
v(s)=\sum_{j=0}^{14}c_j\cos(\omega_js),\qquad
\omega_0=\sqrt2,\quad\omega_j=2j\pi\ (1\le j\le14),
$$

with denominator $10^9$ and numerator vector

```text
1000000000,
12948011,
-12114181,
3684033,
5911261,
-1663892,
5928575,
-7167828,
6229914,
-5147758,
-756341,
440544,
-311207,
237969,
-190433
```

Direct interval arithmetic encloses

$$
H(v)=0.672199902667575775421269384482413\ldots
$$

and proves

$$
\boxed{H(v)>0.6721999026}.
$$

The same interval subdivision proves positivity of the window.

## 3. Local functional with variable total pressure

For six nonnegative gaps set $y_0=0$ and $y_j=g_1+\cdots+g_j$. Define

$$
F(g)=\sum_{r=1}^{6}b_rg_r+
\sum_{0\le i<j\le6}a_{ij}W(y_j-y_i).
$$

The exact nonnegative pair weights in `candidate.json` satisfy

$$
\boxed{\sum_{i=0}^{6-s}a_{i,i+s}=2}\qquad(1\le s\le6).
$$

The exact pressure vector is

$$
\frac1{46000000000}
(22420713,32878293,37700994,37700994,32878293,22420713),
$$

so

$$
\boxed{B=\sum_{r=1}^{6}b_r=\frac{93}{23000}}.
$$

The predecessor proof uses the position pressure only through the symbolic total $B=\sum b_r$: after summing translated local inequalities it obtains

$$
E_B+B\,\operatorname{span}(B)\ge A.
$$

Thus fixing $B=3/1150$ was a design restriction of the predecessor optimization, not an analytic requirement. The present construction legitimately varies $B$, preserves nonnegative pressures and span capacities 2, and uses the new exact $B$ in the final penalty.

## 4. Certified six-dimensional inequality

Adversarial exchange over the total pressure, window, pair weights, and pressure distribution found a floating minimum near

$$
0.0078878193504693\ldots.
$$

The hardened outward-rounded verifier proves

$$
\boxed{F(g_1,\ldots,g_6)\ge0.007887}\qquad(g_i\ge0).
$$

The 4000-grid / 50-digit run, compiled with `-ffp-contract=off`, reports

```text
VERIFIED=true
nodes=3424276
pruned=1712170
splits=1712106
convex=1756299
tangent=801918
max_depth=71
```

It starts from 64 initial boxes with component counts `2,2,2,2,2,2`. The table hashes, workflow run `31603343875`, artifact `9144421792`, and artifact digest are recorded in `candidate.json` and `certificates/latest-verification.txt`.

## 5. Exact shifted-pressure deduction

For an $m$-point block there are $m-6$ translated seven-point windows. Set

$$
A_m=\varepsilon(m-6),\qquad
R_m=h_m(A_m),\qquad
\eta_m=R_m/A_m.
$$

The span-capacity identities control the summed pair contribution by the predecessor block energy, while exact shifted accounting gives pressure charge $(m-6)B$. Hence

$$
\Delta(M)\ge\frac{R_m}{m}S-
\frac{\eta_mB(m-6)}{m}N-o(N),
$$

and therefore

$$
\boxed{
\frac SN\ge
\frac{mH-\eta_mB(m-6)}{m-R_m}-o(1)
}.
$$

## 6. Final arithmetic

Use the certified conservative values

$$
H=0.6721999026,\qquad
\varepsilon=0.007887,\qquad
B=\frac{93}{23000}.
$$

The integer scan selects

$$
\boxed{m=145}.
$$

Then

$$
A_{145}=1.096293,
$$

$$
R_{145}=1.09440740970772755724598196593800412029\ldots,
$$

and

$$
\eta_{145}=0.99828003071051950276612362382866999998\ldots.
$$

Thus

$$
\frac SN\ge
0.67341308528684939167090457164160\ldots-o(1),
$$

so safely

$$
\boxed{
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
>0.6734130852
}.
$$

The certified conservative inputs therefore give **67.3413085287%** before decimal truncation.

## 7. Current tightening experiment

The same exact window and local weights have an observed floating margin of about $8.19\times10^{-7}$ above the certified target. The current hardened workflow probes the upward ladder

$$
0.0078875,\quad0.0078874,\quad0.0078873,\quad0.0078872,
$$

without changing any other parameter. None of these values is part of the certified statement above until the interval verifier closes it.

## Trust boundary

The current interval window bound, exact six-span capacities, exact pressure total, six-dimensional local certificate, shifted-pressure bookkeeping, and final arithmetic are checked in this repository. The explicit-formula / trace interface and finite-$m$ Gram profile remain imported from prior work. Independent reproduction is still requested, so the result remains an interval-certified research-draft candidate rather than a publication-ready theorem.
