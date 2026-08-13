# Analytic smoothing target for the discrete transform

Status: **analytic research target with a derived exponent budget; not yet a proved lemma.**

This note treats Gate A in `critical_corner_lemma.md`: the independent
`O(y T^(1/2+eps))` remainder in the classical sharp discrete mean-value
conversion.

## 1. Why ordinary smooth weights are not enough

A previous draft suggested inserting an arbitrary compactly supported
`C^infty` factor `w(t/T)` directly into the contour integral.  That is not a
valid residue argument: a function of `Im(s)` alone is not holomorphic.

The correct replacement is an **entire** height weight whose values on the
critical line are nonnegative.  RH, already assumed in the Bui--Heath-Brown
theorem, makes this especially natural.

## 2. Entire positive weight

Fix a center `tau~T` and a width `H` with

\[
T^{1/2+\epsilon}\ll H\ll T.
\]

Use

\[
\boxed{
\Omega_{\tau,H}(s)
=\exp\!\left[-\left(\frac{s-\frac12-i\tau}{H}\right)^4\right].
}
\]

This function is entire.  On RH, for a zero

\[
\rho=\frac12+i\gamma,
\]

one has

\[
\boxed{
\Omega_{\tau,H}(\rho)
=e^{-((\gamma-\tau)/H)^4}>0.
}
\]

Thus the weighted Cauchy detector remains valid:

\[
\sum_{\rho\;\mathrm{simple}}
\Omega_{\tau,H}(\rho)
\ge
\frac{
\left|\sum_\rho\Omega_{\tau,H}(\rho)B(\rho)\zeta'(\rho)\right|^2
}{
\sum_\rho\Omega_{\tau,H}(\rho)|B(\rho)\zeta'(\rho)|^2
}.
\]

The quartic exponential also decays super-polynomially on vertical lines as
`|Im(s)-tau|/H -> infinity`, while the horizontal displacement of the usual
zeta contour is only `O(1)` and hence negligible relative to `H`.

## 3. One-dimensional kernel

The classical Gonek kernel is

\[
J_\sigma(r)=\int \chi(\sigma+it)r^{it}\,dt.
\]

Stirling gives, for `t~T`,

\[
\chi(\sigma+it)
=\left(\frac{t}{2\pi}\right)^{1/2-\sigma}
\exp\!\left(i\left[t-t\log\frac{t}{2\pi}+\frac\pi4\right]\right)
\left(1+O(T^{-1})\right).
\]

After multiplication by `r^(it)`, the phase is

\[
\Phi(t)
=t\left(1+\log\frac{2\pi r}{t}\right)+\frac\pi4,
\]

so

\[
\Phi'(t)=\log\frac{2\pi r}{t},
\qquad
\Phi''(t)=-\frac1t,
\]

and the unique saddle is

\[
\boxed{t_0=2\pi r}.
\]

For the analytically weighted kernel

\[
J_{\sigma,\tau,H}(r)
=\int_{-\infty}^{\infty}
\Omega_{\tau,H}(\sigma+it)
\chi(\sigma+it)r^{it}\,dt,
\]

ordinary stationary phase predicts

\[
\boxed{
J_{\sigma,\tau,H}(r)
=2\pi r^{1-\sigma}e(r)
\Omega_{\tau,H}(\sigma+i2\pi r)
+\mathcal E_{\sigma,\tau,H}(r).
}
\]

The important point is the scale of the first correction.  Near the saddle,
`Phi''(t0)~T^(-1)`, while two derivatives of the analytic weight cost
`H^(-2)`.  The standard stationary-phase correction therefore has relative
size

\[
\boxed{O(T/H^2)+O(T^{-1})}.
\]

Equivalently, in the active range `r~T`, the candidate pointwise remainder is

\[
\boxed{
\mathcal E_{\sigma,\tau,H}(r)
\ll
T^{1-\sigma}\left(\frac{T}{H^2}+\frac1T\right)
}
\]

with rapid decay when `|2*pi*r-tau|` is many `H`'s.  A rigorous proof must make
this uniform through the transition region; this bound is the next lemma to
establish, not an input being assumed silently.

## 4. Why this changes the summed error scale

In the Bui--Heath-Brown transform, after expanding

\[
A(s)=\sum_m a(m)m^{-s},
\qquad
B(s)=\sum_{n\le y}b(n)n^{-s},
\]

