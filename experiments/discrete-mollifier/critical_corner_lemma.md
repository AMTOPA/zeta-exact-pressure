# Critical-corner target lemma

Status: **conditional reduction / research target**, not a proved theorem.

This note isolates the large-modulus part of a possible extension of the Bui--Heath-Brown mollifier beyond `theta=1/2`.  **The critical-corner lemma below is not sufficient by itself.**  A complete extension also requires an improvement/reformulation of the `O(y T^(1/2+eps))` remainders already present in Bui--Heath-Brown Lemma 1, and a compatible generalized-Vaughan truncation when `theta>1/2`.

## 1. Three analytic gates

Fix `theta0>1/2`.  A complete endpoint extension has at least three logically separate gates.

### Gate A: discrete-moment remainder

Bui--Heath-Brown Lemma 1 states the first and second discrete moment formulas with remainders of size

\[
O_\varepsilon(yT^{1/2+\varepsilon}).
\]

For `y=T^theta`, this ceases to be lower order as soon as `theta>1/2`.  One must either improve this remainder or reformulate the preliminary discrete moment identity so that the corresponding error is power-saved for the desired `theta`.

### Gate B: generalized-Vaughan support

Their Lemma 3 uses `r=3` and a truncated Möbius polynomial of length `T^(1/2)`.  The remainder is killed in the published range because the relevant Dirichlet coefficients are only needed up to `n << yT < T^(3/2)`.

For a truncation length `T^u`, the same support mechanism suggests the condition

\[
ru>1+\theta.
\]

Thus for `r=3` and `theta` just above `1/2`, one can formally choose

\[
\frac{1+\theta}{3}<u<\theta,
\]

but all subsequent factor-length estimates must be rechecked with this changed `u`.  Alternatively one can redesign the Vaughan identity (for example with a different `r`).

### Gate C: large-modulus critical corner

After optimizing the old long-factor threshold, only a narrow conductor-admissible corner of `M_{nu,3}` remains unresolved.  This is the target of the rest of this note.

## 2. Dyadic block for Gate C

Start from Bui--Heath-Brown equation (11) for `M_{nu,3}` and restrict `k,q,d` to a dyadic block

\[
K/2<k\le K,\qquad Q/2<q\le Q,\qquad D<d\le2D,
\]

with

\[
D\le K,\qquad KQ\ll y=T^\theta.
\]

Let

\[
X=\frac{KQT}{\pi D}.
\]

The exact dyadic contribution should be kept **signed** at this stage: in particular, do not replace the Gauss sum, the arithmetic factor `delta(q,kq,d,psi)`, and the character sum by their absolute values before applying the new estimate.

## 3. Optimized old argument outside the corner

For a block with

\[
Q=T^\alpha,\quad K=T^\kappa,\quad D=T^\delta,
\quad g=\kappa-\delta\ge0,
\]

replace the fixed published long-factor cutoff `y*T^(1/2)` by

\[
R=Q^{4/3}T^{1/3}(K/D)^{1/3}.
\]

In the range where this modification matters (`alpha>=1/2`), `R>=T`.  Subject to Gate B supplying a compatible factorization, the same Pólya--Vinogradov treatment of a genuinely long smooth factor and the same two-block hybrid-large-sieve algebra give the two exponents

\[
E_R=\frac{2\alpha}{3}+\frac23-\frac g3
\]

and

\[
E_{2/3}=\frac56+\frac\alpha3-\frac g6.
\]

Both are strictly below `1` when

\[
g>2\alpha-1.
\]

Hence the only unresolved large-modulus region is

\[
\boxed{
\alpha\ge\frac12,\qquad g\le2\alpha-1.
}
\]

Since

\[
X=T^{1+\alpha+g},
\]

this is equivalent to

\[
\boxed{X\le Q^3}.
\]

## 4. Gate-C target lemma

There exists `delta0=delta0(theta0)>0` such that every **signed** dyadic contribution to `M_{nu,3}` satisfying

\[
T^{1/2-o(1)}\le Q\le T^{\theta_0+o(1)},
\]

\[
D\le K,\qquad KQ\ll T^{\theta_0},
\]

and

\[
X=\frac{KQT}{\pi D}\le Q^3T^{o(1)}
\]

is

\[
\boxed{\ll T^{1-\delta_0}}.
\]

The `T^{o(1)}` margins stand for logarithmic/dyadic losses; a final statement must use explicit epsilon margins.

## 5. Conditional consequence of all three gates

Assume simultaneously:

1. **Gate A:** the preliminary first/second discrete-moment formulas are valid with an `o(T log^C T)` remainder for every fixed `theta<theta0`;
2. **Gate B:** the generalized-Vaughan/factorization step is valid in that range with factor lengths compatible with the estimates used below;
3. **Gate C:** the signed critical-corner estimate above;
4. all remaining small-modulus and noncritical large-modulus steps retain the same power savings after the parameter changes.

Then the Bui--Heath-Brown main-term calculation extends to every fixed `theta<theta0`.  The exact one-piece variational optimization gives the formal endpoint

\[
\boxed{
\kappa^*\ge1-\frac1{(1+\theta_0)^3}
}
\]

under RH, with the usual limiting interpretation.

This is a **conditional reduction**, not a proof beyond `19/27`.

## 6. First milestone

Take

\[
\boxed{\theta_0=0.502}.
\]

The formal simple-zero proportion is

\[
1-\frac1{1.502^3}
=0.7048857354\ldots,
\]

or

\[
\boxed{70.48857354\%}.
\]

For Gate C, the worst optimized old block misses `T^1` by only

\[
\frac{2\theta_0-1}{3}=0.001333333\ldots
\]

in the `T` exponent.  In modulus language (`Q~T^theta0`), a net saving of only

\[
\frac{2\theta_0-1}{3\theta_0}
=0.00265604\ldots
\]

would suffice for this gate.

Gate A has a different budget: the published `yT^(1/2)` remainder misses `T^1` by `theta0-1/2=0.002`.  It must be treated independently.

## 7. Why Gate C remains promising

The critical corner has three simplifying features simultaneously:

- `Q>=T^(1/2-o(1))`;
- `X<=Q^3`, the natural total conductor length in sixth-moment Dirichlet-L problems;
- because `KQ<=T^theta0`, the outer `K` range is extremely short when `theta0` is only slightly above `1/2`.

Thus a new theorem does not need arbitrary long twists.  It needs a small power saving in a narrow, conductor-admissible, signed family.

## 8. Candidate tools

For Gate C:

1. unbalanced-sum complementary-divisor / functional-equation / Kuznetsov machinery in Chandee--Li--Matomäki--Radziwill;
2. asymptotic-large-sieve cancellation in the style of Conrey--Iwaniec--Soundararajan;
3. a direct additive treatment of the original `e(-m/k)` sum before character expansion, possibly using reciprocity/Voronoi after decomposing `a_nu`.

For Gate A, the immediate task is different: trace the exact source of the `O(yT^(1/2+eps))` term in the underlying discrete moment formula and determine whether it comes from a truncation/contour step that admits cancellation, or from an intrinsically square-root-sized arithmetic error.

For Gate B, rederive the support/factor-length bookkeeping with general `(r,u)` before importing any modern mean-value theorem.
