# Signed-family target for crossing theta = 1/2

Status: proposed analytic target; not a theorem.

This note isolates the step that must change if the Bui--Heath-Brown discrete
`zeta'` mollifier is to run with `y=T^theta`, `theta>1/2`.

## 1. Where the old proof destroys the useful arithmetic sign

Before dyadic estimation, Bui--Heath-Brown write the large-modulus contribution in
the form

\[
\mathcal M_{2,3}=
\sum_{q}\sum_{\psi\bmod q}^{*}\tau(\bar\psi)
\sum_k \frac{b(kq)}{kq}
\sum_{d\mid k}\delta(q,kq,d,\psi)
\sum_{m\le kqT/(2\pi d)}a_2(md)\psi(m).
\]

For the one-piece mollifier,

\[
b(n)=\mu(n)P\!\left(\frac{\log(y/n)}{\log y}\right).
\]

The subsequent dyadic reduction takes absolute values of the outer coefficients and
replaces the signed expression by a positive family norm `S(Q,X,d)`.  At that
point Möbius cancellation in `kq` is unavailable.

## 2. Why a uniformly stronger hybrid large sieve is not the right target

After factorizing the inner Dirichlet polynomial into two blocks `A` and `B`, the
hybrid large sieve gives a term of the schematic size

\[
Q^2V X^{1/2}.
\]

The `Q^2V` component is the natural diagonal size of the character/time family.
After the outer prefactors are restored, this contributes a term of shape

\[
QT^{1/2}.
\]

The old proof then uses `Q<=y`, giving `yT^(1/2)`.  At `y=T^theta` this is already
larger than `T` for `theta>1/2`.

Therefore a black-box replacement

> hybrid large sieve -> slightly better hybrid large sieve

is not expected to cross the wall: the problematic component contains a real
diagonal scale.  A successful argument must instead exploit information discarded
before the norm estimate, or identify and subtract/evaluate the diagonal rather than
bounding it absolutely.

## 3. The target object

For dyadic parameters

\[
Q\gg (\log T)^A,\qquad D\le K,\qquad KQ\ll y,
\]

set

\[
X=\frac{KQT}{\pi D}.
\]

The desired new input is a **signed** estimate for the dyadic piece

\[
\mathfrak M(K,Q,D)
=
\sum_{q\asymp Q}\sum_{\psi\bmod q}^{*}\tau(\bar\psi)
\sum_{k\asymp K}\frac{b(kq)}{kq}
\sum_{d\mid k}\delta(q,kq,d,\psi)
\sum_{m\le kqT/(2\pi d)}a_2(md)\psi(m),
\]

without replacing `b(kq)` by `|b(kq)|` before the family transformation.

A sufficient first milestone is to prove, uniformly for `y=T^0.511`, that the
sum of all large-modulus dyadic pieces is

\[
\boxed{\mathcal M_{2,3}=o(T(\log T)^3)}.
\]

Together with an equally uniform replacement for the base discrete-moment error,
this is enough for the one-piece main-term model to yield

\[
1-(1.511)^{-3}=0.7101277730\ldots>71\%.
\]

## 4. What a candidate technique must preserve

A proposed modern input is relevant only if it satisfies all of the following.

1. It acts before the absolute value over the outer `q,k` coefficients, or otherwise
   recovers their cancellation exactly.
2. It is uniform in the BHB dyadic ranges `K,Q,D` and the Perron variable.
3. It retains primitive-character/Gauss-sum weights, or transforms them to an
   explicitly controlled additive/spectral dual family.
4. It handles the long/unbalanced factor regime as well as the balanced two-block
   regime.
5. It produces a genuine power saving at `theta=0.511`, not merely logarithmic
   savings.

This is why continuous twisted mean-square theorems are clues rather than direct
inputs: they must first be connected to this signed discrete family.

## 5. Two concrete transformation routes

### Route A: primitive-character reciprocity

Keep the `q`-sum signed, expand the Gauss/primitive-character weights, and seek a
reciprocity or spectral formula before Cauchy.  The goal is to turn the apparent
`Q^2V` diagonal into an explicit main/dual term where the Möbius-weighted outer
sum can cancel.

### Route B: return to the additive representation

Before the multiplicative-character decomposition, the difficult contribution comes
from

\[
\sum_{k\le y}\frac{b(k)}{k}
\sum_{m\le kT/(2\pi)}a_2(m)e(-m/k).
\]

After a suitable convolution decomposition of `a_2`, investigate Poisson/Voronoi,
reciprocity, or trilinear Kloosterman-fraction technology directly in this additive
form.  This route may avoid creating the positive character norm responsible for the
square-root wall.

## 6. Go/no-go rule

Do not spend time optimizing constants inside the old positive norm.  A new estimate
is useful for the 71% project only if it changes the power of `T` in the `Q~y`
regime **without** assuming a cancellation that has already been destroyed by taking
absolute values.
