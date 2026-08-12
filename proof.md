# Current deduction outline

> **Status:** the global deduction below is arithmetic/analytic bookkeeping for the current 11-term **discovery candidate**. The new local inequality at target `0.005405` is not yet interval-certified, so the projected 67.333% value is not yet a proved lower bound.

The previous 67.3290756019% interval-certified research-draft record is frozen under [`archive/2026-08-12-certified-6732907560/`](archive/2026-08-12-certified-6732907560/).

## 1. Imported analytic interface

Let $S=N_0^s(T,2T)$ and $N=N(T,2T)$. The predecessor framework supplies

$$
S\ge HN+\Delta(M)-o(N),
$$

together with the sharp finite-$m$ Gram profile

$$
h_m(E)=
\begin{cases}
E,&E\le m/(m-1),\\
E/m+2\sqrt{(m-1)E/m}-1,&E\ge m/(m-1).
\end{cases}
$$

These analytic ingredients remain imported.

## 2. Current 11-term window

The discovery window is

$$
v(s)=\sum_{j=0}^{10}c_j\cos(\omega_js),
$$

with $\omega_0=\sqrt2$, $\omega_j=2j\pi$ for $1\le j\le10$, and

```text
(c_j * 1e9) =
1000000000,
8421762,
-9816829,
1448046,
1412305,
-2228329,
2374999,
-4885560,
8393483,
-3137216,
2381462
```

High-precision evaluation gives

$$
H(v)=0.6723307581635602536\ldots,
$$

and the conditional arithmetic projection uses

$$
H_{\rm floor}=0.6723307.
$$

## 3. Local seven-point discovery target

For six nonnegative consecutive gaps and the existing pair/position-pressure layout, adversarial lattice enumeration plus local polishing currently finds

$$
\min F(g)\approx0.00540611079920.
$$

The proposed interval-certification target is

$$
\varepsilon=0.005405.
$$

This statement is currently a **target**, not a certified inequality.

The position-pressure coefficients retain exact total

$$
B=\sum_{r=1}^6b_r=\frac3{1150}.
$$

## 4. Exact pressure multiplicity

For an $m$-point block, sum the seven-point inequality over the $m-6$ local windows. Exact double counting gives total pressure charge

$$
(m-6)B.
$$

Under the shifted-block average, this is retained exactly rather than replaced by the coarser $B(m-1)$ charge.

## 5. Spectral conversion

Conditionally on a proof of the local target, set

$$
A_m=\varepsilon(m-6),\qquad R_m=h_m(A_m),\qquad \eta_m=R_m/A_m.
$$

Then the same block-defect argument gives

$$
\Delta(M)\ge\frac{R_m}{m}S-\frac{\eta_mB(m-6)}{m}N-o(N),
$$

and hence

$$
\frac SN\ge\frac{mH-\eta_mB(m-6)}{m-R_m}-o(1).
$$

## 6. Conditional projection

Using

$$
H=0.6723307,\qquad \varepsilon=0.005405,\qquad B=3/1150,
$$

the integer scan selects

$$
m=204
$$

and gives

$$
\frac SN\gtrsim0.6733300852750384514\ldots,
$$

with decimal floor `0.6733300852`, **conditional on certification of the local target**.

Using the floating-point discovery values directly gives approximately

$$
0.673330866624887\ldots=67.3330866625\ldots\%.
$$

## Status gate

Promotion from discovery candidate to certified research-draft result requires a rigorous interval proof of

$$
F(g_1,\ldots,g_6)\ge0.005405\qquad(g_i\ge0)
$$

for the exact 11-term rational window and recorded pair/pressure data. Until that gate is closed, the archived 67.3290756019% record remains the latest interval-certified research-draft result.
