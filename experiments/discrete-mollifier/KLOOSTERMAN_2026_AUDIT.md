# 2026 Kloosterman-input audit

Status: literature/method compatibility audit; no transfer theorem is claimed.

This note records two current 2026 developments relevant to the signed critical
corner and, equally importantly, one result that must **not** be used.

## 1. Withdrawn input: Dong--Robles--Zeindler, arXiv:2601.00292

The preprint *Bilinear forms with Kloosterman fractions and applications* originally
claimed, among other applications, a twisted second-moment asymptotic with
Dirichlet-polynomial length `T^(1/2+1/46)`.

The authors subsequently withdrew the claimed improvement.  The withdrawal note
states that an `L^2` factor was missed in equation (2.53), turning `L^5` into `L^7`;
after correction, the argument no longer yields the advertised improved bound.

**Repository rule:** the claimed `1/46` extension is not an admissible analytic
input, benchmark, or heuristic theorem.  It may be mentioned only as a withdrawn
attempt and source of techniques whose surviving statements are checked separately.

## 2. Current input: Wright, arXiv:2604.25177v2

Thomas Wright's *Trilinear Kloosterman fractions I: partially fixed moduli and
unbalanced convolutions* develops an improvement of Bettin--Chandee when the
denominator in the Kloosterman fraction contains a fixed factor.  The mechanism is
specifically designed for unbalanced convolutions and preserves a built-in
complementary divisor instead of paying for it as part of a generic coefficient
length.

In the current theorem body, Corollary 2.2(i) treats convolutions in arithmetic
progressions under a Siegel--Walfisz hypothesis on one coefficient sequence, with a
range including

\[
N\le Q^{-33/28}X^{17/28-\varepsilon}.
\]

The paper also explains that the gain comes from a trilinear Kloosterman-fraction
bound with a partially fixed denominator.

## 3. Why Wright is structurally relevant to the BHB critical corner

After optimizing the old Bui--Heath-Brown long-factor cutoff, the unresolved block
has

\[
X_{\rm BHB}=\frac{KQT}{D}\le Q^3,
\qquad
Q\ge T^{1/2-o(1)},
\qquad
K/D=T^{g},\quad g\le2\log_TQ-1.
\]

For the first target `theta=0.502`, the outer parameters are very short:

\[
K\le T^{0.002+o(1)}
\]

at the lower edge `Q~T^(1/2)`, and shorter still near `Q~T^theta`.

This is exactly the qualitative situation in which a "partially fixed modulus"
may be more useful than a fully generic Bettin--Chandee bound: the extra arithmetic
factor is short and should not automatically be charged as part of the oscillatory
conductor.

### Quantitative size check at the conductor edge

Suppose a future transformation identifies Wright's convolution scale with a block
at the BHB conductor edge

\[
X\asymp Q^3.
\]

Then the current Corollary 2.2(i) short-factor condition becomes

\[
N\le Q^{-33/28}(Q^3)^{17/28-\varepsilon}
=Q^{9/14-3\varepsilon}.
\]

Ignoring the explicit epsilon margin, the allowed short exponent is therefore

\[
\boxed{9/14\approx0.642857}.
\]

By contrast, at `theta=0.502` and `Q>=T^(1/2)`, the entire BHB outer range obeys

\[
K\le T^{0.002+o(1)}\le Q^{0.004+o(1)}.
\]

Thus, **if** one of the BHB short arithmetic parameters can genuinely be mapped to
Wright's short convolution/fixed-factor variable, its size is nowhere near the
published range boundary.  The size geometry has huge slack.

This is a useful negative/positive separation:

- **not the main problem:** the raw length of `K` or `D`;
- **still the main problem:** obtaining the correct Kloosterman phase, preserving
  the outer sign, and producing a coefficient satisfying the required
  Siegel--Walfisz/equidistribution hypothesis.

## 4. Why Wright is not yet a black-box theorem for BHB

The present BHB object is not the convolution-in-progressions sum in Wright's
Corollary 2.2.  Before absolute values it contains

\[
\tau(\bar\psi)\,b(kq)\,\delta(q,kq,d,\psi)
\]

and an inner generalized-Vaughan convolution, together with a Perron variable.
A direct application would require at least the following transformations.

1. Convert the primitive-character/Gauss-sum family back to an additive or
   Kloosterman-fraction phase while retaining the signed outer `mu(kq)` weight.
2. Identify a factor playing Wright's fixed denominator role; candidates are built
   from the short `K,D` arithmetic parameters after reciprocity.
3. Produce one genuinely Siegel--Walfisz/equidistributed coefficient sequence in
   the resulting convolution, rather than assuming it.
4. Check the exact size dictionary between Wright's `(M,N,Q,X,R)` and the BHB
   `(K,Q,D,T,X_BHB)` block.
5. Keep the estimate uniform in any smoothing/Perron parameter introduced by the
   discrete transform.

Until this map is written, Wright's theorem is a **methodological lead**, not an
input to the simple-zero bound.

## 5. The range test to perform next

The most useful next calculation is not to compare headline exponents.  Starting
from the BHB additive phase before character expansion,

\[
\sum_{k\sim K}\frac{b(k)}k
\sum_m a_\nu(m)e(-m/k)W(m/(kT)),
\]

insert one concrete generalized-Vaughan factorization of `a_nu`, perform additive
reciprocity/Poisson on the longest factor, and record the resulting phase in the
canonical form

\[
e\!\left(\vartheta\frac{a\overline m}{Rn}\right)
\]

or prove that it cannot be reduced to such a form without losing the outer sign.
Only then should Wright's fixed-factor theorem be tested against the
`theta=0.502` corner.

## 6. Current decision

- **Do not use** the withdrawn `1/46` twisted-second-moment claim.
- **Do investigate** Wright's partially fixed denominator mechanism after deriving
  the exact additive phase generated by the BHB convolution.
- The first quantitative goal remains tiny: the critical corner at `theta=0.502`
  needs only a `Q^(-2/753)`-scale net saving.  Compatibility matters more than a
  large nominal exponent in an unrelated family.
