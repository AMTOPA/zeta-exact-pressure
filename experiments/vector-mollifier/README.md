# Arithmetic-shape mollifier direction

Status: **discovery / analytic development only**. Nothing in this directory changes the root certified record.

This experiment deliberately leaves the exact-pressure / pair-correlation route. The new target is the discrete mollified-derivative method of Conrey--Ghosh--Gonek and Bui--Heath-Brown, whose scalar Möbius mollifier gives the RH-conditional simple-zero proportion `19/27`.

Primary references:

- H. M. Bui and D. R. Heath-Brown, *On simple zeros of the Riemann zeta-function*, arXiv:1302.5018 / Bull. Lond. Math. Soc. 45 (2013), 953--961.
- J. B. Conrey, A. Ghosh and S. M. Gonek, *Simple Zeros of the Riemann Zeta-Function*, Proc. Lond. Math. Soc. 76 (1998), 497--522.
- S. Feng, *Zeros of the Riemann zeta function on the critical line*, arXiv:1003.0059. The setting there is Levinson--Conrey rather than the present discrete-zero method, but Feng's coefficient geometry supplies a genuinely new squarefree arithmetic direction.
- H. M. Bui, *Critical zeros of the Riemann zeta-function*, arXiv:1410.2433, for related multi-piece mollifier arithmetic and explicit cautions about admissible mollifier lengths.

## 1. Scalar discrete-mollifier baseline

For

\[
B(s)=\sum_{k\le y}\frac{\mu(k)P(u_k)}{k^s},
\qquad
u_k:=\frac{\log(y/k)}{\log y},
\qquad y=T^\vartheta,
\]

Bui--Heath-Brown obtain, for `0 < theta < 1/2`, the normalized first- and second-moment main terms

\[
U(P,\vartheta)=\frac12+\vartheta I,
\]

and

\[
Q(P,\vartheta)
=\frac13+\vartheta I+\vartheta^2I^2
 +\frac{K}{12\vartheta},
\]

where

