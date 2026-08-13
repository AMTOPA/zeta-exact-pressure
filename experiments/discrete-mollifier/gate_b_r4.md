# Gate B: an r=4 generalized Vaughan redesign

Status: **support/factorization redesign verified algebraically; downstream analytic estimates still under review.**

Bui--Heath-Brown Lemma 3 is stated for every integer `r>=1`.  Their published proof
chooses `r=3` and the truncated Möbius polynomial

\[
M(s)=\sum_{n\le T^{1/2}}\mu(n)n^{-s}
\]

because their relevant coefficient support satisfies `md<T^(3/2)`.

For a longer mollifier `y=T^theta`, this exact choice is no longer optimal.

## 1. Support condition

Let the truncated Möbius polynomial have length `T^u`.  The coefficients of

\[
1-\zeta(s)M(s)
\]

vanish through `n<=T^u`.  Consequently the remainder

\[
(1-\zeta M)^r\,\zeta'/\zeta
\]

has no coefficient below the `r`-fold support threshold `T^(ru)`.

The BHB coefficient range is

\[
md\ll yT=T^{1+\theta}.
\]

Thus it is enough to choose

\[
\boxed{ru>1+\theta}.
\]

At the first endpoint-crossing target `theta=0.502`:

\[
r=3\quad\Longrightarrow\quad u>0.500666\ldots,
\]

which pushes the truncated Möbius factors beyond the square-root scale.

But

\[
\boxed{r=4\quad\Longrightarrow\quad u>0.3755}.
\]

The concrete choice

\[
\boxed{u=0.38}
\]

gives

\[
4u-(1+\theta)=1.52-1.502=0.018>0,
\]

while every truncated Möbius factor remains strictly shorter than `T^(1/2)`.

This arithmetic is machine-checked by `gate_b_r4.py`.

## 2. Number and type of convolution factors

For the second moment BHB use

\[
a_2=-\Lambda*\log*\log*b.
\]

In the largest `j=r` term of the generalized Vaughan identity, replacing `Lambda`
produces

- one logarithmic factor from `zeta'`;
- `r-1` copies of the constant-one Dirichlet coefficient from `zeta^(r-1)`;
- `r` truncated Möbius factors from `M^r`.

Adding the two external logarithms and the mollifier coefficient `b` gives at most

\[
3+1+(r-1)+r=2r+3
\]

factors.

Thus:

\[
r=3:\ 9\text{ factors},
\qquad
r=4:\ \boxed{11\text{ factors}}.
\]

For `r=4` the maximal schematic list is

\[
\log,\log,\log,\ b,\ 1,1,1,\ \mu,\mu,\mu,\mu,
\]

with each Möbius factor supported below `T^0.38`.

## 3. Why the two-block grouping is not tied to nine factors

BHB Section 3.3 does not use a special identity involving the number nine.  Given
factor lengths `M_i`, total product `X`, and a target `A_0`, their construction is:

1. if one factor has `M_i >= X/A_0`, use it as one block and the remaining product
   as the other;
2. otherwise multiply factors greedily until the first block is maximal subject to
   `A<=A_0`; the next factor is `<X/A_0`, forcing the complementary block to obey the
   same `A_0` bound once `A_0` is chosen large enough.

This combinatorial argument works for any fixed finite number of factors.  Replacing
9 by 11 changes divisor-function/logarithmic exponents, but not the power geometry
of the split.

Therefore the extra two factors introduced by `r=4` are not, by themselves, a new
power obstruction.

## 4. What must still be rechecked

Gate B is **not yet declared solved**.  The remaining analytic bookkeeping is:

1. redo the `d`-separation formula with 11 factors and record the corresponding
   `tau_11` coefficient majorants;
2. replace every use of the published bound `M_i<=y*T^(1/2)` by the correct list of
   individual factor caps for `r=4,u=0.38`;
3. re-optimize the long-factor threshold rather than carrying over the old
   `y*T^(1/2)` cutoff;
4. verify that the resulting two-block lengths entering the signed critical-corner
   problem retain the same conductor relation `X<=Q^3`, or record the corrected
   corner if analytic smoothing changes it;
5. repeat the calculation for `a_1`, whose convolution is simpler but should not be
   inferred automatically from `a_2`.

The key positive conclusion is narrower but useful:

> The square-root obstruction in Gate B is not caused by a limitation of the
> generalized Vaughan identity.  BHB's identity itself permits `r=4`, and at
> `theta=0.502` one can annihilate the remainder while keeping all truncated Möbius
> factors below `T^(1/2)`.
