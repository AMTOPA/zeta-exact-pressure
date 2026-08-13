# Arithmetic-shape mollifier direction

Status: **discovery / analytic development only**. Nothing in this directory changes the root certified record.

This experiment deliberately leaves the exact-pressure / pair-correlation route. The new target is the discrete mollified-derivative method of Conrey--Ghosh--Gonek and Bui--Heath-Brown, whose scalar Möbius mollifier gives the RH-conditional simple-zero proportion `19/27`.

Primary references:

- H. M. Bui and D. R. Heath-Brown, *On simple zeros of the Riemann zeta-function*, arXiv:1302.5018 / Bull. Lond. Math. Soc. 45 (2013), 953--961.
- J. B. Conrey, A. Ghosh and S. M. Gonek, *Simple Zeros of the Riemann Zeta-Function*, Proc. Lond. Math. Soc. 76 (1998), 497--522.
- H. M. Bui, *Critical zeros of the Riemann zeta-function*, arXiv:1410.2433, for examples of genuinely different multi-piece mollifier arithmetic in a related continuous-moment setting.

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

The Cauchy lower bound is therefore

\[
\mathcal R(P,\vartheta)=\frac{U(P,\vartheta)^2}{Q(P,\vartheta)}.
\]

### Exact scalar ceiling

For fixed `I`, the least possible Dirichlet energy among `H^1` functions with

\[
P(0)=0,\qquad P(1)=1,\qquad \int_0^1P=I
\]

is attained by the quadratic

\[
P_I(x)=(3-6I)x^2+(6I-2)x
\]

and equals

\[
K_{\min}=4(3I^2-3I+1).
\]

Substituting this into the quotient and optimizing over `I` gives

\[
I_*(\vartheta)=\frac{3+\vartheta}{6},
\]

hence

\[
P_*(x)=-\vartheta x^2+(1+\vartheta)x,
\]

and the exact optimum

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

Therefore the whole scalar family with `theta < 1/2` has the sharp limiting ceiling

\[
\boxed{
\lim_{\vartheta\to1/2^-}\mathcal R_*(\vartheta)
=\frac{19}{27}=0.703703\ldots
}.
\]

At `theta = 1/2`, formally,

\[
P_*(x)=-\tfrac12x^2+\tfrac32x,
\quad I=\tfrac7{12},
\quad K=\tfrac{13}{12},
\quad U=\tfrac{19}{24},
\quad Q=\tfrac{57}{64},
\]

so `U^2/Q = 19/27` exactly.

`check_scalar_ceiling.py` checks these rational identities.

## 2. A false vector direction: `mu * Lambda`

The initially tempting second basis vector

\[
(\mu*\Lambda)(n)
\]

is not new. The exact convolution identity is

\[
\boxed{(\mu*\Lambda)(n)=-\mu(n)\log n}.
\]

Thus, at a common cutoff `y`, any piece

\[
(\mu*\Lambda)(n)P_1(\nu_n)
\]

is just `mu(n)` times another one-variable weight in `nu_n`, because

\[
\frac{\log n}{\log y}=1-\nu_n.
\]

It is already contained in the scalar variational class above. The same warning applies to any finite number of reciprocal-derivative pieces that reduce to `mu(n)` times powers of `log n` at the same cutoff.

So a genuine improvement must either

1. see arithmetic information not determined by `log n` alone; or
2. break the `theta = 1/2` length barrier.

## 3. First genuine enlargement: prime-shape directions

The Bui--Heath-Brown RH-only treatment uses the fact that the mollifier coefficients are supported on squarefree integers in its initial cleaning of the large-modulus character sums. This makes it attractive to keep the `mu(n)` support but enlarge the coefficient geometry inside the squarefree integers.

For squarefree `n`, define

\[
R_j(n;y)=\sum_{p\mid n}
\left(\frac{\log p}{\log y}\right)^j.
\]

`R_1(n;y)=log(n)/log(y)` contains no new information, but `R_j` for `j >= 2` records how the logarithmic mass of `n` is distributed among its prime factors and cannot be recovered from `n`'s total logarithm.

The first test family is

\[
B_0(s)=\sum_{n\le y}
\frac{\mu(n)P_*(\nu_n)}{n^s},
\]

\[
B_2(s)=\sum_{n\le y}
\frac{\mu(n)\,\nu_n(1-\nu_n)R_2(n;y)}{n^s}.
\]

For a vector mollifier `B = alpha_0 B_0 + alpha_2 B_2`, if asymptotics

\[
S_{1,j}\sim u_j\frac{T\mathcal L^2}{2\pi},
\qquad
S_{2,ij}\sim Q_{ij}\frac{T\mathcal L^3}{2\pi}
\]

can be proved, the optimized Cauchy quotient is the Rayleigh value

\[
\boxed{u^*Q^{-1}u}.
\]

This is the quantity the analytic work should target. It is not enough for a new basis direction merely to improve a finite numerical fit.

## 4. Finite-zero go/no-go probe

`finite_zero_probe.py` is intentionally **not a proof tool**. It evaluates `zeta'(rho) B_j(rho)` at the first `N` numerical zeta zeros and compares the scalar and two-dimensional finite-sample Rayleigh quotients.

With `theta = 0.49` the current local probe gave:

| zeros | scalar `B0` | `B0 + B2` optimized |
|---:|---:|---:|
| 100 | 0.905686 | 0.914177 |
| 150 | 0.903418 | 0.911866 |
| 200 | 0.895672 | 0.905687 |

The absolute values are strongly finite-height biased and must not be read as asymptotic simple-zero proportions. The useful observation is only that the sign of the `R2` gain is stable in these truncations. Tests at `theta = 0.35, 0.40, 0.45` also gave a positive finite-sample gain.

This is enough to justify deriving the **asymptotic first variation** of the discrete moments in a prime-shape direction. It is not enough to claim any improvement over `19/27`.

## 5. Next analytic target

The next go/no-go calculation is deliberately narrow:

1. perturb the optimal scalar coefficient by
   \[
   b_\lambda(n)=\mu(n)\left[P_*(\nu_n)+\lambda\,\nu_n(1-\nu_n)R_2(n;y)\right];
   \]
2. derive the `q=1` residue/main-term first variation of `S1` and `S2` at `lambda = 0`;
3. evaluate
   \[
   \left.\frac{d}{d\lambda}\frac{U(\lambda)^2}{Q(\lambda)}\right|_{\lambda=0};
   \]
4. continue only if that derivative is genuinely nonzero in a favorable direction (or, if the first derivative vanishes, if the second variation has a positive generalized eigenvalue);
5. separately audit whether the Bui--Heath-Brown generalized-Vaughan error estimate survives the extra divisor-log factors. Squarefree support is preserved, but this compatibility is not assumed until checked line by line.

A positive formal variation would identify a real new arithmetic degree of freedom beyond the sharp scalar `19/27` ceiling. A zero/negative variation would terminate this prime-shape family before any large proof effort.
