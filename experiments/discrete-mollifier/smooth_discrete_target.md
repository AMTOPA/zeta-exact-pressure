# Smooth discrete-transform target

Status: **analytic research target**, not a proved lemma.

This note isolates the first of two independent obstacles to extending the
Bui--Heath-Brown one-piece mollifier beyond `theta=1/2`.

## 1. Why the large-modulus estimate is not the whole problem

Before estimating the large-modulus term `M_{nu,3}`, the Conrey--Ghosh--Gonek / Bui--Heath-Brown discrete mean-value conversion already contains an error of shape

\[
O_\varepsilon(yT^{1/2+\varepsilon}).
\]

For `y=T^theta` this is lower order only for `theta<1/2`.  Therefore a proof of the signed critical-corner lemma for `M_{nu,3}` alone does **not** justify `theta>1/2`.

The source of this error is the sharp stationary-phase conversion attached to a hard height endpoint.  In its simplest form, Gonek's stationary-phase lemma turns

\[
\frac1{2\pi}\int_0^T
\chi(1-c-it)\sum_{m\ge1}a_m m^{-c-it}\,dt
\]

into a sharp sum over `m<=T/(2*pi)` with an error of square-root size.

## 2. Weighted detector

Let `w>=0` be a fixed smooth weight supported in `(1,2)`.  Define

\[
S_1(w)=\sum_\rho w(\gamma/T)\,B(\rho)\zeta'(\rho),
\]

and

\[
S_2(w)=\sum_\rho w(\gamma/T)\,|B(\rho)\zeta'(\rho)|^2.
\]

Since a multiple zero has `zeta'(rho)=0`, weighted Cauchy gives

\[
\sum_{\rho\;\mathrm{simple}}w(\gamma/T)
\ge \frac{|S_1(w)|^2}{S_2(w)}.
\]

Thus replacing a sharp zero-height cutoff by a nonnegative smooth one preserves the simple-zero detector.

If a uniform lower bound is proved for a sequence of smooth weights satisfying
`0<=w<=1` and tending from inside to the indicator of `[1,2]`, the usual zero-counting asymptotic recovers the same unweighted dyadic liminf, up to an arbitrarily small boundary loss.

## 3. Desired stationary-phase identity

The model weighted transform should have the form

\[
\frac{1}{2\pi i}\int
w(t/T)\,\chi(1-c-it)A(c+it)B(1-c-it)\,dt
\]

with

\[
A(s)=\sum_{m\ge1}a(m)m^{-s},\qquad
B(s)=\sum_{n\le y}b(n)n^{-s}.
\]

After expanding the absolutely convergent series, the stationary point is at

\[
t=\frac{2\pi m}{n}.
\]

The expected main term is therefore the **smooth additive sum**

\[
\boxed{
\sum_{n\le y}\frac{b(n)}n
\sum_{m\ge1}a(m)e(-m/n)
\,w\!\left(\frac{2\pi m}{nT}\right)
}.
\]

Unlike the sharp formula, there is no discontinuous condition
`m<=nT/(2*pi)` at the upper saddle endpoint.

## 4. First theorem target

For the first crossing milestone, set

\[
\theta_0=0.502.
\]

A sufficient smooth-transform theorem is an asymptotic of the form above,
uniformly for `y<=T^(theta0)`, with total remainder

\[
\boxed{O(T^{1-\delta} (\log T)^C)}
\]

for some fixed `delta>0`, for each Dirichlet series `A` occurring in the first and second mollified `zeta'` moments.

No particular value of `delta` is required beyond positivity.  The logarithmic powers differ between the first and second moments and should be tracked in a proof rather than hidden in the final statement.

## 5. Why smoothing is a plausible lever

The square-root error in the classical sharp lemma is consistent with a stationary-phase estimate with hard endpoints.  For a smooth compactly supported weight, repeated integration by parts kills nonstationary ranges, while the saddle contribution has a full local asymptotic expansion.  This suggests that the `y*T^(1/2)` barrier should be re-audited rather than treated as automatically structural.

This paragraph is motivation only.  A proof must still sum the stationary-phase remainders uniformly over `m,n`; no power saving is claimed here.

## 6. Dependency graph for theta > 1/2

A longer one-piece mollifier now has two explicit analytic dependencies:

1. **smooth discrete-transform lemma:** remove the independent sharp-endpoint `y*T^(1/2)` loss;
2. **signed critical-corner lemma:** control the remaining large-modulus blocks in `M_{nu,3}` without discarding the outer arithmetic signs.

Only after **both** are proved may the unchanged formal main-term curve

\[
1-(1+\theta)^{-3}
\]

be used with `theta>1/2`.

## 7. Immediate technical task

Prove a one-dimensional kernel lemma first: for fixed smooth `w`, obtain a uniform asymptotic for

\[
\frac1{2\pi}\int w(t/T)\chi(1-c-it)v^{-c-it}\,dt
\]

through the saddle `t=2*pi*v`, with a remainder strong enough to be summable after `v=m/n` and `n<=T^0.502`.  This isolates the analytic issue before any zeta-specific convolution is introduced.
