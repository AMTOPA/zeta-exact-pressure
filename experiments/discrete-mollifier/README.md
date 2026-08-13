# Discrete zeta-prime mollifier research pivot

Status: **active analytic research direction; no new theorem or root record is claimed here.**

The exact-pressure / pair-correlation line remains reproducible in the repository, but it is no longer the primary optimization target. This directory studies a genuinely different detector for simple zeros: discrete mollified moments of `zeta'(rho)`.

## 1. Starting inequality

For any regular function `B(s)`, a multiple zero `rho` has `zeta'(rho)=0`. Hence Cauchy gives

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

with `P(0)=0`, `P(1)=1`. Their main terms imply, writing

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

For fixed `I`, minimizing `J` subject to `P(0)=0`, `P(1)=1` is a quadratic Euler--Lagrange problem. Parametrize the minimizer as

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

A tempting second basis vector is the coefficient sequence `mu * Lambda`, motivated by differentiating `1/zeta`. It is **not** a genuinely new direction:

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

which is already a `mu(n)` times polynomial-weight direction. The same observation applies to all derivatives of `1/zeta`: their Dirichlet coefficients are `mu(n)` times powers of `log n`, so polynomial smoothing absorbs them.

**Conclusion:** the originally proposed two-piece basis `(mu, mu*Lambda)` has rank one in the existing polynomial mollifier space. It should not be pursued as a supposed vector improvement.

## 4. The actual bottleneck is a three-term junction

The simplified statement of Bui--Heath-Brown Lemma 2 is

\[
M_{\nu,3}\ll_\varepsilon y^{1/3}T^{5/6+\varepsilon}+\eta^{-1/2}T\mathcal L^C,
\]

but that simplification already uses `y <= T^(1/2)`. For attempts to cross `theta=1/2`, the unsimplified estimate at the end of their proof is the relevant one:

\[
\boxed{
M_{\nu,3}\ll_\varepsilon
 yT^{1/2+\varepsilon}
 +y^{1/2}T^{3/4+\varepsilon}
 +y^{1/3}T^{5/6+\varepsilon}
 +\eta^{-1/2}T\mathcal L^C.
}
\]

The origins of the three power terms are structurally different:

1. `y T^(1/2)` comes from the **long-single-factor regime** in Section 3.2, where a long Dirichlet-polynomial factor is disposed of using Pólya--Vinogradov;
2. `y^(1/2) T^(3/4)` comes from the `A0 >= y T^(1/2)` branch of the two-block factorization followed by the hybrid large sieve;
3. `y^(1/3) T^(5/6)` comes from the balancing branch
   \[
   A_0\ge (KQT/D)^{2/3}
   \]
   in the same factorization/large-sieve argument.

With `y=T^theta`, their exponents of `T` are

\[
E_1=\theta+\frac12,
\qquad
E_2=\frac\theta2+\frac34,
\qquad
E_3=\frac\theta3+\frac56.
\]

At

\[
\boxed{\theta=\frac12}
\]

all three satisfy

\[
E_1=E_2=E_3=1.
\]

Thus the `1/2` barrier is a **triple junction**, not a single `y^(1/3)T^(5/6)` obstruction. Any genuine `theta>1/2` proof must improve the long-factor regime as well as the balanced factorization regime (or replace the decomposition by one estimate that treats both simultaneously).

## 5. Payoff and exponent budget

The one-piece optimum makes the payoff of breaking the barrier explicit:

| target simple-zero proportion | required theta |
|---:|---:|
| 19/27 = 70.370370...% | 0.5000000000 |
| 71% | 0.5107780535 |
| 72% | 0.5285535437 |
| 73% | 0.5471962779 |
| 75% | 0.5874010520 |
| 80% | 0.7099759467 |

For 71%, `theta = 0.5107780535...`. Under the published exponents the three terms exceed the `T^1` threshold by respectively

\[
\boxed{0.01077805,\quad0.00538903,\quad0.00359268}.
\]

So a 71% proof requires a small but genuine power saving in **all active regimes**. The largest required saving is in the long-factor term, not the `5/6` term.

For 72%, the corresponding excesses are approximately

\[
0.02855354,\quad0.01427677,\quad0.00951785.
\]

This gives a quantitative go/no-go test for any proposed modern input.

## 6. Most promising analytic attack

The next primary task is therefore:

> Replace the Section 3.2--3.4 pointwise-long-factor + two-block hybrid-large-sieve treatment by a stronger **family-averaged mean-value/bilinear estimate**, first targeting the minimal milestone `theta=0.511`.

Two modern references are particularly relevant to audit, without assuming in advance that their hypotheses match our weighted sum:

- Conrey--Iwaniec--Soundararajan, arXiv:0710.5176, prove a power-saving asymptotic for the sixth moment of Dirichlet `L`-functions averaged over moduli, primitive characters, and the critical line. This is structurally close to the sixth-moment input that the older Conrey--Ghosh--Gonek route needed.
- Chandee--Li--Matomäki--Radziwiłł, arXiv:2409.01457, obtain the sixth moment at the central point without the extra `t`-averaging and explicitly develop methods for difficult **unbalanced sums**. The unbalanced-factor regime is exactly where the Bui--Heath-Brown proof pays the first `y T^(1/2)` loss.

The immediate research question is not "can we cite a sixth-moment theorem?" but the precise compatibility problem:

> Can the weighted primitive-character sum arising from `M_{nu,3}` be transformed into a form covered by a modern sixth-moment/asymptotic-large-sieve estimate with enough uniformity in `q`, the Perron `t` variable, and the extra `d,k` weights to save at least `T^(-0.011)` at `theta=0.511`?

If yes, the formal mollifier optimization already converts that analytic saving into a simple-zero proportion above 71%.

A genuinely new multi-piece mollifier remains secondary. Any second coefficient family must first pass a rank test: it must not reduce to `mu(n)` multiplied by a function already contained in the polynomial smoothing space.

## 7. Trust boundary

The algebra in this directory is a formal reorganization of the published Bui--Heath-Brown main terms. It does **not** prove any result beyond `19/27`. Any claim with `theta>1/2` requires a new rigorous off-diagonal estimate before it can be promoted.

Run `python3 experiments/discrete-mollifier/one_piece.py` for the exact `19/27` check and the target-length table.
