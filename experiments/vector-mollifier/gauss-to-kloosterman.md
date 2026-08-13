# Gauss-to-Kloosterman rewrite of the large-modulus term

Status: **exact algebraic reduction / analytic estimates not yet proved**.

This note identifies a different place to attack the `theta=1/2` barrier in Bui--Heath--Brown. Instead of taking absolute values of Gauss sums and then applying Cauchy plus the hybrid large sieve, retain the Gauss phase and perform primitive-character orthogonality first.

Primary source for the starting expression: Bui--Heath--Brown, arXiv:1302.5018, equations (5), (6), (11), especially the squarefree cleanup immediately before equation (11).

## 1. Squarefree support

Their mollifier coefficient is

\[
b(k)=\mu(k)P\left(\frac{\log(y/k)}{\log y}\right).
\]

Hence a nonzero term `b(kq)` forces `kq` to be squarefree. In particular

\[
q\ \text{is squarefree},
\qquad
(k,q)=1.
\]

This is exactly the observation used in Bui--Heath--Brown to simplify `d|kq` to `d|k`.

## 2. The `l`-dependence disappears from the character phase

Their equation (6) contains

\[
\delta(q,kq,d,\psi)
=
\sum_{l\mid(d,k)}
\frac{\mu(d/l)}{\varphi(kq/l)}
\overline\psi(-k/l)\psi(d/l)\mu(k/l).
\]

After multiplying by the inner `psi(m)` from equation (11), and using `(k,q)=1`,

\[
\overline\psi(-k/l)\psi(d/l)\psi(m)
=
\psi(-dm\bar k).
\]

Thus **the entire oscillatory character factor is independent of `l`**. All `l`-dependence remains in a nonoscillatory divisor coefficient.

## 3. Exact primitive Gauss identity

For `(r,q)=1`, define

\[
G_q(r)
:=
\sum_{\psi\;({\rm mod}\ q)}^{*}
\tau(\overline\psi)\psi(r).
\]

Primitive-character orthogonality gives

\[
\sum_{\psi\;({\rm mod}\ q)}^{*}\psi(n)
=
\sum_{d\mid(q,n-1)}\varphi(d)\mu(q/d).
\]

Since

\[
\tau(\overline\psi)
=
\sum_{a\;({\rm mod}\ q)}^{*}
\overline\psi(a)e(a/q),
\]

we get

\[
G_q(r)
=
\sum_{d\mid q}\varphi(d)\mu(q/d)
\sum_{\substack{a\;({\rm mod}\ q)^{*}\\a\equiv r\;({\rm mod}\ d)}}e(a/q).
\]

For squarefree `q`, write `q=dh`. CRT gives

\[
\sum_{\substack{a\;({\rm mod}\ q)^{*}\\a\equiv r\;({\rm mod}\ d)}}e(a/q)
=
\mu(h)e(r\bar h/d).
\]

Since `mu(h)^2=1`,

\[
\boxed{
G_q(r)
=
\sum_{d\mid q}
\varphi(d)
e\left(\frac{r\,\overline{q/d}}{d}\right)
}
\qquad(q\ \text{squarefree}).
\]

The `d=1` exponential is interpreted as `1`.

For prime `q=p`, this reduces to the elementary check

\[
G_p(r)=1+(p-1)e(r/p).
\]

`check_gauss_transform.py` directly enumerates primitive characters for small odd squarefree moduli and checks this identity numerically.

## 4. Application to the Bui--Heath--Brown phase

In equation (11), put

\[
r=-dm\bar k\pmod q.
\]

For a divisor `c|q`, the corresponding oscillation is

\[
e\left(-\frac{dm\bar k\,\overline{q/c}}{c}\right).
\]

Now write

\[
q=ch,
\qquad
n=kh.
\]

Because `kq` is squarefree, `(k,h)=1`, `(n,c)=1`, and

\[
kq=nc,
\qquad
\frac1{kq}=\frac1{nc}.
\]

The reciprocal phase becomes

\[
\boxed{
e\left(-\frac{dm\bar n}{c}\right)
}.
\]

The original mollifier cutoff also simplifies:

\[
kq\le y
\iff
nc\le y.
\]

Thus the large-modulus contribution can be reorganized into divisor-weighted sums whose oscillatory core has **Kloosterman-fraction form in `(n,c)`**.

The quotient `h=q/c` and the old divisor variables remain inside arithmetic coefficients/conditions, but the phase and the principal mollifier factor no longer depend on them in a complicated way.

## 5. Why this changes the attack surface

Bui--Heath--Brown next use `|tau(psi)|=q^{1/2}`, losing the Gauss phase before equation (13), and eventually apply Cauchy plus the hybrid large sieve. That produces the two raw barriers

\[
yT^{1/2+ε},
\qquad
y^{1/2}T^{3/4+ε}.
\]

The rewrite above suggests a different order of operations:

1. use squarefree support and cancel the `l`-dependence in the character phase;
2. perform the primitive-character/Gauss sum exactly;
3. reorganize `q=ch`, `n=kh`;
4. only then apply the generalized Vaughan/Type I--II decomposition to the `m`-coefficient;
5. estimate the resulting reciprocal sums
   \[
   \sum_{n,c}\alpha_n\beta_c
   e(-a\bar n/c)
   \]
   or their trilinear variants **before** a Cauchy step destroys the phase.

This is precisely the shape for which the DFI / Bettin--Chandee / Pratt--Robles line of Kloosterman-fraction estimates is relevant.

A 2026 preprint of Dong--Robles--Zeindler gives stronger bilinear Kloosterman-fraction bounds, but its claimed improved twisted-second-moment application was subsequently withdrawn because of a missing logarithmic factor. The bilinear theorem may still be useful here, but no exponent gain is imported from that withdrawn application.

## 6. Next analytic milestone

The next target is to derive a dyadic model sum from the rewritten equation (11) of the form

\[
\mathcal E(K,C,M,D)
=
\sum_{c\sim C}
\sum_{n\sim N,(n,c)=1}
\alpha_n\beta_c
\sum_{m\sim M}\gamma_m
 e\left(-\frac{dm\bar n}{c}\right),
\]

with all norms and parameter relations inherited explicitly from Bui--Heath--Brown.

Only after this model is exact should a modern bilinear/trilinear estimate be inserted. The quantitative goal is a replacement of the old large-modulus bound by

\[
yT^{1/2-\delta_1+ε}
+y^{1/2}T^{3/4-\delta_2+ε}
\]

with `min(delta_1, 2 delta_2)>0`.
