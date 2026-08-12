# Two-supporting-line energy-pressure experiment

Status: **auxiliary local interval certification pending**. This experiment also depends on the continuous banded-Gram analytic profile in `experiments/banded-gram/`, which is under independent review in issue #5.

## Why this is different from parameter squeezing

The root local certificate gives one block constraint

\[
S+P\ge A_0,
\qquad
S:=E_1+\cdots+E_6,
\qquad
P:=B\,\operatorname{span}(B),
\]

with

\[
\varepsilon_0=0.0079107,
\qquad
A_0=\varepsilon_0(m-6).
\]

A single supporting line permits the proof to trade band energy against pressure in a way that creates the familiar Gram discount. Instead of optimizing the same certificate again, this experiment adds a **second local inequality with a different energy-pressure slope**.

## Auxiliary pressure-scaled certificate

Keep exactly the same interval-certified 17-term analytic window and exactly the same pair weights, but multiply the entire position-pressure vector by

\[
\boxed{c=\frac65}.
\]

The auxiliary local functional therefore differs only in its linear pressure term. Its exact pressure total is

\[
\frac65\,B
=\frac{279}{57500}.
\]

Unscreened polishing of all \(4^6=4096\) resonance templates gives

\[
0.008999276423831326\ldots
\]

near

\[
(1.034964897995,
 1.038703956438,
 1.962587593105,
 1.039262172775,
 1.035733103346,
 1.961720338887).
\]

Six multi-range differential-evolution runs were all higher; the lowest was above `0.00905`.

The proposed rigorous target is

\[
\boxed{\varepsilon_1=0.0089985}.
\]

If the interval verifier closes this target, summing translated auxiliary inequalities gives

\[
\boxed{
S+\frac65 P\ge A_1,
\qquad
A_1=\varepsilon_1(m-6).
}
\]

Together with the root inequality

\[
S+P\ge A_0,
\]

this gives two supporting lines in the \((S,P)\)-plane.

## Combine with the continuous banded profile

Use the proposed six-band profile

\[
g(S)=
\begin{cases}
S,&S\le7/6,\\[1mm]
2\sqrt{\frac76S}-\frac76,&S\ge7/6.
\end{cases}
\]

from `experiments/banded-gram/`.

Choose

\[
\boxed{m=259},
\qquad n=m-6=253.
\]

Then

\[
A_0=0.0079107\times253
=\frac{20014071}{10000000}
=2.0014071,
\]

and, conditional on the auxiliary target,

\[
A_1=0.0089985\times253
=\frac{4553241}{2000000}
=2.2766205.
\]

The two pressure lower bounds

\[
P\ge A_0-S,
\qquad
P\ge\frac56(A_1-S)
\]

intersect at

\[
S_*=\frac{(6/5)A_0-A_1}{1/5}
=\frac{6253401}{10000000}
=0.6253401.
\]

Crucially,

\[
S_*<\frac76.
\]

### Region 1: \(0\le S\le S_*\)

The root supporting line is active and the banded profile is linear, so

\[
g(S)+P
\ge S+(A_0-S)
=A_0.
\]

### Region 2: \(S_*\le S\le A_1\)

The auxiliary line is active. The function

\[
g(S)+\frac56(A_1-S)
\]

is concave, so its minimum on this interval occurs at an endpoint. At \(S=S_*\) it equals \(A_0\). At \(S=A_1\), it equals \(g(A_1)\), and exact arithmetic proves

\[
g(A_1)>A_0
\]

via

\[
\frac76A_1-
\left(\frac{A_0+7/6}{2}\right)^2
=
\frac{528783848062631}{3600000000000000}>0.
\]

### Region 3: \(S\ge A_1\)

Here \(P\ge0\), and monotonicity gives

\[
g(S)\ge g(A_1)>A_0.
\]

Therefore the two supporting lines remove the Gram loss completely:

\[
\boxed{
\Delta+P\ge A_0.
}
\]

Equivalently,

\[
\boxed{R=A_0,\qquad \eta=1.}
\]

This is the central point of the experiment: the second certificate does not merely raise a local epsilon. It changes the **shape of the admissible energy-pressure region** enough to eliminate the scalar Gram discount at the selected block length.

## Conditional exact projection

Using the already interval-certified

\[
H>0.6721881580,
\qquad
B=\frac{93}{23000},
\]

and \(R=A_0\), \(\eta=1\), the shifted-block expression becomes

\[
\frac{mH-B(m-6)}{m-A_0}
=
\frac{86536866461}{128499296450}
\]

\[
=0.6734423366642487\ldots.
\]

Thus, **conditional on** the auxiliary interval certificate and independent acceptance of the banded-Gram analytic profile, the construction gives

\[
\boxed{67.3442336664\ldots\%}
\]

with safe decimal floor

\[
\boxed{0.6734423366}.
\]

That is about **0.002585 percentage points** above the current root scalar-Gram record 67.3416490971%.

## Certification strategy

The auxiliary window is identical to the root 17-term window. Only the pressure coefficients change. Moreover the pressure is scaled upward by \(6/5\), so the interval table range required by target `0.0089985` is actually *shorter* than the range required by the exploratory `0.0079445` auxiliary run already generating the shared kernel tables.

Therefore the next strict test reuses those outward-rounded tables and recompiles only the exact auxiliary coefficients.

Exact conditional arithmetic is checked by

```bash
python3 src/check_multilag.py
```

The result must not replace the root record unless both of the following hold:

1. the auxiliary local target returns `VERIFIED=true` in the hardened interval verifier;
2. the continuous banded-Gram profile and its insertion into shifted-block pinching pass independent mathematical review.
