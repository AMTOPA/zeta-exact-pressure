# Two-certificate multi-lag experiment

Status: **auxiliary local interval certification in progress**. This experiment also depends on the continuous banded-Gram analytic profile in `experiments/banded-gram/`, which is under independent review in issue #5.

## Motivation

A single translated local certificate is compressed to

\[
S+P\ge A_0,
\qquad
S:=E_1+\cdots+E_6,
\]

where \(P=B\,\operatorname{span}(B)\). Even after replacing the unrestricted scalar Gram profile by the stronger six-band profile, this one constraint allows a large part of the lower bound to be paid by the pressure term.

The goal here is to add one independent lag-weighted inequality that restricts that tradeoff.

## Base certificate

The root interval-certified 17-term certificate gives

\[
S+P\ge A_0,
\qquad
A_0=\varepsilon_0(m-6),
\qquad
\varepsilon_0=0.0079107.
\]

## Odd/even tilted certificate

Keep the same analytic window and the same position-pressure vector, but multiply every odd pair span by

\[
1+\delta=\frac{26}{25}
\]

and every even pair span by

\[
1-\delta=\frac{24}{25},
\qquad \delta=\frac1{25}.
\]

The exact per-span capacities are therefore

\[
2.08,\ 1.92,\ 2.08,\ 1.92,\ 2.08,\ 1.92.
\]

All pair coefficients are stored exactly over denominator \(25\cdot10^9\) in `candidate.json`.

Unscreened polishing of all \(4^6=4096\) resonance templates gives the current floating minimum

\[
0.00794501634934098\ldots
\]

near

\[
(1.045569055916,
 1.979587403541,
 1.051588313705,
 2.919045694850,
 1.048163136758,
 1.044664917907).
\]

The interval target being tested is

\[
\boxed{\varepsilon_1=0.0079445}.
\]

If it closes, the translated auxiliary inequality is

\[
\frac{26}{25}E_{\rm odd}
+\frac{24}{25}E_{\rm even}
+P
\ge A_1,
\qquad
A_1=\varepsilon_1(m-6).
\]

Since

\[
E_{\rm odd}-E_{\rm even}\le
E_{\rm odd}+E_{\rm even}=S,
\]

we obtain the weaker but scalar consequence

\[
\boxed{
\frac{26}{25}S+P\ge A_1.
}
\]

Together with the base inequality this supplies two distinct supporting lines in the \((S,P)\)-plane.

## Combination with the continuous banded profile

Let \(g=g_6\) be the continuous profile from `experiments/banded-gram/`:

\[
g(S)=
\begin{cases}
S,&S\le7/6,\\
2\sqrt{\frac76S}-\frac76,&S\ge7/6.
\end{cases}
\]

For fixed \(m\), the two local inequalities imply

\[
P\ge
\max\left(
A_0-S,
A_1-\frac{26}{25}S,
0
\right).
\]

The first two affine lower bounds intersect at

\[
S_*=25(A_1-A_0).
\]

For the selected \(m=173\),

\[
A_0=\frac{13210869}{10000000}=1.3210869,
\]

\[
A_1=\frac{2653463}{2000000}=1.3267315,
\]

and

\[
S_*=\frac{28223}{200000}=0.141115<\frac76.
\]

Take the rational profile floor

\[
R=\frac{131628967}{100000000}=1.31628967.
\]

The exact square witness

\[
\frac76A_0-
\left(\frac{R+7/6}{2}\right)^2
=
\frac{2718616199}{360000000000000000}>0
\]

proves \(R<g(A_0)\).

Choose

\[
\eta=\frac{R-S_*}{A_0-S_*}
=\frac{117517467}{117997190}.
\]

At \(S=S_*\), the base pressure line gives exactly

\[
g(S_*)+\eta(A_0-S_*)=R,
\]

because \(S_*<7/6\) and hence \(g(S_*)=S_*\). At \(S=0\), exact arithmetic gives \(\eta A_1>R\), and at \(S=A_0\), the square witness gives \(g(A_0)>R\).

On each interval cut out by \(0,S_*,A_0\), the function `g(S) + eta * (active affine pressure line)` is concave, so its minimum occurs at an endpoint. Consequently, conditional on the auxiliary local certificate,

\[
\boxed{
\Delta+\eta P\ge R.
}
\]

## Conditional exact projection

Using

\[
H>0.6721881580,
\qquad
B=\frac{93}{23000},
\qquad
m=173,
\]

the shifted-block expression is exactly

\[
\frac{mH-\eta B(m-6)}{m-R}
=
\frac{93944445751924037}{139502543089048315}
\]

\[
=0.6734246105603732\ldots.
\]

Thus, **if** the auxiliary target `0.0079445` closes and **if** the banded-Gram analytic profile passes independent review, the two-certificate multi-lag construction yields

\[
\boxed{67.3424610560\ldots\%}
\]

with safe floor

\[
\boxed{0.6734246105}.
\]

This is not a root record yet. The exact arithmetic is checked by

```bash
python3 src/check_multilag.py
```

while the auxiliary interval computation is run by `.github/workflows/multilag-certificate.yml`.
