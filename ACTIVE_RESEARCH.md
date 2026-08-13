# Active research direction

Date: 2026-08-13

The primary research direction is now **discrete mollified moments of `zeta'(rho)`**, not further numerical tightening of the exact-pressure / pair-correlation construction.

The existing exact-pressure result remains the repository's current certified research-draft record and remains reproducible.  Its optimization line is considered frozen unless a genuinely new analytic ingredient appears.

## Why the pivot

The pair-correlation / pressure / Gram route is showing strong diminishing returns and lies in the same broad information regime as substantially optimized pair-correlation SDP methods.  A different detector already has a stronger literature baseline: Bui--Heath-Brown prove on RH that at least `19/27 = 70.370370...%` of zeta zeros are simple.

The active experiment is under:

- `experiments/discrete-mollifier/README.md`
- `experiments/discrete-mollifier/one_piece.py`
- `experiments/discrete-mollifier/rayleigh2.py`

## First result of the pivot

The published Bui--Heath-Brown one-piece main terms can be optimized exactly.  For mollifier length `y=T^theta`, the variational optimum over the full polynomial-smoothed `mu(n) P` class is

\[
\boxed{\kappa(\theta)=1-(1+\theta)^{-3}}.
\]

Thus the `19/27` endpoint is exactly the value at `theta=1/2`.

The initially proposed second basis `(mu, mu*Lambda)` is not independent because

\[
(\mu*\Lambda)(n)=-\mu(n)\log n.
\]

It is absorbed by polynomial smoothing and therefore cannot improve the variational space.

## Current main problem

Bui--Heath-Brown obtain a large-modulus error of shape

\[
M_{\nu,3}\ll y^{1/3}T^{5/6+\varepsilon}+\cdots,
\]

which forces `theta<1/2`.  The new primary goal is to improve this off-diagonal estimate enough to support `theta>1/2`.

Concrete milestones from the exact variational curve:

- 71% requires `theta > 0.5107780535`;
- 72% requires `theta > 0.5285535437`;
- 73% requires `theta > 0.5471962779`.

If the `y^(1/3)` exponent is unchanged, 71% requires improving the `T` exponent from `5/6 = 0.833333...` to below approximately `0.82974065`.

No >`19/27` theorem is claimed until the new off-diagonal bound is proved.
