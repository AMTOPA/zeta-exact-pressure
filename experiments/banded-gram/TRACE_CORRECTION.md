# Trace-corrected finite-m banded-Gram profile

Status: **new analytic lemma under review**.  This is a finite-`m` strengthening
of the continuous banded-Gram profile in `README.md`.  It uses no new local
numerical assumptions, but it is a new matrix-analytic step and must not be
promoted to the root result without independent review.

## Statement

Let `G` be an `m x m` Hermitian positive-semidefinite Gram matrix with
`G_ii <= 1`, put `X=G-I`, and let `Y` be the off-diagonal `q`-band part of
`X`.  Write

\[
E=\|Y\|_F^2
 =2\sum_{1\le j-i\le q}|G_{ij}|^2,
\qquad
T=\frac{q+1}{q}.
\]

Then the proposed finite-dimensional profile is

\[
\boxed{
\operatorname{tr}\Psi(G)\ge g^{\rm tr}_{q,m}(E)
}
\]

with

\[
g^{\rm tr}_{q,m}(E)=
\begin{cases}
E,&0\le E\le T,\\[2mm]
\displaystyle
\frac{E+m\left(2\sqrt{E/T}-1\right)}{1+m/T},
&E\ge T.
\end{cases}
\]

It agrees with the original banded profile in the linear region, is strictly
stronger for finite `m` in the nonlinear region, and decreases to the original
profile

\[
2\sqrt{TE}-T
\]

as `m -> infinity`.

## Proof

For an eigenvalue `lambda >= 0`, set `x=lambda-1 >= -1` and

\[
\phi(x)=\Psi(x+1)
=x^2-(x-1)_+^2.
\]

Thus `phi(x)=x^2` on `[-1,1]` and `phi(x)=2x-1` on `[1,infinity)`.
Taking the supremum of `ax-phi(x)` on these two intervals gives the scalar
Fenchel conjugate

\[
\phi^*(a)=
\begin{cases}
-a-1,&a<-2,\\
a^2/4,&-2\le a\le2,\\
+\infty,&a>2.
\end{cases}
\]

Indeed, for `-2<=a<=2` the stationary point `x=a/2` lies in `[-1,1]`,
while for `a<-2` the constrained maximizer is the endpoint `x=-1`; for
`a>2` the linear tail makes the supremum infinite.  In particular, for every
`a<=2`,

\[
\phi^*(a)\le a^2/4,
\]

because on `a<-2` this is exactly
`a^2/4-(-a-1)=(a+2)^2/4>=0`.

For completeness, the matrix Fenchel step does **not** require `A` and `X` to
commute.  Let `x_1<=...<=x_m` and `a_1<=...<=a_m` be their eigenvalues.
Von Neumann's trace inequality gives

\[
\operatorname{tr}(AX)\le\sum_{i=1}^m a_i x_i.
\]

Scalar Fenchel applied termwise gives

\[
a_i x_i\le \phi(x_i)+\phi^*(a_i).
\]

Hence every Hermitian `A` whose eigenvalues satisfy `a_i<=2` obeys

\[
\operatorname{tr}\phi(X)
\ge \operatorname{tr}(AX)-\operatorname{tr}\phi^*(A)
\ge \operatorname{tr}(AX)-\frac14\|A\|_F^2.
\]

Since `G` is positive semidefinite, every eigenvalue of `X=G-I` is at least
`-1`, so the scalar domain condition used above is automatic.  Therefore every
Hermitian `A<=2I` gives

\[
\operatorname{tr}\Psi(G)
=\operatorname{tr}\phi(X)
\ge \operatorname{tr}(AX)-\frac14\|A\|_F^2.
\]

As in the banded-Gram proof, coloring indices modulo `q+1` gives

\[
\|Y\|_{\rm op}
\le \rho:=\sqrt{E/T}.
\]

Explicitly, for a unit vector `u`, put `p_i=|u_i|^2` and let `P_c` be the
`p_i`-mass in residue class `c mod (q+1)`.  Every `q`-band edge joins two
different classes, so

\[
2\sum_{1\le j-i\le q}p_ip_j
\le 1-\sum_c P_c^2
\le \frac{q}{q+1}.
\]

Cauchy--Schwarz in the edge sum then gives

\[
|u^*Yu|^2
\le
\left(2\sum_{1\le j-i\le q}|Y_{ij}|^2\right)
\left(2\sum_{1\le j-i\le q}p_ip_j\right)
\le E\frac{q}{q+1}=rac ET,
\]

