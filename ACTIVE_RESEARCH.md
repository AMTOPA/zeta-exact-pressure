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

The active experiment is under `experiments/discrete-mollifier/`.

## Formal one-piece optimum

For mollifier length `y=T^theta`, the Bui--Heath-Brown one-piece main-term model has exact variational optimum

\[
\boxed{\kappa(\theta)=1-(1+\theta)^{-3}}.
\]

Thus `19/27` is exactly the endpoint at `theta=1/2`.

The initially proposed second basis `(mu, mu*Lambda)` is not independent because

\[
(\mu*\Lambda)(n)=-\mu(n)\log n.
\]

It is absorbed by polynomial smoothing and has been discarded.  A genuine Feng-type `k=2` squarefree prime-factor piece remains a parallel fallback, but no mixed `zeta'` moment is claimed yet.

## First theorem milestone: theta = 0.502

Do **not** optimize toward 71% first.  The smallest useful structural crossing is

\[
\boxed{\theta_0=0.502}.
\]

The formal one-piece value is then

\[
1-(1.502)^{-3}=0.7048857354\ldots,
\]

or

\[
\boxed{70.48857354\%}.
\]

The point of this target is not the numerical record.  It tests whether the square-root length wall can be crossed at all.

## The three analytic gates

A rigorous `theta>1/2` extension now has three separate dependencies.

### Gate A -- analytic discrete smoothing

The classical sharp discrete transform has an independent remainder

\[
O_\varepsilon(yT^{1/2+\varepsilon}).
\]

A non-holomorphic `C^infty` cutoff cannot simply be inserted into the residue contour.  The active replacement is the entire positive-on-RH weight

\[
\Omega_{\tau,H}(s)
=\exp\!\left[-\left(\frac{s-\frac12-i\tau}{H}\right)^4\right].
\]

At a zero `rho=1/2+i gamma`,

\[
\Omega_{\tau,H}(\rho)=e^{-((\gamma-\tau)/H)^4}>0.
\]

The one-dimensional stationary-phase expansion has saddle `t0=2*pi*r`.  The first amplitude-derivative term is odd and cancels against the leading Fresnel kernel; the first uniform weight cost is therefore `T/H^2`, not `sqrt(T)/H`.

After summing the BHB coefficient ranges, the candidate Gate-A remainder is

\[
\boxed{O_\varepsilon(yT/H\,T^\varepsilon)}.
\]

With `y=T^theta` and

\[
H=T^{(1+\theta)/2},
\]

this has exponent `(1+theta)/2<1`.  At `theta=0.502`, the formal remainder is only `T^0.751` up to logarithms.  This is a derived proof target, not yet a proved lemma; see `smooth_discrete_target.md` and `analytic_kernel_lemma.md`.

### Gate B -- generalized Vaughan support/factorization

The published factorization is tuned to `theta<1/2`.  When `theta` moves above the square-root point, its truncation/support bookkeeping must be rederived before any modern mean-value theorem is imported.

The main design question is whether increasing the Heath-Brown/Vaughan identity depth can keep every truncated Möbius factor below `T^(1/2)` while still annihilating the unwanted support.  This gate is combinatorial/factor-length bookkeeping, distinct from the analytic estimates in Gates A and C.

### Gate C -- signed critical corner

After optimizing the old long-factor cutoff, all large-modulus blocks outside

\[
\alpha\ge\frac12,\qquad g\le2\alpha-1
\]

already power-save.  Since

\[
X=T^{1+\alpha+g},\qquad Q=T^\alpha,
\]

the unresolved region is exactly

\[
\boxed{X\le Q^3}.
\]

For `theta=0.502`, the extra signed-family saving needed at the worst edge is only

\[
\boxed{Q^{-2/753+o(1)}}.
\]

The key restriction is methodological: this saving must be obtained **before** the outer Möbius/Gauss-sum structure is destroyed by absolute values.

## Current Kloosterman lead

Thomas Wright's 2026 partially-fixed-modulus trilinear Kloosterman work is a serious compatibility lead, but not a black-box theorem for BHB.

At the conductor edge `X~Q^3`, Wright's current short-factor range contains

\[
N\lesssim Q^{9/14},
\]

whereas the BHB outer factor at `theta=0.502` is only

\[
K\le T^{0.002+o(1)}\le Q^{0.004+o(1)}.
\]

So raw parameter size is not the obstacle.  The remaining questions are whether the BHB additive/character expression can be transformed into the required fixed-factor Kloosterman phase **without losing the outer sign**, and whether one resulting coefficient satisfies the needed Siegel--Walfisz condition.

The withdrawn 2026 Dong--Robles--Zeindler `1/46` twisted-second-moment claim is explicitly excluded from the project; see `KLOOSTERMAN_2026_AUDIT.md`.

## Current execution order

1. Close the entire-weight one-dimensional stationary-phase lemma for Gate A, including uniform tails and exact `a_1,a_2` coefficient summation.
2. Rebuild Gate B with general truncation/depth parameters and identify a choice that keeps all short Möbius factors below the square-root scale at `theta=0.502`.
3. Starting from the **signed additive** BHB expression, derive one explicit reciprocity/Poisson transformation and test whether the resulting phase fits Wright's partially-fixed-modulus theorem.
4. Keep the Feng `k=2` two-piece route in parallel only as a formal main-term fallback; do not invest in its off-diagonal proof until its Schur-complement gain is known.

No result above `19/27` is claimed until all new analytic dependencies for the chosen route are proved.
