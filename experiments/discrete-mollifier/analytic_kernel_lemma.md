# Entire-weight stationary-phase kernel: proof skeleton

Status: **derived analytic lemma candidate; the uniform tails/coefficient summation
still need a line-by-line proof before this is promoted.**

The goal is to replace the sharp Gonek kernel by an entire-weight kernel whose
stationary-phase remainder remains summable when the mollifier length is slightly
larger than `T^(1/2)`.

## 1. Kernel and phase

Fix `sigma` in a compact interval, `tau~T`, and

\[
T^{1/2+\delta}\le H\le T^{1-\delta}.
\]

Let

\[
\Omega_{\tau,H}(s)
=\exp\!\left[-\left(\frac{s-\frac12-i\tau}{H}\right)^4\right].
\]

Consider

\[
J_{\sigma,\tau,H}(r)
=\int_{-\infty}^{\infty}
\Omega_{\tau,H}(\sigma+it)
\chi(\sigma+it)r^{it}\,dt.
\]

For `t~T`, Stirling gives

\[
\chi(\sigma+it)
=\left(\frac{t}{2\pi}\right)^{1/2-\sigma}
 e^{i\Phi_0(t)}\left(1+O(T^{-1})\right),
\]

where after multiplication by `r^(it)` the phase is

\[
\Phi(t)
=t\left(1+\log\frac{2\pi r}{t}\right)+\frac\pi4.
\]

Thus

