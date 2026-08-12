# Banded-Gram analytic extension

Status: **analytic-extension research candidate**. The local 17-term six-gap certificate used here is interval-certified. The new matrix profile below is an analytic step and should receive independent human review before this experiment replaces the root certified record.

## Why this direction

The predecessor compresses all off-diagonal Gram information into

\[
E=2\sum_{i<j}|G_{ij}|^2
\]

and then applies the sharp unrestricted profile \(\Delta\ge h_m(E)\), where \(\Delta=\operatorname{tr}\Psi(G)\). Because \(h_m\) is sharp when only total energy is retained, repeatedly tuning the local window cannot remove that loss.

The translated seven-point certificate contains stronger information: it uses only pair spans at most six. Define

\[
E_q=2\sum_{1\le j-i\le q}|G_{ij}|^2.
\]

For the present certificate, \(q=6\). Exact span capacities equal to 2 imply after summing translated local inequalities

\[
E_6+B\,\operatorname{span}(B)\ge A,
\qquad A=\varepsilon(m-6),
\]

without first relaxing \(E_6\) to total off-diagonal energy.

## Continuous banded-Gram profile

Let \(G\succeq0\) be Hermitian and let

\[
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
\]

Set

\[
T_q=\frac{q+1}{q}.
\]

Then the proposed strengthened profile is

\[
\boxed{
\operatorname{tr}\Psi(G)\ge g_q(E_q)
}
\]

with

\[
g_q(E)=
\begin{cases}
E,&0\le E\le T_q,\\[1mm]
2\sqrt{T_qE}-T_q,&E\ge T_q.
\end{cases}
\]

The function \(g_q\) is increasing, concave, continuous, \(C^1\) at \(T_q\), and satisfies \(g_q(0)=0\).

### Proof

Write

\[
G-I=Y+Z,
\]

where \(Y\) contains exactly the off-diagonal entries with \(1\le|i-j|\le q\), and \(Z\) contains the diagonal and all farther entries. Their Frobenius supports are disjoint, so

\[
\|Y\|_F^2=E_q,
\qquad
\|G-I\|_F^2=E_q+\|Z\|_F^2.
\]

For a unit vector \(x\), put \(p_i=|x_i|^2\). Color indices by residue modulo \(q+1\). Every q-band edge joins different colors. If \(P_c\) denotes total \(p_i\)-mass in color class \(c\), then

\[
\sum_{1\le j-i\le q}p_ip_j
\le
\sum_{c<d}P_cP_d
=\frac12\left(1-\sum_cP_c^2\right)
\le\frac{q}{2(q+1)}.
\]

Cauchy--Schwarz gives

\[
|x^*Yx|^2
\le E_q\frac{q}{q+1}.
\]

Hence

\[
\|Y\|_{\rm op}\le C,
\qquad
C:=\sqrt{\frac{q}{q+1}E_q}
=\sqrt{\frac{E_q}{T_q}}.
\]

Now use the eigenvalue identity

\[
\Psi(\lambda)
=(\lambda-1)^2-(\lambda-2)_+^2,
\]

which yields

\[
\Delta:=\operatorname{tr}\Psi(G)
=\|G-I\|_F^2-\|(G-2I)_+\|_F^2.
\]

If \(C\le1\), then \(Y-I\preceq0\). Since the Frobenius norm of the positive part is the distance to the cone of negative-semidefinite matrices,

\[
\|(G-2I)_+\|_F\le\|Z\|_F,
\]

so \(\Delta\ge E_q\).

If \(C>1\), put \(\alpha=C^{-1}\). Then \(\alpha Y-I\preceq0\) and

\[
G-2I=(\alpha Y-I)+\bigl(Z+(1-\alpha)Y\bigr).
\]

Again using distance to the negative-semidefinite cone and Frobenius orthogonality of \(Y\) and \(Z\),

\[
\|(G-2I)_+\|_F^2
\le
\|Z\|_F^2+(1-\alpha)^2E_q.
\]

Therefore

\[
\Delta
\ge
E_q\bigl(1-(1-\alpha)^2\bigr)
=E_q(2\alpha-\alpha^2).
\]