the relevant ratio is `r=m/n`.  The saddle condition localizes

\[
m=\frac{n\tau}{2\pi}+O(nH).
\]

For `c=1+O(1/log T)`, the coefficient multiplying the kernel is of size
approximately

\[
m^{-c}n^{c-1}\asymp\frac1{nT}.
\]

There are `O(nH)` active `m` values for each `n`.  Hence the weight-curvature
part of the pointwise kernel error sums, at the level of absolute coefficient
counting, to

\[
\frac{nH}{nT}\cdot\frac{T^2}{H^2}
\asymp\frac{T}{H}
\]

per `n`, up to divisor/logarithmic factors.  Summing `n<=y` gives the candidate
total remainder

\[
\boxed{
O_\varepsilon\!\left(\frac{yT}{H}T^\varepsilon\right).
}
\]

The ordinary `O(1)` stationary-phase correction contributes only
`O(yH/T)` at this bookkeeping level and is smaller when `sqrt(T)<<H<<T`.

Thus if

\[
y=T^\theta,\qquad H=T^h,
\]

the new candidate error exponent is

\[
\boxed{1+\theta-h}.
\]

It is power-saved precisely when

\[
\boxed{h>\theta}.
\]

Since the zero-localization window must also satisfy `H=o(T)`, there is room
for every fixed `theta<1`.

A symmetric convenient choice is

\[
\boxed{h=\frac{1+\theta}{2}},
\]

for which the transform error has exponent `(1+theta)/2<1` and the relative
boundary width `H/T` tends to zero with the same power.

For the first target `theta=0.502`, this gives

\[
H=T^{0.751},
\qquad
\frac{yT}{H}=T^{0.751}.
\]

So, **if the uniform kernel lemma is proved**, Gate A would have enormous
power margin compared with the tiny `0.002` endpoint excess of the classical
sharp formula.

## 5. Main term after analytic smoothing

For the product transform with `sigma=1-c`, the saddle main term cancels the
powers of `m,n` exactly as in the classical formula.  One obtains the weighted
additive model

\[
\boxed{
\sum_{n\le y}\frac{b(n)}n
\sum_m a(m)e(-m/n)
\Omega_{\tau,H}\!\left(1-c+i\frac{2\pi m}{n}\right).
}
\]

Because the real displacement `1-c-1/2` is `O(1)` whereas `H` is a power of
`T`, replacing this saddle weight by its critical-line value changes it only
by a further `O(H^{-1})`-type analytic correction.  This correction must be
tracked explicitly in the final proof.

## 6. Recovering an unweighted dyadic proportion

The analytic weight localizes zeros to an interval of width `H=o(T)` around
`tau`.  To return to a dyadic statement, integrate the weighted inequality in
`tau` over `[T,2T]` (or use a discrete partition of centers with bounded
overlap).  By Fubini, an interior zero receives essentially the same total
positive mass, while only boundary strips of total width `O(H)` are treated
nonuniformly.

Since the zero density is `asymp log T`, the boundary contribution is
`O(H log T)`, versus `asymp T log T` zeros in the dyadic interval.  Therefore
`H=o(T)` makes the boundary loss negligible.

This averaging step needs to be written carefully for both the first and
second mollified moments, but it removes the need for a non-holomorphic compact
support weight.

## 7. Revised dependency graph for theta > 1/2

A longer one-piece proof has at least three gates:

1. **Gate A -- analytic smoothing:** prove the uniform entire-weight kernel and
   summed remainder above;
2. **Gate B -- generalized Vaughan support:** re-check the factorization/truncation
   when the mollifier exceeds `T^(1/2)`;
3. **Gate C -- signed critical corner:** prove a power-saving estimate for the
   remaining `X<=Q^3` large-modulus blocks without destroying the outer signs.

Only after all three are closed can the formal curve

\[
1-(1+\theta)^{-3}
\]

be used beyond `theta=1/2`.

## 8. Immediate proof task

The next concrete analytic task is now sharply isolated:

> Prove the uniform kernel estimate in Section 3 for the entire quartic weight,
> including rapid off-saddle decay and explicit dependence on `H`, then sum the
> remainder for the exact coefficient classes `a_1,a_2` occurring in the BHB
> first/second moments.

This is a substantially smaller problem than the signed critical-corner lemma
and is the natural first gate to try to close rigorously.
