# Discrete zeta-prime mollifier research pivot

Status: **active analytic research direction; no new theorem or root record is claimed here.**

The exact-pressure / pair-correlation line remains reproducible in the repository, but it is no longer the primary optimization target.  This directory studies a genuinely different detector for simple zeros: discrete mollified moments of `zeta'(rho)`.

## 1. Starting inequality

For any regular function `B(s)`, a multiple zero `rho` has `zeta'(rho)=0`.  Hence Cauchy gives

\[
N^*(T)\ge
\frac{\left|\sum_{0<\gamma\le T}B(\rho)\zeta'(\rho)\right|^2}
{\sum_{0<\gamma\le T}|B(\rho)\zeta'(\rho)|^2}.
\]

Bui--Heath-Brown, *On simple zeros of the Riemann zeta-function*, arXiv:1302.5018 / Bull. Lond. Math. Soc. (2013), take

\[
B(s)=\sum_{k\le y}\frac{\mu(k)}{k^s}
P\!\left(\frac{\log(y/k)}{\log y}\right),
\qquad y=T^\theta,\quad 0<\theta<\frac12,
\]

with `P(0)=0`, `P(1)=1`.  Their main terms imply, writing

\[
I=\int_0^1P(u)\,du,
\qquad
J=\int_0^1P'(u)^2\,du,
\]

that the normalized first and second moments are

\[
A(P,\theta)=\frac12+\theta I,
\]

and

\[
D(P,\theta)=
\frac13+\theta I+\theta^2 I^2+\frac{J}{12\theta}.
\]

Thus the formal simple-zero proportion from this one-piece mollifier is

\[
\mathcal K(P,\theta)=\frac{A(P,\theta)^2}{D(P,\theta)}.
\]

## 2. Exact variational optimum of the one-piece class

For fixed `I`, minimizing `J` subject to `P(0)=0`, `P(1)=1` is a quadratic Euler--Lagrange problem.  Parametrize the minimizer as

\[
P_a(x)=a x^2+(1-a)x.
\]

Then

\[
I=\frac{3-a}{6},
\qquad
J=\frac{a^2+3}{3}.
\]

Differentiating `K(P_a,theta)` with respect to `a` gives the relevant stationary point

\[
a=-\theta,
\]

so the maximizing polynomial is exactly

\[
\boxed{P_\theta(x)=-\theta x^2+(1+\theta)x}.
\]

Substitution simplifies completely:

\[
\boxed{
\mathcal K_{\rm one-piece}(\theta)
=\frac{\theta(\theta^2+3\theta+3)}{(1+\theta)^3}
=1-\frac{1}{(1+\theta)^3}.
}
\]

At `theta -> 1/2-`, this gives

\[
1-\frac{1}{(3/2)^3}=\frac{19}{27}=0.7037037037\ldots.
\]

So `19/27` is not merely the result of one convenient quadratic choice: within the Bui--Heath-Brown one-piece `mu(n) P` main-term model, it is the variational endpoint forced by the available mollifier length `theta<1/2`.

## 3. First proposed vector piece collapses

A tempting second basis vector is the coefficient sequence `mu * Lambda`, motivated by differentiating `1/zeta`.  It is **not** a genuinely new direction:

\[
\left(\frac1{\zeta(s)}\right)'
=-\sum_{n\ge1}\frac{\mu(n)\log n}{n^s}
=\sum_{n\ge1}\frac{(\mu*\Lambda)(n)}{n^s},
\]

hence

\[
\boxed{(\mu*\Lambda)(n)=-\mu(n)\log n}.
\]

If

\[
x_n=\frac{\log(y/n)}{\log y},
\]

then

\[
\frac{(\mu*\Lambda)(n)}{\log y}P_1(x_n)
=-\mu(n)(1-x_n)P_1(x_n),
\]

which is already a `mu(n)` times polynomial-weight direction.  The same observation applies to all derivatives of `1/zeta`: their Dirichlet coefficients are `mu(n)` times powers of `log n`, so polynomial smoothing absorbs them.

**Conclusion:** the originally proposed two-piece basis `(mu, mu*Lambda)` has rank one in the existing polynomial mollifier space.  It should not be pursued as a supposed vector improvement.

## 4. The actual bottleneck: the length exponent

Bui--Heath-Brown reduce the difficult large-modulus contribution to

\[
M_{\nu,3}\ll_\varepsilon
 y^{1/3}T^{5/6+\varepsilon}
 +\eta^{-1/2}T\mathcal L^C.
\]

With `y=T^theta`, the first term is lower order only when

\[
\frac{\theta}{3}+\frac56<1,
\]

i.e.

\[
\boxed{\theta<\frac12}.
\]

This is therefore the precise analytic barrier responsible for the `19/27` endpoint in this framework.

The one-piece optimum makes the payoff of breaking the barrier explicit:

| target simple-zero proportion | required theta |
|---:|---:|
| 19/27 = 70.370370...% | 0.5000000000 |
| 71% | 0.5107780535 |
| 72% | 0.5285535437 |
| 73% | 0.5471962779 |
| 75% | 0.5874010520 |
| 80% | 0.7099759467 |

In particular, reaching 71% formally requires only `theta > 0.510778...`.

If the `y` exponent `1/3` is unchanged, supporting theta `0.510778...` would require replacing `T^(5/6)` by approximately

\[
T^{0.82974065+\varepsilon},
\]

a saving of only about `0.00359268` in the `T` exponent.  Conversely, if the `T^(5/6)` exponent is fixed, the exponent of `y` would need to drop from `1/3` to below approximately `0.32629958`.

These are concrete analytic targets, not numerical mollifier tuning targets.

## 5. Research decision

The next primary task is therefore:

> Improve the large-modulus/off-diagonal estimate behind `M_{nu,3}` enough to allow `theta>1/2`, starting with the minimal milestone `theta=0.511` (already sufficient for a formal bound above 71%).

The proof should be attacked at the factorization + hybrid-large-sieve stage, where the published argument chooses a balanced factor size and produces the `y^(1/3) T^(5/6)` term.  Modern bilinear/character-sum estimates should be tested against that explicit exponent budget.

A genuinely new multi-piece mollifier remains a secondary route, but any second coefficient family must first pass a rank test: it must not reduce to `mu(n)` multiplied by a function already contained in the polynomial smoothing space.

## 6. Trust boundary

The algebra in this directory is a formal reorganization of the published Bui--Heath-Brown main terms.  It does **not** prove any result beyond `19/27`.  Any claim with `theta>1/2` requires a new rigorous bound for the large-modulus/off-diagonal contribution before it can be promoted.

Run `python3 experiments/discrete-mollifier/one_piece.py` for the exact `19/27` check and the target-length table.
