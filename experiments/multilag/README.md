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

but do not keep the old pressure shape. At that exact total, adversarial exchange optimizes the reflection-symmetric position-pressure distribution.

The resulting exact vector is

\[
\frac1{230000000000}
(138257404,
191681784,
228060812,
228060812,
191681784,
138257404).
\]

Its entries are nonnegative and sum exactly to \(279/57500\).

The optimization used semi-infinite LP exchange against the dangerous basins, followed by unscreened polishing of all \(4^6=4096\) resonance templates. After quantization, the robust floating minimum is

\[
\boxed{0.00902172205332521\ldots}
\]

near

\[
(1.036097587833,
1.038002793236,
1.965416856027,
1.045335923444,
1.967453357559,
1.040665593176).
\]

Six multi-range differential-evolution stress runs did not find a lower value; one converged to the same lowest basin.

The proposed rigorous auxiliary target is

\[
\boxed{\varepsilon_1=0.0090210}.
\]

If this interval target closes, summing translated auxiliary inequalities gives

\[
\boxed{
S+\frac65P\ge A_1,
\qquad
A_1=\varepsilon_1(m-6).
}
\]

Together with the root inequality

\[
S+P\ge A_0,
\]

we obtain two supporting lines in the \((S,P)\)-plane.

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

The largest block for which the two supporting lines remove the Gram loss completely is

\[
\boxed{m=312},
\qquad n=m-6=306.
\]

At this block length,

\[
A_0=0.0079107\times306
=\frac{12103371}{5000000}
=2.4206742,
\]

and, conditional on the auxiliary target,

\[
A_1=0.009021\times306
=\frac{1380213}{500000}
=2.760426.
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
=\frac{451197}{625000}
=0.7219152.
\]

Crucially,

\[
S_*<\frac76.
\]

### Region 1: \(0\le S\le S_*\)

The root supporting line is active and the banded profile is linear, hence

\[
g(S)+P
\ge S+(A_0-S)
=A_0.
\]

### Region 2: \(S_*\le S\le A_1\)

The auxiliary pressure line is active. The function

\[
g(S)+\frac56(A_1-S)
\]

is concave, so its minimum occurs at an endpoint. At \(S=S_*\) it equals \(A_0\). At \(S=A_1\), it equals \(g(A_1)\), and exact arithmetic proves

\[
g(A_1)>A_0
\]

through the square witness

\[
\frac76A_1-
\left(\frac{A_0+7/6}{2}\right)^2
=
\frac{2919038927231}{900000000000000}>0.
\]

### Region 3: \(S\ge A_1\)

Here \(P\ge0\), and monotonicity gives

\[
g(S)\ge g(A_1)>A_0.
\]

Therefore, conditional on the auxiliary certificate and the banded-Gram profile,

\[
\boxed{\Delta+P\ge A_0}.
\]

Equivalently,

\[
\boxed{R=A_0,\qquad\eta=1.}
\]

The scalar Gram discount disappears completely at \(m=312\).

This endpoint is genuine rather than a scan cutoff: for the same exact targets, the corresponding square condition is already negative at \(m=313\). Thus \(m=312\) is the last block in the full no-loss regime.

## Conditional exact projection

Using the already interval-certified

\[
H>0.6721881580,
\qquad
B=\frac{93}{23000},
\]

and \(R=A_0,\eta=1\), the shifted-block expression is

\[
\frac{mH-B(m-6)}{m-A_0}
=
\frac{199798509242}{296680187225}
\]

\[
=0.6734474287306362\ldots.
\]

Hence, **conditional on** the auxiliary interval certificate and independent acceptance of the banded-Gram analytic profile, this construction gives

\[
\boxed{67.3447428731\ldots\%}
\]

with safe decimal floor

\[
\boxed{0.6734474287}.
\]

That is about **0.003094 percentage points** above the current root scalar-Gram record 67.3416490971%.

## Certification strategy

The auxiliary analytic window is identical to the root 17-term window. Only the pressure coefficients change. A previously launched auxiliary workflow has already generated outward-rounded tables for this exact window; the optimized auxiliary pressure target requires no wider table range. The strict verifier can therefore reuse those tables and recompile only the exact auxiliary coefficients.

Exact conditional arithmetic is checked by

```bash
python3 src/check_multilag.py
```

The result must not replace the root record unless both conditions hold:

1. `epsilon_1 = 0.0090210` returns `VERIFIED=true` in the hardened interval verifier;
2. the continuous banded-Gram profile and its insertion into shifted-block pinching pass independent mathematical review.