\[
\Phi'(t)=\log\frac{2\pi r}{t},
\quad
\Phi''(t)=-\frac1t,
\quad
\Phi'''(t)=\frac1{t^2},
\]

and the saddle is

\[
t_0=2\pi r.
\]

## 2. Leading term

At the saddle,

\[
\Phi(t_0)=t_0+\frac\pi4,
\qquad
\Phi''(t_0)=-1/t_0.
\]

The leading stationary-phase factor is therefore

\[
e^{-i\pi/4}\sqrt{2\pi t_0}.
\]

Multiplying by

\[
(t_0/2\pi)^{1/2-\sigma}
\]

and by `e^(i(t0+pi/4))` gives exactly

\[
\boxed{
2\pi r^{1-\sigma}e(r)
\Omega_{\tau,H}(\sigma+it_0).
}
\]

This recovers the classical Gonek main term with the hard saddle indicator replaced
by an analytic weight evaluated at the saddle.

## 3. Local expansion and the missing first-derivative loss

Put

\[
t=t_0+\sqrt{t_0}\,x.
\]

Writing `u=x/sqrt(t0)`, one has the exact Taylor pattern

\[
(1+u)(1-\log(1+u))
=1-\frac{u^2}{2}+\frac{u^3}{6}-\frac{u^4}{12}+O(u^5),
\]

so

\[
\Phi(t)
=t_0+\frac\pi4
-\frac{x^2}{2}
+\frac{x^3}{6\sqrt{t_0}}
-\frac{x^4}{12t_0}
+O\!\left(\frac{|x|^5}{T^{3/2}}\right).
\]

Let `A(t)` denote the full smooth amplitude, including the power
`(t/2*pi)^(1/2-sigma)`, the entire weight and the Stirling correction.  In the
active saddle range,

\[
\frac{A'(t_0)}{A(t_0)}
=O(T^{-1}+H^{-1}L^3),
\]

and

\[
\frac{A''(t_0)}{A(t_0)}
=O(T^{-2}+H^{-2}L^6)
\]

if `|t0-tau|<=HL` with a polylogarithmic `L`.

The potentially dangerous term in the amplitude expansion is

\[
A'(t_0)\sqrt{t_0}\,x.
\]

If bounded absolutely it would appear to cost `sqrt(T)/H`.  This loss is
spurious.  Against the leading Fresnel factor,

\[
\int_{-\infty}^{\infty}x e^{-ix^2/2}\,dx=0
\]

in the oscillatory sense.  The first nonzero contribution involving `A'` comes
from coupling it to the cubic phase correction

\[
\frac{i x^3}{6\sqrt{t_0}},
\]

so the `sqrt(t0)` factors cancel.  Its relative size is only

\[
O(A'/A)=O(H^{-1}+T^{-1}).
\]

The quadratic amplitude term contributes

\[
O\!\left(T\frac{A''}{A}\right)
=O(T/H^2+T^{-1})
\]

up to polylogarithmic factors.  Since `H<T`, this dominates the `1/H` correction.

Hence the natural relative remainder is

\[
\boxed{
O\!\left(\frac{T}{H^2}L^C+\frac{L^C}{T}\right).
}
\]

This cancellation is the central reason analytic smoothing can improve the summed
error instead of reproducing the classical `y sqrt(T)` loss.

## 4. Candidate uniform local statement

For any fixed `A>0`, choose `L=(A log T)^(1/4)`.  In the active range

\[
|t_0-\tau|\le HL
\]

and `t0~T`, the target estimate is

\[
\boxed{
J_{\sigma,\tau,H}(r)
=2\pi r^{1-\sigma}e(r)
\Omega_{\tau,H}(\sigma+it_0)
+O\!\left(
T^{1-\sigma}
\left(\frac{T}{H^2}+\frac1T\right)L^C
\,\mathcal W\!\left(\frac{t_0-\tau}{H}\right)
\right),
}
\]

where `W(u)` is a fixed polynomial times `exp(-c u^4)`.

The exact polynomial is irrelevant for summation; only its integrability matters.

## 5. Off-saddle region

The entire weight gives

\[
|\Omega_{\tau,H}(\sigma+it)|
\ll \exp(-c|(t-\tau)/H|^4)
\]

for `sigma` in a fixed strip, after enlarging the constant on a bounded central
region.

If `|t0-tau|>2HL`, then on the effective support `|t-tau|<=HL`,

\[
|\Phi'(t)|
=\left|\log\frac{t_0}{t}\right|
\gg \frac{|t_0-\tau|}{T}.
\]

Integration by parts with

\[
\mathcal D=(i\Phi'(t))^{-1}\frac d{dt}
\]

costs one amplitude derivative `O(H^(-1)L^C)` but gains
`T/|t0-tau|`.  At the boundary `|t0-tau|=HL`, the net factor is

\[
\frac{T}{H^2L}\ll T^{-2\delta}/L,
\]

because `H>=T^(1/2+delta)`.  Repetition therefore gives arbitrary power saving.
The tails where `|t-tau|>HL` are already `O(T^{-A})` from the quartic weight.

This supplies the required rapid decay away from the saddle, modulo routine
bookkeeping of derivatives of the Stirling expansion.

## 6. Summation over BHB coefficients

For the product transform on `Re(s)=c=1+O(1/log T)`, one uses
`sigma=1-c`.  The coefficient outside the kernel is

\[
m^{-c}n^{c-1}.
\]

In the active range `m/n~T`,

\[
m^{-c}n^{c-1}\asymp\frac1{nT^c}.
\]

For fixed `n`, the entire saddle weight restricts `m` to an interval of effective
length `O(nH L)`.  For the BHB coefficient classes `a_1,a_2`, divisor/logarithmic
majorants give schematically

\[
\sum_{m\ \mathrm{active}}|a_\nu(m)|m^{-c}
\ll H T^{-c}L^C.
\]

Multiplying by the kernel remainder `T^(c+1)/H^2` gives

\[
O(T/H\,L^C)
\]

for each outer `n`.  With bounded mollifier coefficients and `n<=y`, the total
candidate error is therefore

\[
\boxed{
O\!\left(\frac{yT}{H}L^C\right).
}
\]

The ordinary `1/T` stationary-phase correction gives only `O(yH/T L^C)`.

## 7. Consequence for the first crossing

Let

\[
y=T^\theta,\qquad H=T^h.
\]

The curvature error is power-saved if

\[
h>\theta,
\]

while local-to-dyadic averaging requires `h<1`.  These are compatible for every
fixed `theta<1`.

For `theta=0.502`, the balanced choice

\[
h=(1+\theta)/2=0.751
\]

gives

\[
\frac{yT}{H}=T^{0.751},
\qquad
H/T=T^{-0.249}.
\]

Thus Gate A has large formal power margin if the target kernel estimate is closed.

## 8. What remains before calling this a lemma

The conceptual stationary-phase mechanism is now explicit.  A rigorous promotion
still requires:

1. a uniform Stirling expansion for `chi(s)` with enough derivatives on the two
   contour lines;
2. explicit near/far cutoffs showing the oscillatory odd-term cancellation without
   an illegal absolutely convergent Fresnel manipulation;
3. divisor-sum bounds for the exact `a_1,a_2` coefficient classes with the quartic
   saddle weight;
4. the contour/residue calculation for the first and second weighted moments and
   the comparison of the saddle-line weight to its positive critical-line value;
5. averaging in `tau` to recover the dyadic unweighted proportion.

None of these five items invokes the hard signed critical-corner estimate.  Gate A
has therefore been isolated as a plausible standalone lemma rather than hidden
inside the large-modulus problem.
