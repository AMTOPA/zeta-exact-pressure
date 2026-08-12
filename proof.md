# Proof outline

This file records the new deduction and parameters. It is deliberately explicit about what is imported.

## 1. Imported analytic interface

Let $S=N_0^s(T,2T)$ and $N=N(T,2T)$. The predecessor framework supplies an inequality of the form

$$
S\ge H_{\rm cert}N+\Delta(M)-o(N),
$$

together with the sharp finite-$m$ Gram profile

$$
h_m(E)=
\begin{cases}
E,&E\le m/(m-1),\\
E/m+2\sqrt{(m-1)E/m}-1,&E\ge m/(m-1).
\end{cases}
$$

These analytic ingredients are imported.

## 2. Local seven-point certificate

For the window and pair/pressure weights recorded in `candidate.json`, the current interval computation certifies

$$
F(g_1,\ldots,g_6)\ge\varepsilon,\qquad \varepsilon=\frac{52289}{10^7}.
$$

The pressure weights $b_1,\ldots,b_6$ satisfy

$$
B=\sum_{r=1}^6b_r=\frac3{1150}.
$$

## 3. Exact pressure multiplicity

For an $m$-point block, sum the seven-point inequality over the $m-6$ local windows. If $c_j$ is the total pressure coefficient carried by the $j$-th internal gap, then exact double counting gives

$$
\sum_{j=1}^{m-1}c_j=(m-6)B.
$$

A fixed global gap, over all $m$ shifted block partitions, visits every internal position exactly once. Thus the shifted average retains the exact pressure charge $(m-6)B$, rather than replacing it by a coarse $B(m-1)$.

## 4. Spectral conversion

Set

$$
A_m=\varepsilon(m-6),\qquad R_m=h_m(A_m),\qquad \eta_m=R_m/A_m.
$$

The local certificate and the Gram profile give the block defect lower bound with pressure coefficient $\eta_m$. Averaging the $m$ shifted partitions yields

$$
\Delta(M)\ge\frac{R_m}{m}S-\frac{\eta_mB(m-6)}{m}N-o(N).
$$

Substitute into the imported counting inequality:

$$
S\ge H_{\rm cert}N+\frac{R_m}{m}S-\frac{\eta_mB(m-6)}{m}N-o(N).
$$

Solving for $S/N$,

$$
\boxed{\frac SN\ge\frac{mH_{\rm cert}-\eta_mB(m-6)}{m-R_m}-o(1).}
$$

## 5. New window

The window is

$$
v(s)=\sum_{j=0}^6c_j\cos(\omega_js)
$$

with

$$
(c_0,\ldots,c_6)=10^{-9}(1000000000,6907835,-9359173,528441,1509267,-4923883,1358707).
$$

Its computed analytic value is

$$
H(v)=0.67240570242660302900695918\ldots,
$$

and we use

$$
H_{\rm cert}=0.6724057.
$$

## 6. Final arithmetic

With

$$
\varepsilon=0.0052289,\qquad B=3/1150,
$$

the integer scan selects

$$
m=210.
$$

Then

$$
A_{210}=1.0666956,
$$

$$
R_{210}=1.0657746255211988006371517667\ldots,
$$

and

$$
\eta_{210}=0.9991366098455818141906198607\ldots.
$$

Therefore

$$
\frac SN\ge0.6732907560192226357616716519\ldots-o(1),
$$

hence safely

$$
\boxed{\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}>0.6732907560.}
$$

## Status

The final arithmetic and exact pressure deduction are elementary once the imported analytic interface and local interval certificate are accepted. The new local certificate should be independently reproduced before this candidate is treated as an established theorem.
