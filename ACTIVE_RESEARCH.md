# Active research direction

Date: 2026-08-13

The primary research direction is now **discrete mollified moments of `zeta'(rho)`**, not further numerical tightening of the exact-pressure / pair-correlation construction.

The existing exact-pressure result remains the repository's current certified research-draft record and remains reproducible. Its optimization line is frozen unless a genuinely new analytic ingredient appears.

## Why the pivot

The pair-correlation / pressure / Gram route is showing strong diminishing returns and lies in the same broad information regime as substantially optimized pair-correlation methods. A different detector already has a stronger literature baseline: Bui--Heath-Brown prove on RH that at least

\[
\frac{19}{27}=70.370370\ldots\%
\]

of zeta zeros are simple.

The active experiment is under:

- `experiments/discrete-mollifier/README.md`
- `experiments/discrete-mollifier/one_piece.py`
- `experiments/discrete-mollifier/rayleigh2.py`

## First result of the pivot

The published Bui--Heath-Brown one-piece main terms can be optimized exactly. For mollifier length `y=T^theta`, the variational optimum over the full polynomial-smoothed `mu(n) P` class is

\[
\boxed{\kappa(\theta)=1-(1+\theta)^{-3}}.
\]

Thus the `19/27` endpoint is exactly the value at `theta=1/2`.

The initially proposed second basis `(mu, mu*Lambda)` is not independent because

\[
(\mu*\Lambda)(n)=-\mu(n)\log n.
\]

It is absorbed by polynomial smoothing and therefore cannot improve the variational space.

## Correct analytic bottleneck: a triple junction

For attempts to cross `theta=1/2`, one must use the unsimplified end-product of Bui--Heath-Brown's large-modulus argument:

\[
M_{\nu,3}\ll_\varepsilon
 yT^{1/2+\varepsilon}
 +y^{1/2}T^{3/4+\varepsilon}
 +y^{1/3}T^{5/6+\varepsilon}
 +\eta^{-1/2}T\mathcal L^C.
\]

With `y=T^theta`, the three power exponents are

\[
E_1=\theta+\frac12,\qquad
E_2=\frac\theta2+\frac34,\qquad
E_3=\frac\theta3+\frac56.
\]

All three equal `1` at `theta=1/2`. Hence the length wall is **not** a single `y^(1/3)T^(5/6)` obstruction: it is a triple junction involving the long-factor Pólya--Vinogradov regime and both branches of the two-block hybrid-large-sieve argument.

Concrete milestones from the exact variational curve:

- 71% requires `theta > 0.5107780535`;
- 72% requires `theta > 0.5285535437`;
- 73% requires `theta > 0.5471962779`.

At the 71% theta, the published exponents exceed `T^1` by respectively

\[
0.01077805,\qquad0.00538903,\qquad0.00359268.
\]

Any genuine 71% proof therefore needs a power saving in all active regimes; the largest missing saving is in the long-factor term.

## Current main problem

The Bui--Heath-Brown hard family is a weighted primitive-character sum with total Dirichlet length

\[
X=\frac{KQT}{\pi D},\qquad KQ\ll y,\quad D\le K,
\]

and, after Perron, a family integral

\[
T(Q,V)=\sum_{q\asymp Q}\sum_{\psi\bmod q}^{*}
\int_{-V}^{V}|H_1(\psi,t)\cdots H_9(\psi,t)|\,dt.
\]

Modern sixth-moment theorems are not a black-box match: their conductor, smoothing, and `t`-averaging hypotheses differ. The promising point is methodological instead. Modern work on the sixth moment at the central point handles precisely the difficult **unbalanced** character sums that the older proof avoids by a pointwise long-factor estimate.

The current target is therefore:

> Adapt modern unbalanced-sum / spectral-reciprocity machinery to the weighted `M_{nu,3}` family, replacing the Section 3.2 Pólya--Vinogradov long-factor disposal and the most lossy part of the Section 3.3 two-block hybrid large sieve.

The first go/no-go milestone is `theta=0.511`, which is already enough for a formal proportion above 71% once the new error estimate is rigorous.

No result above `19/27` is claimed until that off-diagonal estimate is proved.