Substituting \(\alpha=\sqrt{T_q/E_q}\) gives

\[
\Delta\ge2\sqrt{T_qE_q}-T_q.
\]

This proves the displayed continuous profile.

## Pressure combination

The translated local certificate gives

\[
E_q+P\ge A,
\qquad P=B\,\operatorname{span}(B)\ge0.
\]

Set

\[
R=g_q(A),
\qquad
\eta=\frac{R}{A}.
\]

Because \(g_q\) is increasing, concave, and vanishes at zero, for \(E_q\le A\)

\[
g_q(E_q)\ge\frac{E_q}{A}g_q(A)=\eta E_q,
\]

while for \(E_q\ge A\), \(g_q(E_q)\ge R\). Hence in all cases

\[
\boxed{
\Delta+\eta P\ge R.
}
\]

This is exactly the form required by the predecessor shifted-block/pinching step, but with \(h_m(A)\) replaced by the stronger banded profile \(g_q(A)\).

## Interval-certified local input

The second-exchange 17-term local certificate has closed in the hardened outward-rounded verifier:

\[
H>0.6721881580,
\qquad
\varepsilon=0.0079107,
\qquad
B=\frac{93}{23000}.
\]

Evidence:

```text
workflow run = 31610179703
artifact id = 9147378469
artifact digest sha256 = 871532c739d5a9e8de770cf00675381ea4fd9c81f212d8e46f86403a27a34dc1
VERIFIED=true
nodes=3768186
pruned=1884125
splits=1884061
convex=2030240
tangent=936616
max_depth=74
```

## Exact projection

The strengthened profile changes the optimal block length to

\[
\boxed{m=165}.
\]

With \(q=6\),

\[
A=0.0079107\times159
=1.2578013
=\frac{12578013}{10000000},
\]

and

\[
T_6=\frac76.
\]

Instead of using a floating square root in the final statement, take the rational lower floor

\[
R_{\rm floor}=1.2560878
=\frac{6280439}{5000000}.
\]

The exact checker proves

\[
R_{\rm floor}<2\sqrt{T_6A}-T_6
\]

by the rational square inequality

\[
T_6A-\left(\frac{R_{\rm floor}+T_6}{2}\right)^2
=
\frac{43705511}{900000000000000}>0.
\]

Thus

\[
\eta=\frac{R_{\rm floor}}A
=\frac{12560878}{12578013}.
\]

The shifted-block arithmetic becomes

\[
\frac SN\ge
\frac{mH-\eta B(m-6)}{m-R_{\rm floor}}-o(1),
\]

and evaluates exactly to

\[
\frac{607970185271419}{902805037076740}
=0.6734235635636362491098136775718\ldots.
\]

Therefore this analytic extension projects to

\[
\boxed{67.34235635636362\ldots\%},
\]

with safe ten-decimal floor

\[
\boxed{0.6734235635}.
\]

This is about **0.00082496 percentage points** above the current root record 67.3415313957%.

## Geometry checks

A first 7-point/8-point mixture experiment was also carried out. Under a common analytic window, the pair-capacity constraint forces the mixture coefficients to form a convex combination, and the scalar \(A_m\to h_m(A_m)\) projection selected an endpoint rather than an interior mixture. That negative result is what motivated retaining band position information instead of mixing geometries before the scalar Gram compression.

A preliminary five-gap experiment was also tested because \(T_5=6/5\) is larger than \(T_6\). Free pair/pressure LPs initially overfit badly; after adversarial exchange, the robust local minima fell well below the level needed to beat the six-gap construction. At present \(q=6\) appears to be the better geometry for this banded profile.

## Reproduce exact arithmetic

```bash
python3 src/check_banded_gram.py
```

The same check is wired into `sh run.sh` and normal arithmetic CI.

## Trust boundary

The 17-term local inequality and its window floor are interval-certified. The arithmetic from the banded profile to the displayed rational bound is exact. The genuinely new step is the continuous banded-Gram matrix inequality and its use inside the predecessor shifted-block/pinching argument. That analytic extension should receive independent human review before root promotion.
