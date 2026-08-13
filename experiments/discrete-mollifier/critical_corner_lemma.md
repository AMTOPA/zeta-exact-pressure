# Critical-corner target lemma

Status: **conditional reduction / research target**, not a proved theorem.

The purpose of this note is to isolate the smallest new analytic statement that would extend the Bui--Heath-Brown mollifier beyond `theta=1/2`.

## 1. Dyadic block

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

The exact dyadic contribution should be kept **signed** at this stage: in particular, do not replace the Gauss sum, `delta(q,kq,d,psi)`, and the character sum by their absolute values before applying the new estimate.

## 2. Optimized old argument outside the corner

For a block with

\[
Q=T^\alpha,\quad K=T^\kappa,\quad D=T^\delta,
\quad g=\kappa-\delta\ge0,
\]

replace the fixed Bui--HB long-factor cutoff `y*T^(1/2)` by

\[
R=Q^{4/3}T^{1/3}(K/D)^{1/3}.
\]

In the only range where this modification is needed (`alpha>=1/2`), one has `R>=T`, so every factor that can exceed `R` is among the same Pólya--Vinogradov-compatible factors used in their Section 3.2; the truncated Möbius factors have length at most `T^(1/2)`.

Repeating their algebra with `R` in place of `y*T^(1/2)` balances the long-factor contribution and the `A0=R` two-block contribution.  The two relevant exponents are

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

Thus every dyadic block outside

\[
\boxed{
\alpha\ge\frac12,\qquad g\le2\alpha-1
}
\]

already has a power saving by the old mechanism with the optimized threshold.

Since

\[
X=T^{1+\alpha+g},
\]

the unresolved condition is equivalent to

\[
\boxed{X\le Q^3}.
\]

## 3. Target lemma

Fix `theta0>1/2`.  It would suffice to prove the following statement for `nu=1,2`.

### Critical-corner lemma (target)

There exists `delta0=delta0(theta0)>0` such that every signed dyadic contribution to `M_{nu,3}` satisfying

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

The `T^{o(1)}` margins are placeholders for the logarithmic dyadic losses in the published argument; a final proof should state explicit epsilon margins.

## 4. Consequence of the target lemma

Assuming the target lemma, combine:

1. Bui--HB's existing treatment of `q=1` and small `q`;
2. the optimized old argument for all large-modulus blocks with `X>Q^3`;
3. the new critical-corner estimate for `X<=Q^3`.

Then `M_{nu,3}=o(T log^C T)` continues to hold with `y=T^theta` for every fixed `theta<theta0` (with the appropriate log powers for `nu=1,2`).  The main-term calculation is unchanged.

The exact one-piece variational optimization then gives

\[
\boxed{
\kappa^*\ge1-\frac1{(1+\theta_0)^3}
}
\]

under RH, subject to the usual limiting interpretation if the analytic estimate is proved only for `theta<theta0`.

## 5. First milestone

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

At the worst corner, the optimized old estimate misses `T^1` by only

\[
\frac{2\theta_0-1}{3}=0.001333333\ldots
\]

in the `T` exponent.  In modulus language (`Q~T^theta0`), a net saving of only

\[
\frac{2\theta_0-1}{3\theta_0}
=0.00265604\ldots
\]

is enough.

This should be the first go/no-go theorem target.  There is no reason to optimize toward 71% until this small endpoint crossing is understood.

## 6. Why the critical corner is promising

The critical corner has three simplifying features simultaneously:

- `Q>=T^(1/2-o(1))`, so the modulus is already on the square-root scale of the external height;
- `X<=Q^3`, exactly the natural total length in sixth-moment Dirichlet-L problems;
- because `KQ<=T^theta0` and `Q>=T^(1/2)`, the outer `K` range is short: for `theta0=0.502`, one has only `K<=T^(0.002+o(1))` at the lower edge and essentially `K=T^o(1)` at `Q~y`.

Hence a new theorem does not need uniform control of arbitrary long twists.  It needs a power-saving signed estimate in a narrow conductor-admissible family with only very short extra arithmetic parameters.

## 7. Candidate tools

The current candidates are not black-box citations but proof mechanisms:

1. the unbalanced-sum complementary-divisor / functional-equation / Kuznetsov machinery in Chandee--Li--Matomäki--Radziwill (2024);
2. asymptotic-large-sieve cancellation in the style of Conrey--Iwaniec--Soundararajan (2007), if the Bui weights and Perron variable can be incorporated;
3. a direct additive treatment of the original `e(-m/k)` sum before character expansion, possibly using Voronoi/reciprocity after a suitable decomposition of `a_nu`.

The next analytic task is to decide which of these can produce the required `Q^{-0.00266}`-scale saving for `theta0=0.502` while retaining the signed structure.
