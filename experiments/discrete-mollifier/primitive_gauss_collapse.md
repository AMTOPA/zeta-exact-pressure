# Exact collapse of the signed primitive-character family

Status: **exact finite character/arithmetic identities proved below; application to
a modern Kloosterman theorem still requires numerator/range separation.**

This note removes one of the main ambiguities in Gate C.  The primitive-character
and Gauss-sum part of Bui--Heath-Brown equation (5) can be collapsed **before taking
absolute values** because the mollifier forces the conductor modulus to be
squarefree.

## 1. Squarefree setup from the BHB mollifier

BHB use

\[
b(n)=\mu(n)P(\log(y/n)/\log y).
\]

Hence a nonzero term `b(kq)` forces `kq` to be squarefree.  In particular

\[
q\text{ is squarefree},\qquad(k,q)=1.
\]

Their initial cleaning also reduces to `d|k`, so

\[
(d,q)=1.
\]

For an inner term with `psi(m) != 0` one also has `(m,q)=1`.

## 2. Primitive orthogonality

For `(u,q)=1`, primitive-character orthogonality gives

\[
\boxed{
\sum_{\chi\bmod q}^{*}\chi(u)
=
\sum_{s\mid(q,u-1)}\phi(s)\mu(q/s).
}
\]

Therefore, for `(a x,q)=1`,

\[
\sum_{\chi\bmod q}^{*}\chi(a)\bar\chi(x)
=
\sum_{\substack{s\mid q\\x\equiv a\pmod s}}
\phi(s)\mu(q/s).
\]

## 3. Primitive Gauss collapse for squarefree q

Define

\[
G_q(a)=\sum_{\chi\bmod q}^{*}\tau(\bar\chi)\chi(a),
\qquad(a,q)=1.
\]

Expanding the Gauss sum and using primitive orthogonality,

\[
G_q(a)
=
\sum_{s\mid q}\phi(s)\mu(q/s)
\sum_{\substack{x\bmod q\\(x,q)=1\\x\equiv a\pmod s}}
e(x/q).
\]

Write

\[
q=se.
\]

Since `q` is squarefree, `(s,e)=1`.  Chinese remaindering gives

\[
e(x/q)
=e(a\bar e/s)e(x_e\bar s/e),
\]

where `x_e` ranges through the units modulo `e`.  Hence

\[
\sum_{\substack{x\bmod q\\(x,q)=1\\x\equiv a\pmod s}}e(x/q)
=e(a\bar e/s)c_e(1)
=\mu(e)e(a\bar e/s).
\]

But the primitive-orthogonality coefficient is also `mu(e)`.  Since `e` is
squarefree,

\[
\mu(e)^2=1.
\]

Thus

\[
\boxed{
G_q(a)=
\sum_{s\mid q}\phi(s)
 e\!\left(\frac{a\,\overline{q/s}}{s}\right).
}
\]

This identity is exact.  `primitive_gauss.py` numerically sanity-checks it for all
squarefree `q<=120`, but the proof above is the actual justification.

## 4. The BHB delta factor has one character argument

BHB equation (6) is

\[
\delta(q,kq,d,\psi)
=
\sum_{l\mid(d,k)}
\frac{\mu(d/l)}{\phi(kq/l)}
\bar\psi(-k/l)\psi(d/l)\mu(k/l).
\]

Multiplying by the `psi(m)` in equation (5), and using `(kdl,q)=1`, gives

\[
\bar\psi(-k/l)\psi(d/l)\psi(m)
=
\boxed{\psi(-md\,\bar k)}.
\]

The `l` dependence disappears completely from the character argument.  Therefore

\[
\sum_{\psi\bmod q}^{*}\tau(\bar\psi)
\delta(q,kq,d,\psi)\psi(m)
=
C(q,k,d)\,G_q(-md\bar k),
\]

with

\[
C(q,k,d)=
\sum_{l\mid d}
\frac{\mu(d/l)\mu(k/l)}{\phi(kq/l)}.
\]

## 5. The l-sum also collapses exactly

Because `k` is squarefree and `d|k`, for every `l|d`

\[
\mu(d/l)\mu(k/l)=\mu(d)\mu(k).
\]

Write `k=dc` with `(c,d)=1`.  Multiplicativity gives

