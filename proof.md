# Current deduction outline

> **Certified baseline:** the current root seven-point / six-gap certificate has interval-verified `epsilon = 0.0079107` and `H > 0.6721881580`. Under the inherited scalar Gram profile this gives **67.3416490971%** before truncation, with safe floor `0.6734164909`.
>
> **Analytic extension under review:** retaining six-band Gram energy gives a proposed continuous profile and an exact projection to **67.3423563564%**. The local numerical input is interval-certified, but the new matrix lemma is not yet promoted to the root result.

## 1. Imported analytic interface

Let \(S=N_0^s(T,2T)\) and \(N=N(T,2T)\). The lineage framework supplies

\[
S\ge HN+\Delta(M)-o(N),
\]

and the unrestricted finite-dimensional Gram profile

\[
h_m(E)=
\begin{cases}
E,&E\le m/(m-1),\\
E/m+2\sqrt{(m-1)E/m}-1,&E\ge m/(m-1).
\end{cases}
\]

For a PSD Gram block \(G\),

\[
E=2\sum_{i<j}|G_{ij}|^2,
\qquad
\Delta(G)=\operatorname{tr}\Psi(G),
\]

where

\[
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
\]

The unrestricted profile is sharp if only total off-diagonal energy is retained.

## 2. Certified 17-term window

Use

\[
v(s)=\sum_{j=0}^{16}c_j\cos(\omega_js),
\qquad
\omega_0=\sqrt2,
\quad \omega_j=2j\pi\;(1\le j\le16),
\]

with denominator \(10^9\) and numerator vector

```text
1000000000,
12378982,
-12602495,
4164033,
5741405,
-1724025,
6219280,
-8047828,
6321519,
-5241981,
-892658,
560544,
-431207,
357969,
-310433,
100000,
-100000
```

Outward-rounded interval arithmetic encloses

\[
H(v)=0.6721881581182345851694563877256548\ldots
\]

and proves

\[
\boxed{H(v)>0.6721881580}.
\]

The same interval subdivision proves a positive window lower bound above `0.7616418486`.

## 3. Certified local inequality

For six nonnegative gaps, put \(y_0=0\) and \(y_j=g_1+\cdots+g_j\), and define

\[
F(g)=\sum_{r=1}^{6}b_rg_r+
\sum_{0\le i<j\le6}a_{ij}W(y_j-y_i).
\]

The exact pair weights in `candidate.json` are nonnegative and satisfy

\[
\sum_{i=0}^{6-s}a_{i,i+s}=2
\qquad(1\le s\le6).
\]

The exact position-pressure vector is

\[
\frac1{46000000000}
(22420713,32878293,37700994,37700994,32878293,22420713),
\]

so

\[
\boxed{B=\sum b_r=\frac{93}{23000}}.
\]

The second adversarial exchange found a floating minimum

\[
0.007911105155226424\ldots.
\]

The hardened outward-rounded verifier proves

\[
\boxed{F(g_1,\ldots,g_6)\ge0.0079107}
\qquad(g_i\ge0).
\]

The successful run records

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

The run uses grid `1/4000`, 50 decimal digits for table construction, and `-ffp-contract=off`.

## 4. Existing scalar-Gram deduction

Summing the \(m-6\) translated local inequalities gives

\[
E+B\,\operatorname{span}(B)\ge
A_m:=\varepsilon(m-6).
\]

Set

\[
R_m=h_m(A_m),
\qquad
\eta_m=R_m/A_m.
\]

Concavity and monotonicity of \(h_m\), followed by the inherited shifted-block pinching and averaging, give

\[
\frac SN\ge
\frac{mH-\eta_mB(m-6)}{m-R_m}-o(1).
\]

Using the certified conservative inputs

\[
H=0.6721881580,
\qquad
\varepsilon=0.0079107,
\qquad
B=\frac{93}{23000},
\]

the integer scan selects \(m=145\) and gives

\[
\boxed{0.67341649097149929495\ldots},
\]

hence the safe root statement

\[
\boxed{
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
>0.6734164909
}.
\]

This is **67.3416490971%** before truncation.

## 5. New band-position-aware Gram profile

The translated certificate contains more information than total energy: it only uses pairs of index span at most six. For general bandwidth \(q\), define

\[
E_q=2\sum_{1\le j-i\le q}|G_{ij}|^2,
\qquad
T_q=\frac{q+1}{q}.
\]

The analytic-extension experiment proposes

\[
\boxed{
\Delta(G)\ge g_q(E_q)
}
\]

with

\[
g_q(E)=
\begin{cases}
E,&E\le T_q,\\
2\sqrt{T_qE}-T_q,&E\ge T_q.
\end{cases}
\]

A proof is given in `experiments/banded-gram/README.md`. Its two ingredients are:

1. coloring the q-band graph by residues modulo \(q+1\), giving
   \[
   \|Y\|_{\rm op}^2\le \frac{q}{q+1}E_q;
   \]
2. the identity
   \[
   \Delta(G)=\|G-I\|_F^2-\|(G-2I)_+\|_F^2,
   \]
   together with the Frobenius distance to the negative-semidefinite cone.

The resulting \(g_q\) is increasing, concave, and satisfies \(g_q(0)=0\), so if

\[
E_q+P\ge A,
\]
then with \(R=g_q(A)\) and \(\eta=R/A\),

\[
\Delta+\eta P\ge R.
\]

Thus the inherited shifted-block step has exactly the same algebraic form, with \(h_m\) replaced by \(g_q\).

## 6. Exact banded-Gram projection under review

For the certified local input, take \(q=6\) and \(m=165\). Then

\[
A=0.0079107\times159
=\frac{12578013}{10000000}.
\]

Rather than use a floating square root, take

\[
R_{\rm floor}=1.2560878
=\frac{6280439}{5000000}.
\]

The exact checker verifies

\[
\frac76A-
\left(\frac{R_{\rm floor}+7/6}{2}\right)^2
=
\frac{43705511}{900000000000000}>0,
\]

so \(R_{\rm floor}<g_6(A)\). With

\[
\eta=\frac{R_{\rm floor}}A
=\frac{12560878}{12578013},
\]

the final exact ratio is

\[
\frac{607970185271419}{902805037076740}
=0.6734235635636362491\ldots.
\]

Therefore the analytic extension projects to

\[
\boxed{67.3423563564\%}
\]

with safe floor `0.6734235635`.

**This number is not yet the root certified record.** The local numerical certificate is rigorous and the final arithmetic is exact, but the new banded-Gram lemma and its insertion into the inherited pinching argument require independent mathematical review.

## 7. Current research direction

A same-window 7-point / 8-point mixture was tested first. Under the scalar \(A\mapsto h_m(A)\) compression the optimizer selected an endpoint, so mixing geometries did not break the bottleneck.

The next experiment therefore keeps multiple lag constraints instead of a single scalar local inequality. In particular, a second certificate with odd span capacities scaled by \(1+\delta\) and even spans by \(1-\delta\) can constrain how much of the local lower bound is paid by band energy versus the linear pressure term. This is a controlled step toward a multi-lag SDP while retaining an auditable finite-dimensional proof structure.

## Trust boundary

Directly checked here: the 17-term interval window bound, positivity, exact local coefficients and pressure total, the six-dimensional local certificate, the existing scalar-Gram final arithmetic, and the exact rational arithmetic of the banded experiment.

Imported from the lineage: the explicit-formula / trace interface and shifted-block pinching/averaging framework. New and still under review: the banded-Gram matrix profile and any multi-lag extension built on top of it.
