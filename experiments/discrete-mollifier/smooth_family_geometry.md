# Analytic smoothing inside the two-block character family

Status: **exponent-level reduction; the weighted hybrid-large-sieve step still needs a formal proof.**

The entire-weight Gate-A proposal changes the additive product condition from a sharp
prefix to a smooth short window.  This note tracks what that change does to the
Bui--Heath-Brown two-block family after Mellin inversion.

## 1. Relative product width

The saddle weight localizes

\[
m/n=\tau/(2\pi)+O(H),
\]

so in a dyadic block whose product center is `X`, the relative product width is

\[
\boxed{\delta=H/T}.
\]

Write a model product cutoff as

\[
W_\delta(x)=w((x-1)/\delta).
\]

Its Mellin transform has the scaling

\[
\widehat W_\delta(t)
=\delta\,\widehat w_{\rm Mellin}(\delta t)
\]

up to harmless `O(delta)` changes caused by replacing `log x` with `x-1` on the
short support.  Consequently

\[
|t|\lesssim\delta^{-1}=T/H
\]

is the effective Mellin range, while

\[
\int|\widehat W_\delta(t)|\,dt\asymp1.
\]

## 2. Weighted hybrid-large-sieve scaling

Let the generalized-Vaughan convolution be split into blocks of lengths `A,B` with
`AB~X`.  On a Mellin dyadic interval of size `V`, the usual hybrid large sieve gives
schematically

\[
\int_{|t|\lesssim V}\sum_{q\sim Q}\sum_\psi^*|A(\psi,t)|^2dt
\ll (Q^2V+A)A\,L^C,
\]

and similarly for `B`.

On the active range `V~delta^(-1)`, the Mellin weight itself has size `~delta`.
After Cauchy, the weighted two-block family therefore has the structural scale

\[
\boxed{
Q^2X^{1/2}
+Q\delta^{1/2}X^{1/2}A_0^{1/2}
+\delta X
}
\]

up to logarithmic factors and the usual `A,B<=A_0` grouping.

The same conclusion follows by summing Mellin dyadic intervals: the `Q^2V` part is
multiplied by `delta` at the largest active `V=delta^(-1)`, so it remains `Q^2`;
the polynomial-length parts retain one power of the small Mellin amplitude.

## 3. The crucial negative result

Analytic smoothing **does not** save a power on

\[
\boxed{Q^2X^{1/2}}.
\]

That term is the true diagonal scale of the primitive-character family.  Its survival
is important: one cannot claim that smoothing alone proves the critical-corner
estimate or crosses `theta=1/2`.

What smoothing does do is isolate this diagonal more cleanly.  The other two generic
hybrid-large-sieve branches gain powers of `delta`.

## 4. Size at the first endpoint crossing

For

\[
\theta=0.502,
\qquad
H=T^{(1+\theta)/2}=T^{0.751},
\]

we have

\[
\delta=H/T=T^{-0.249}
\]

and effective Mellin width

\[
\delta^{-1}=T^{0.249}.
\]

Thus, relative to the sharp-Perron bookkeeping,

\[
\boxed{
\text{mixed branch gains }T^{-0.1245},
\qquad
\text{pure-length branch gains }T^{-0.249}.
}
\]

These are enormous compared with the `T^{-0.0013}`-scale saving needed at the
first critical-corner milestone.

The family diagonal receives no such gain.

## 5. Revised interpretation of Gate C

After analytic smoothing and an `r=4` Gate-B factorization, the hard question should
not be phrased as "improve every branch of the old hybrid large sieve."  The two
length-sensitive branches now have large formal slack.

The genuinely new analytic task is more specific:

> evaluate, subtract, or exploit signed cancellation in the piece represented by
> the `Q^2 X^(1/2)` family diagonal **before** the outer Möbius/Gauss-sum structure is
> destroyed by absolute values.

This is precisely the type of task for which asymptotic large sieve, additive
reciprocity, complementary-divisor, or partially-fixed-modulus Kloosterman methods
are conceptually relevant.

## 6. Remaining proof obligations

Before this reduction is used in a theorem, one must:

1. derive the exact Mellin transform of the entire saddle weight rather than the
   model `W_delta`;
2. prove a weighted hybrid-large-sieve inequality with the stated `delta` scaling;
3. track the `d_i` divisor decomposition and the `r=4` eleven-factor coefficients;
4. verify that the outer prefactors convert the surviving `Q^2 X^(1/2)` piece to
   the same signed critical-corner scale identified in the sharp argument;
5. only then match the remaining signed diagonal to a spectral/Kloosterman theorem.

`smoothed_family_geometry.py` checks the exact exponent bookkeeping for the proposed
`theta=0.502`, `H=T^0.751` parameters.