\[
\sum_{l\mid d}\frac1{\phi(k/l)}
=
\frac1{\phi(c)}
\prod_{p\mid d}\left(1+\frac1{p-1}\right)
=
\frac{d}{\phi(k)}.
\]

Since `(q,k)=1`, it follows that

\[
\boxed{
C(q,k,d)=
\mu(k)\mu(d)\frac{d}{\phi(k)\phi(q)}.
}
\]

This identity is exact and is checked with rational arithmetic in
`primitive_gauss.py`.

Multiplying by the original mollifier coefficient

\[
\frac{b(kq)}{kq}
=
\frac{\mu(k)\mu(q)}{kq}
P\!\left(\frac{\log(y/kq)}{\log y}\right)
\]

cancels `mu(k)^2`.  Now write `q=se`.  The `phi(s)` from the Gauss collapse cancels
against the same factor in `phi(q)=phi(s)phi(e)`.  Thus each divisor-phase term has
exact arithmetic coefficient

\[
\boxed{
P\!\left(\frac{\log(y/kse)}{\log y}\right)
\frac{\mu(s)\mu(e)\mu(d)d}
{k\,s\,e\,\phi(k)\phi(e)}
}
\]

multiplying

\[
\boxed{
e\!\left(-md\frac{\overline{ke}}s\right)}.
\]

This exposes the signed structure that equation (13) discards.  In particular the
large reciprocal modulus `s` carries the natural Möbius weight

\[
\boxed{\mu(s)/s}.
\]

So the hard object is not an arbitrary positive character norm: it is a
Möbius-weighted Kloosterman-fraction family with only short additional arithmetic
parameters.

## 6. Additive reciprocity and Wright's phase shape

Because `(ke,s)=1`, additive reciprocity gives

\[
\frac{\overline{ke}}s+rac{\bar s}{ke}
\equiv\frac1{kes}\pmod1.
\]

Therefore

\[
\boxed{
 e\!\left(-md\frac{\overline{ke}}s\right)
=
 e\!\left(md\frac{\bar s}{ke}\right)
 e\!\left(-\frac{md}{kq}\right).
}
\]

The first factor has exactly the partially-fixed-modulus Kloosterman shape

\[
e\!\left(\vartheta\frac{a\bar m}{Rn}\right)
\]

studied in Wright's 2026 theorem, under the formal dictionary

\[
\boxed{
m_{\rm W}=s,\qquad n_{\rm W}=e,\qquad R_{\rm W}=k,
\qquad a_{\rm W}=md.}
\]

The short BHB outer factor `k` appears in precisely the fixed factor `R` of the
reciprocal denominator.

## 7. The remaining obstruction to a black-box Wright application

The dictionary above does **not** prove Gate C.  Two important couplings remain.

### 7.1 Large numerator/product coupling

The formal Wright numerator would be

\[
a_{\rm W}=md,
\]

whose natural scale is tied to the whole BHB product.  A direct substitution into
Wright's trilinear bound may pay a bad factor through the theorem's dependence on
`A/(MN)`.

Thus one must first use the generalized-Vaughan factorization, Poisson, or another
convolution split so that the oscillatory numerator variable entering the trilinear
Kloosterman estimate is a controlled factor rather than the entire `md` product.

### 7.2 Reciprocity correction

The second exact factor

\[
e(-md/(kq))
\]

is the original high-frequency additive phase.  It cannot simply be discarded or
absorbed into a coefficient independent of the other Kloosterman variables.

Analytic smoothing localizes the ratio `md/(kq)` to a short interval around the
external height, so this factor should be treated together with the entire saddle
weight.  A successful application needs a separation transform whose cost is
compatible with the desired `theta=0.502` power saving.

## 8. Revised Gate-C subproblem

The primitive-character and arithmetic simplification is now exact.  The next
subproblem is narrower:

> Starting from the Möbius-weighted divisor-phase formula above and an `r=4`
> convolution of `a_nu`, separate the product `md` and the smooth correction
> `e(-md/(kq))Omega(md/(kq))` so that one trilinear piece matches Wright's
> `B(M,N,A;R)` with `R=k`, while retaining `mu(s)/s` rather than taking absolute
> values.

If this separation can be done with only polylogarithmic or a sufficiently small
power cost, Wright's fixed-factor theorem becomes a concrete candidate input rather
than a merely analogous result.