\[
I=\int_0^1P(u)\,du,
\qquad
K=\int_0^1(P'(u))^2\,du.
\]

The Cauchy lower bound is

\[
\mathcal R(P,\vartheta)=\frac{U(P,\vartheta)^2}{Q(P,\vartheta)}.
\]

### Exact scalar ceiling

For fixed `I`, the least possible Dirichlet energy among `H^1` functions satisfying

\[
P(0)=0,\qquad P(1)=1,\qquad \int_0^1P=I
\]

is attained by

\[
P_I(x)=(3-6I)x^2+(6I-2)x
\]

and equals

\[
K_{\min}=4(3I^2-3I+1).
\]

Substitution and optimization over `I` give

\[
I_*(\vartheta)=\frac{3+\vartheta}{6},
\qquad
P_*(x)=-\vartheta x^2+(1+\vartheta)x,
\]

and

\[
\boxed{
\mathcal R_*(\vartheta)
=\frac{\vartheta(\vartheta^2+3\vartheta+3)}{(1+\vartheta)^3}
}.
\]

Moreover

\[
\frac{d}{d\vartheta}\mathcal R_*(\vartheta)
=\frac{3}{(1+\vartheta)^4}>0.
\]

Thus the full one-variable Möbius-weight class with `theta < 1/2` has the sharp limiting ceiling

\[
\boxed{
\lim_{\vartheta\to1/2^-}\mathcal R_*(\vartheta)
=\frac{19}{27}=0.703703\ldots
}.
\]

At the formal endpoint `theta=1/2`,

\[
I=\tfrac7{12},\quad K=\tfrac{13}{12},\quad
U=\tfrac{19}{24},\quad Q=\tfrac{57}{64},
\]

and `U^2/Q = 19/27` exactly. `check_scalar_ceiling.py` verifies these rational identities.

This is an important filter: adding more polynomial degrees, more pieces with the same Möbius arithmetic, or different shorter cutoffs that merely produce another one-variable weight cannot create a new asymptotic degree of freedom.

## 2. A false vector direction: `mu * Lambda`

The initially tempting basis vector `(mu * Lambda)(n)` is not new. Exactly,

\[
\boxed{(\mu*\Lambda)(n)=-\mu(n)\log n}.
\]

At a common cutoff `y`, multiplying it by a polynomial in `nu_n` merely gives `mu(n)` times another one-variable function, because

\[
\frac{\log n}{\log y}=1-\nu_n.
\]

It is already contained in the scalar class above. The same warning applies to reciprocal-derivative pieces that reduce to `mu(n)` times powers of `log n`.

A real improvement must therefore either see arithmetic information not determined by `log n` alone, or break the `theta=1/2` length barrier.

## 3. Genuine arithmetic enlargement: Feng prime-tuple shape

Feng's mollifier introduces terms of the form

\[
\mu(n)
\sum_{p_1p_2\mid n}
\frac{\log p_1\log p_2}{\log^2 y}
P_2(\nu_n),
\]

and higher prime tuples. For the present discrete-zero problem, define the normalized elementary two-prime statistic

\[
E_2(n;y)=
\sum_{p<q,\;pq\mid n}
\frac{\log p\log q}{\log^2 y}
\qquad(n\ \hbox{squarefree}).
\]

This is genuinely different from a scalar weight. For comparison,

\[
\left(\frac{\log n}{\log y}\right)^2
=
\sum_{p\mid n}\left(\frac{\log p}{\log y}\right)^2
+2E_2(n;y),
\]

so the earlier power-sum `R2` direction differs from `E2` only by a scalar one-variable component. `E2` is therefore the cleaner coordinate for the new arithmetic degree of freedom.

The first discrete Feng-shape family is

\[
B_0(s)=\sum_{n\le y}\frac{\mu(n)P_0(\nu_n)}{n^s},
\]

\[
B_2(s)=\sum_{n\le y}
\frac{\mu(n)P_2(\nu_n)E_2(n;y)}{n^s}.
\]

For `B = alpha_0 B_0 + alpha_2 B_2`, if one proves mixed discrete moment asymptotics

\[
S_{1,j}\sim u_j\frac{T\mathcal L^2}{2\pi},
\qquad
S_{2,ij}\sim Q_{ij}\frac{T\mathcal L^3}{2\pi},
\]

then optimizing the mollifier coefficients is exactly the Rayleigh problem

\[
\boxed{u^*Q^{-1}u}.
\]

The point is not the linear algebra; the new research content is deriving `u` and `Q` with a genuinely arithmetic `E2` basis while retaining an RH-only error analysis.

### Why this is a plausible transplant

Bui--Heath-Brown's large-modulus cleanup explicitly uses that their `b(*)` is supported on squarefree integers. The Feng-shape deformation keeps the outer `mu(n)`, hence keeps squarefree support. Its extra prime-log factors grow only polylogarithmically. This makes compatibility with the generalized-Vaughan error mechanism plausible, but **not proved**; the proof must be audited rather than assumed.

By contrast, directly importing a `mu_2` / `1/zeta^2` piece loses the squarefree property at exactly the place where the RH-only Bui--Heath-Brown argument uses it, so it is not the first target here.

## 4. Finite-zero go/no-go probe

`finite_zero_probe.py` is deliberately non-rigorous. It evaluates `zeta'(rho) B_j(rho)` at the first `N` numerical zeta zeros. To avoid falsely crediting the arithmetic piece for ordinary finite-height reoptimization of `P`, the baseline is a scalar polynomial subspace `mu(n) u^k`, not a single fixed quadratic.

The default arithmetic direction is

\[
\mu(n)\,u(1-u)E_2(n;y).
\]

With scalar degree 3 and `theta=0.49`, the current probe gives:

| zeros | scalar polynomial subspace | plus `E2` |
|---:|---:|---:|
| 100 | 0.917875 | 0.918818 |
| 150 | 0.916711 | 0.919912 |
| 200 | 0.908762 | 0.913773 |

At `theta=0.35, 0.40, 0.45` the incremental `E2` gain is also positive for `N=100,150,200` in the current probe.

The absolute values are strongly finite-height biased, the cutoff is tiny at these heights, and the matrices can be ill-conditioned. **These numbers are not asymptotic simple-zero predictions.** Their only use is as a sign test showing that the arithmetic coordinate is not immediately redundant after allowing scalar polynomial reoptimization.

## 5. Next analytic target: first variation at `19/27`

The next calculation is a strict go/no-go test, not a large proof project.

Take the scalar optimum `P_*` and perturb it in one Feng direction,

\[
b_\lambda(n)=\mu(n)
\left[P_*(\nu_n)+\lambda P_2(\nu_n)E_2(n;y)\right].
\]

The immediate task is:

1. derive the `q=1` residue/main-term first variation of the discrete first moment `S1` at `lambda=0`;
2. derive the mixed first variation of the discrete second moment `S2`;
3. evaluate the derivative of the optimized quotient at the scalar `19/27` extremizer;
4. if the first variation vanishes for structural reasons, compute the two-dimensional Hessian / generalized eigenvalue instead;
5. continue only if the enlarged main-term quadratic form has a direction strictly above `19/27`;
6. only then audit the large-modulus generalized-Vaughan estimates with the prime-tuple weights.

This ordering is intentional. A favorable main-term variation would show that the `19/27` barrier belongs to the scalar coefficient geometry, not to the entire discrete-derivative method. A nonpositive variation would kill the first Feng-shape family before any expensive error-term work.
