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

Its scalar Fenchel conjugate on `x>=-1` satisfies

\[
\phi^*(a)=
\begin{cases}
-a-1,&a<-2,\\
a^2/4,&-2\le a\le2,\\
+\infty,&a>2,
\end{cases}
\]

and hence, for every `a<=2`,

\[
\phi^*(a)\le a^2/4.
\]

By spectral Fenchel duality, every Hermitian `A<=2I` therefore gives

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

The operator-norm bound implies `A<=2I`.  If `X=Y+Z`, where `Z` contains the
diagonal and all entries farther than `q`, then `Y` and `Z` are Frobenius
orthogonal and `tr Y=0`.  Consequently

\[
\operatorname{tr}(AX)
=2\alpha E-d\operatorname{tr}X
\ge2\alpha E,
\]

while

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

this maximizer lies on the asserted branch.  Substitution, using
`rho^2=E/T`, gives

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

This numerical gain is intentionally small: the purpose of the test is to
isolate and validate the finite-`m` trace correction before attempting stronger
matrix refinements.
