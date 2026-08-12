# Two-supporting-line energy-pressure experiment

Status: **optimized auxiliary local interval certification pending**. This experiment also depends on the continuous banded-Gram analytic profile in `experiments/banded-gram/`, which is under independent review in issue #5.

## Why this changes the bottleneck

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
B=\frac{93}{23000},
\qquad
A_0=\varepsilon_0(m-6).
\]

A single supporting line permits the block argument to trade band energy against pressure in the configuration that produces the scalar Gram discount. The new strategy is not to squeeze the same certificate further, but to add a **second local certificate with a different energy-pressure slope**.

## Optimized auxiliary certificate

Keep exactly the same interval-certified 17-term analytic window and exactly the same pair weights as the root certificate. Increase the **total** auxiliary position pressure to

\[
\frac65 B=\frac{279}{57500},
\]

then adversarially optimize the reflection-symmetric distribution at that exact total. The exact vector is

\[
\frac1{230000000000}
(138257404,
191681784,
228060812,
228060812,
191681784,
138257404).
\]

Unscreened polishing of all \(4^6=4096\) resonance templates, followed by six multi-range differential-evolution runs, gives a robust floating minimum

\[
\boxed{0.00902172205332521\ldots}.
\]

The strict target is deliberately **not** pushed to that floating optimum. At the globally selected block \(m=312\), the exact no-Gram-loss condition only requires approximately

\[
\varepsilon_1>0.009011915.
\]

We therefore target

\[
\boxed{\varepsilon_1=0.009015},
\]

leaving about \(6.72\times10^{-6}\) floating margin while preserving exactly the same final projection. This is a certifiability-directed target rather than a local-record target.

If it closes, summing translated auxiliary inequalities gives

\[
\boxed{
S+\frac65P\ge A_1,
\qquad
A_1=\varepsilon_1(m-6).
}
\]

Together with \(S+P\ge A_0\), this gives two supporting lines in the \((S,P)\)-plane.

## Combine with the continuous banded profile

Use

\[
g(S)=
\begin{cases}
S,&S\le7/6,\\[1mm]
2\sqrt{\frac76S}-\frac76,&S\ge7/6.
\end{cases}
\]

from `experiments/banded-gram/`. The largest full no-Gram-loss block for the exact target above is

\[
\boxed{m=312},\qquad n=306.
\]

Then

\[
A_0=0.0079107\times306
=\frac{12103371}{5000000}
=2.4206742,
\]

\[
A_1=0.009015\times306
=\frac{275859}{100000}
=2.75859.
\]

The pressure lower bounds

\[
P\ge A_0-S,
\qquad
P\ge\frac56(A_1-S)
\]

intersect at

\[
S_*=\frac{(6/5)A_0-A_1}{1/5}
=\frac{913869}{1250000}
=0.7310952
<\frac76.
\]

For \(0\le S\le S_*\), the root line is active and \(g(S)=S\), so \(g(S)+P\ge A_0\). For \(S_*\le S\le A_1\), the auxiliary line is active and

\[
g(S)+\frac56(A_1-S)
\]

is concave, so its minimum occurs at an endpoint. At \(S_*\) it is \(A_0\); at \(A_1\), exact arithmetic proves \(g(A_1)>A_0\) via

\[
\frac76A_1-
\left(\frac{A_0+7/6}{2}\right)^2
=
\frac{991238927231}{900000000000000}>0.
\]

For \(S\ge A_1\), monotonicity gives the same conclusion. Therefore, conditional on the auxiliary certificate and the banded-Gram profile,

\[
\boxed{\Delta+P\ge A_0},
\qquad
\boxed{R=A_0,\ \eta=1}.
\]

At \(m=313\) the exact endpoint square witness is already negative,

\[
-\frac{9309444857209}{3600000000000000}<0,
\]

so \(m=312\) is a genuine analytic boundary rather than a scan cutoff.

## Conditional exact projection

Using the already interval-certified

\[
H>0.6721881580,
\qquad B=\frac{93}{23000},
\]

we obtain exactly

\[
\frac{mH-B(m-6)}{m-A_0}
=
\frac{199798509242}{296680187225}
=0.6734474287306362\ldots.
\]

Thus, **conditional on** auxiliary interval closure and independent acceptance of the banded-Gram profile,

\[
\boxed{67.3447428731\ldots\%}
\]

with safe decimal floor

\[
\boxed{0.6734474287}.
\]

That is about **0.003094 percentage points** above the current root scalar-Gram record 67.3416490971%.

## Beyond a single auxiliary line

The deeper direction is now clear: certificates of the form

\[
S+cP\ge A(c)
\]

are supporting lines for the local energy-pressure feasible region. A small bundle of rigorously certified scales can approximate that frontier piecewise and extend the range where the Gram discount disappears.

Current numerical exploration finds a stronger single-line scale near \(c\approx1.6\), and combining several scales (for example \(1,1.2,1.6\), with a later \(2.0\) line) pushes the conditional no-loss block farther than any one auxiliary line. These higher-scale lines remain discovery work until separately interval-certified.

## Certification strategy

The auxiliary analytic window is identical to the root 17-term window, so the strict verifier reuses the already certified root outward-rounded kernel tables and recompiles only the exact auxiliary pressure coefficients. The verifier independently checks the required table range.

Exact conditional arithmetic is checked by

```bash
python3 src/check_multilag.py
```

The result must not replace the root record unless both conditions hold:

1. `epsilon_1 = 0.009015` returns `VERIFIED=true` in the hardened interval verifier;
2. the continuous banded-Gram profile and its insertion into shifted-block pinching pass independent mathematical review.