which proves the operator-norm bound.

Now exploit the diagonal constraint that was unused in the first profile:

\[
\operatorname{tr}X
=\operatorname{tr}G-m\le0.
\]

For `alpha>=0`, choose

\[
A=2\alpha Y-dI,
\qquad
d=2(\alpha\rho-1)_+.
\]

The operator-norm bound implies

\[
\lambda_{\max}(A)
\le 2\alpha\rho-d\le2,
\]

so `A<=2I` as required.  If `X=Y+Z`, where `Z` contains the diagonal and all
entries farther than `q`, then `Y` and `Z` have disjoint Frobenius support and
`tr Y=0`.  Consequently

\[
\operatorname{tr}(AX)
=2\alpha\operatorname{tr}(YX)-d\operatorname{tr}X
=2\alpha E-d\operatorname{tr}X
\ge2\alpha E,
\]

while the vanishing trace of `Y` also removes the cross term in
`\|2\alpha Y-dI\|_F^2`, giving

\[
\frac14\|A\|_F^2
=\alpha^2E+\frac m4d^2.
\]

Thus

\[
\Delta:=\operatorname{tr}\Psi(G)
\ge
(2\alpha-\alpha^2)E
-m(\alpha\rho-1)_+^2.
\]

If `E<=T`, take `alpha=1`; then `rho<=1`, the last term vanishes, and
`Delta>=E`.

Assume `E>T`, so `rho>1`.  On the branch `alpha rho >=1`, the right-hand side
is a concave quadratic in `alpha`:

\[
-(E+m\rho^2)\alpha^2
+2(E+m\rho)\alpha-m.
\]

Its maximizer is

\[
\alpha_*=
\frac{E+m\rho}{E+m\rho^2}.
\]

Since

\[
\alpha_*\rho-1
=\frac{E(\rho-1)}{E+m\rho^2}>0,
\]

this maximizer lies on the asserted branch.  Its value is

\[
\frac{(E+m\rho)^2}{E+m\rho^2}-m
=
\frac{E\bigl(E+m(2\rho-1)\bigr)}{E+m\rho^2}.
\]

Substituting `rho^2=E/T` therefore gives

\[
\Delta\ge
\frac{E+m(2\sqrt{E/T}-1)}{1+m/T}.
\]

This proves the displayed profile.

## Shape

The nonlinear derivative is

\[
\frac{1+m/\sqrt{ET}}{1+m/T},
\]

so the function is increasing and concave.  At `E=T` its value and derivative
are `T` and `1`, respectively.  Hence the two pieces join `C^1`.

The same supporting-line logic used for the original `g_q` can therefore be
applied blockwise.  In particular, for a finite list of certified inequalities

\[
E+c_jP\ge A_j,
\]

one may minimize `g^{tr}_{q,m}(E)+P` over the resulting piecewise-linear
pressure envelope.  On each active affine pressure segment the objective is
concave, so its minimum occurs at a segment endpoint (including the linear /
nonlinear junction `E=T`).

## First test case: m=577

For the current root 17-term window and already certified pressure-frontier
lines, the old continuous banded profile misses full no-loss at `m=577` by a
small amount at the `c=21/20` / `c=6/5` switch.  The trace-corrected profile
reduces the deficit to the point that no reoptimization is needed: keeping the
same `c=21/20` coefficients and raising only its rigorous local target from
`0.008205` to `0.0082051` suffices.

The proposed test target remains well below the observed floating local minimum
`0.00820573038985...` for those exact coefficients.  `src/check_trace_banded_gram.py`
checks every frontier endpoint with rational arithmetic plus exact square
witnesses.  Conditional on that tiny local tightening and on acceptance of this
analytic lemma, it gives

\[
\boxed{m=577}
\]

and

\[
\boxed{
\frac{4433753022409}{6583554388450}
=0.6734588583618979155\ldots
}
\]

or `67.3458858362%`, with safe floor `0.6734588583`.

A later trace-only root-local tightening improves the numerical projection
without changing this matrix lemma; that experiment is recorded separately in
`trace-root-tightening.json` so that the original root record remains
untouched.

## Trust boundary

The derivation above is now self-contained at the matrix-inequality level: the
scalar conjugate, the noncommutative trace Fenchel step, the coloring bound,
and the finite-`m` optimization are all written explicitly.  The remaining
research trust boundary is external to this algebraic derivation: independent
review of the lemma and of its insertion into the predecessor shifted-block /
pinching framework is still required before any trace-corrected number is
promoted to the root result.
