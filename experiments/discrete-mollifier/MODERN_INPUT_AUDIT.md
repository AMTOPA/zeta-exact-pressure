# Modern input audit for the discrete-mollifier pivot

Status: research audit only; no theorem beyond the published `19/27` is claimed.

The active question is whether the Bui--Heath-Brown discrete mollified-`zeta'`
argument can be moved past mollifier length `y=T^theta`, `theta=1/2`, or whether a
genuinely independent second mollifier piece is the more realistic route.

## 1. Baseline to beat

Bui--Heath-Brown (arXiv:1302.5018) prove on RH that at least `19/27` of the
zeros are simple.  In the one-piece main-term model the exact variational curve is

\[
K(theta)=1-(1+theta)^{-3}.
\]

Thus 71% would require

\[
theta=0.510778053489\ldots.
\]

The published large-modulus analysis has the unsimplified power terms

\[
yT^{1/2},\qquad y^{1/2}T^{3/4},\qquad y^{1/3}T^{5/6},
\]

which all hit exponent `T^1` at `theta=1/2`.  At the 71% value of theta their
excess exponents are approximately

\[
0.01077805,\qquad0.00538903,\qquad0.00359268.
\]

Therefore a longer one-piece proof needs a simultaneous improvement of the
long/unbalanced and balanced regimes, not just a refinement of the final
`y^(1/3)T^(5/6)` term.

## 2. Benli--Elma--Ng: modern discrete mean values, but the same wall

Reference: K. Benli, E. Elma, N. Ng, *A discrete mean value of the Riemann zeta
function*, arXiv:2311.13554.

This work gives general discrete mean formulae over zeta zeros for Dirichlet
polynomials and for higher derivatives.  It is highly relevant because the target
object is genuinely discrete rather than a continuous `t`-average.

However, its general setup still takes Dirichlet-polynomial length below the
square-root barrier, and the unconditional large-modulus analysis produces the
same type of critical exponents (including terms of shapes `N*T^(1/2)`,
`N^(1/3)*T^(5/6)`, and another term critical at `N=T^(1/2)`).

**Decision:** this is the best modern template for reorganizing the discrete
calculation, but it is not a black-box theorem permitting `theta>1/2`.

## 3. Bettin--Chandee--Radziwill: enough continuous length, wrong averaging

Reference: S. Bettin, V. Chandee, M. Radziwill, *The mean square of the product
of zeta(s) with Dirichlet polynomials*, arXiv:1411.7764.

They prove an asymptotic for the continuous mean square of `zeta(s)` times an
arbitrary Dirichlet polynomial of length

\[
T^{1/2+0.01515\ldots}.
\]

Numerically, that extra length is already larger than the `0.010778...` needed by
the one-piece formal curve to cross 71%.

But a continuous critical-line integral is not the Bui--Heath-Brown residue sum
over zeta zeros.  The result cannot simply be substituted into the discrete
argument.

**Research use:** audit whether the Kloosterman-fraction / trilinear technology
behind this continuous theorem can replace one of the discrete long-factor losses.
Do not claim a transfer without deriving the residue-family transformation.

## 4. Modern sixth moments: relevant to the unbalanced regime

Reference: V. Chandee, X. Li, K. Matomaki, M. Radziwill, *The sixth moment of
Dirichlet L-functions at the central point*, arXiv:2409.01457.

This work removes an earlier auxiliary `t`-average from the sixth-moment problem.
Its authors emphasize difficult unbalanced character sums as the main new issue.
That is structurally close to the regime where the Bui--Heath-Brown proof uses a
pointwise long-factor estimate before the hybrid large sieve.

**Decision:** this is a methodological candidate for the `theta>1/2` project,
not a ready lemma.  The required compatibility audit is:

- modulus/conductor range;
- primitive-character weighting;
- Perron `t` variable and smoothing;
- additional `d,k` coefficients in `M_{nu,3}`;
- uniformity strong enough to save at least `T^-0.011` at `theta=0.511` in the
  worst long-factor regime.

If these cannot be matched, abandon the longer-one-piece route rather than
forcing a citation outside its hypotheses.

## 5. Parallel fallback: a genuine Feng k=2 arithmetic piece

The proposed `(mu, mu*Lambda)` vector direction is exactly redundant because

\[
(mu*Lambda)(n)=-mu(n)\log n.
\]

A Feng-type `k=2` coefficient instead contains the squarefree prime-factor statistic

\[
e_2(n)=\sum_{p<q\mid n}\log p\log q.
\]

In formal prime-log variables, `e_2` is the second elementary symmetric
polynomial and is not a polynomial in `e_1=log n` alone.  Thus it passes the
algebraic rank test.  Keeping the prefactor `mu(n)` also preserves squarefree
support, which is attractive for compatibility with the Bui--Heath-Brown
factorization/cleaning machinery.

Before proving any new off-diagonal estimates, derive the normalized mixed
first/second moments

\[
u=(u_0,u_1),\qquad
Q=\begin{pmatrix}q_{00}&q_{01}\\q_{10}&q_{11}\end{pmatrix}
\]

at `theta<1/2` and compute `u^*Q^{-1}u`.

The minimum incremental Rayleigh gains over `19/27` are exactly

\[
71\%:\ \frac{17}{2700},\qquad
72\%:\ \frac{11}{675},\qquad
73\%:\ \frac{71}{2700}.
\]

If the formal `k=2` mixed moments do not deliver a substantial fraction of these
gaps, stop before attempting a rigorous off-diagonal proof.

## 6. Current decision tree

1. **Longer one-piece route:** attempt a precise transformation of the BHB/Benli
   long-factor family into a setting amenable to modern unbalanced/spectral or
   Kloosterman technology.  Target only `theta=0.511` first.
2. **Feng k=2 route in parallel:** derive the formal mixed main terms at
   `theta=1/2-` and apply the exact Schur-complement go/no-go test.
3. Do not return to exact-pressure coefficient tightening unless a new analytic
   ingredient changes its information ceiling.
4. Do not promote any `>19/27` number until the corresponding new mean-value
   estimate is proved with all ranges and error terms checked.
