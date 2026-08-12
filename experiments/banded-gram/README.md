# Banded-Gram analytic extension

Status: **analytic-extension research candidate**.  The local 17-term six-gap certificate used here is interval-certified.  The new matrix lemma below is an analytic step and should receive independent human review before this experiment replaces the root certified record.

## Why this direction

The scalar Gram profile used by the predecessor keeps only the total off-diagonal energy

\[
E=2\sum_{i<j}|G_{ij}|^2,
\]

then applies the sharp unrestricted profile \(\Delta\ge h_m(E)\), where \(\Delta=\operatorname{tr}\Psi(G)\).  That profile is sharp if *only* total energy is known, so further parameter squeezing cannot improve this step.

The translated seven-point certificate contains more information: it only uses pairs whose index span is at most six.  Therefore define the six-band energy

\[
E_6=2\sum_{1\le j-i\le6}|G_{ij}|^2.
\]

Because every local pair-span capacity is at most 2, summing the translated local inequalities gives

\[
E_6+B\,\operatorname{span}(B)\ge A,
\qquad A=\varepsilon(m-6),
\]

without first replacing \(E_6\) by the full off-diagonal energy.

## Banded-Gram lemma

Let \(G\succeq0\) be an \(m\times m\) Hermitian Gram matrix with \(G_{ii}\le1\), and let

\[
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
\]

For an integer \(q\ge1\), set

\[
E_q=2\sum_{1\le j-i\le q}|G_{ij}|^2.
\]

Then

\[
\boxed{
E_q\le\frac{q+1}{q}
\quad\Longrightarrow\quad
\operatorname{tr}\Psi(G)\ge E_q.
}
\]

### Proof

Write \(X=G-I\), and split

\[
X=Y+Z,
\]

where \(Y\) keeps exactly the off-diagonal entries with \(1\le |i-j|\le q\), and \(Z\) contains the diagonal and all farther entries.  The supports are disjoint, hence

\[
\|Y\|_F^2=E_q,
\qquad
\|X\|_F^2=\|Y\|_F^2+\|Z\|_F^2.
\]

For a unit vector \(x\), put \(p_i=|x_i|^2\).  Color the indices by their residues modulo \(q+1\).  Every band edge joins two different colors.  If \(P_c\) is the total \(p_i\)-mass in color class \(c\), then

\[
\sum_{1\le j-i\le q}p_ip_j
\le
\sum_{c<d}P_cP_d
=
\frac12\left(1-\sum_cP_c^2\right)
\le
\frac{q}{2(q+1)}.
\]

Cauchy--Schwarz therefore gives

\[
|x^*Yx|^2
\le
E_q\,\frac{q}{q+1}.
\]

Thus if \(E_q\le(q+1)/q\), then \(\|Y\|_{\rm op}\le1\), so \(Y-I\preceq0\).

Eigenvalue by eigenvalue,

\[
\Psi(\lambda)
=(\lambda-1)^2-(\lambda-2)_+^2,
\]

hence

\[
\operatorname{tr}\Psi(G)
=
\|G-I\|_F^2-\|(G-2I)_+\|_F^2.
\]

Now

\[
G-2I=(Y-I)+Z.
\]

The Frobenius norm of the positive part is the distance to the cone of negative-semidefinite Hermitian matrices.  Since \(Y-I\preceq0\),

\[
\|(G-2I)_+\|_F
\le\|Z\|_F.
\]

Consequently

\[
\operatorname{tr}\Psi(G)
\ge
\|Y\|_F^2+\|Z\|_F^2-\|Z\|_F^2
=E_q.
\]

This proves the lemma.

## Combination with the existing scalar profile

The unrestricted predecessor theorem still gives

\[
\operatorname{tr}\Psi(G)\ge h_m(E_{\rm total}),
\qquad E_{\rm total}\ge E_q.
\]

Let

\[
T_q=\frac{q+1}{q}.
\]

Suppose the translated local certificate gives

\[
E_q+B\,\operatorname{span}(B)\ge A
\]

and that

\[
A<T_q,
\qquad
h_m(T_q)>A.
\]

If \(E_q\le T_q\), the banded lemma gives \(\Delta\ge E_q\), hence \(\Delta+B\operatorname{span}(B)\ge A\).  If \(E_q>T_q\), monotonicity of the unrestricted profile gives

\[
\Delta\ge h_m(E_{\rm total})\ge h_m(T_q)>A.
\]

Therefore in all cases

\[
\boxed{\Delta+B\operatorname{span}(B)\ge A.}
\]

In the shifted-block deduction this means we may use

\[
R=A,\qquad \eta=1,
\]

instead of \(R=h_m(A)\), \(\eta=R/A\).

## Current numerical input

The second-exchange 17-term local certificate has now closed in the hardened outward-rounded verifier:

\[
H>0.6721881580,
\qquad
\varepsilon=0.0079107,
\qquad
B=\frac{93}{23000}.
\]

Verifier evidence:

```text
workflow run = 31610179703
artifact id = 9147378469
artifact digest sha256 = 871532c739d5a9e8de770cf00675381ea4fd9c81f212d8e46f86403a27a34dc1
VERIFIED=true
nodes=3768186
pruned=1884125
splits=1884061
convex=2030240
tangent=936616
max_depth=74
```

Take \(q=6\) and \(m=152\).  Then

\[
A=0.0079107\times146
=1.1549622
=\frac{5774811}{5000000},
\]

while

\[
T_6=\frac76=1.1666\ldots.
\]

The exact checker verifies \(h_{152}(7/6)>A\) by squaring the single positive square-root comparison; the resulting rational square gap is

\[
\frac{2040735610367471}{324900000000000000}>0.
\]

Thus the strengthened block deduction uses \(R=A\) and \(\eta=1\).  The exact final ratio is

\[
\frac{292048975046}{433679483675}
=0.6734212385865638563170612269568\ldots,
\]

or

\[
\boxed{67.34212385865638\ldots\%}.
\]

A safe ten-decimal floor is

\[
\boxed{0.6734212385}.
\]

This is about **0.00059246 percentage points** above the current root record 67.3415313957%.

## Reproduce the exact arithmetic

Run

```bash
python3 src/check_banded_gram.py
```

or `sh run.sh` after this experiment is wired into the normal arithmetic checks.

## Trust boundary

The 17-term local inequality and its window floor are interval-certified.  The calculations from the banded lemma to the displayed rational bound are exact.  The only genuinely new non-computational step is the banded-Gram lemma and its insertion into the predecessor shifted-block/pinching argument.  That step should be independently reviewed before root promotion.
