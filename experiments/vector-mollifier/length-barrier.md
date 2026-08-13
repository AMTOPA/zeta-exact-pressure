# Discrete mollifier length barrier

Status: **analytic roadmap / no new theorem claimed**.

This note isolates the exact place where the Bui--Heath-Brown RH-only discrete-mollifier argument stops at `theta < 1/2`, and quantifies what an improved off-diagonal estimate would need to save.

Primary source: H. M. Bui and D. R. Heath-Brown, *On simple zeros of the Riemann zeta-function*, arXiv:1302.5018, especially equations (13), (17), (20), (21) and the deduction of Lemma 2.

## 1. The two raw large-modulus errors

Their large-modulus contribution satisfies, dyadically,

\[
\mathcal M_{2,3}
\ll
K^{-1}Q^{-3/2}\,L^C
\sum_{d\asymp D}S(Q,X,d).
\]

After the generalized Vaughan decomposition and Perron removal, their hybrid-large-sieve estimate is

\[
V^{-1}T(Q,V)
\ll_ε
K^{1/2}Q^{5/2}D^{-1/2}T^{1/2+ε}
+
K^{1/2}Q^{3/2}D^{-1/2}y^{1/2}T^{3/4+ε}.
\]

The divisor/factorization counts are logarithmic or `T^epsilon`, and the dyadic constraints include

\[
D\le K,
\qquad Q\le y.
\]

Substitution therefore gives the two genuinely relevant power-size errors

\[
\boxed{yT^{1/2+ε}}
\qquad\text{and}\qquad
\boxed{y^{1/2}T^{3/4+ε}}.
\]

For `y=T^theta` these have exponents

\[
\theta+\frac12,
\qquad
\frac\theta2+\frac34.
\]

Both hit exponent `1` exactly at `theta=1/2`.

When `y<=T^{1/2}`, Bui--Heath--Brown may dominate both by the convenient common expression

\[
y^{1/3}T^{5/6+ε},
\]

which is the form recorded in their Lemma 2. The important point for future work is that this common expression should **not** be extrapolated beyond `theta=1/2`; the two raw terms above are the correct attack surface.

## 2. Required savings

Suppose a replacement for the hybrid-large-sieve/off-diagonal step saves powers

\[
yT^{1/2-δ_1+ε}
+
y^{1/2}T^{3/4-δ_2+ε}.
\]

Then a length `y=T^theta` is admissible (at the power-counting level) provided

\[
\boxed{
\theta<\frac12+δ_1
}
\]

and

\[
\boxed{
\theta<\frac12+2δ_2.
}
\]

Thus the smaller of `delta_1` and `2 delta_2` determines the gain past one half.

Some exact targets:

| target `theta` | required `delta_1` | required `delta_2` |
|---:|---:|---:|
| `51/101` | `> 1/202` | `> 1/404` |
| `17/33` | `> 1/66` | `> 1/132` |
| `6/11` | `> 1/22` | `> 1/44` |
| `4/7` | `> 1/14` | `> 1/28` |

The `51/101` row is deliberately modest: it asks only for an exponent saving of about `0.00495` in the first raw term and `0.00248` in the second.

## 3. Payoff if the scalar main term survives

The sharp scalar Bui--Heath--Brown variational main term is

\[
R_*(\theta)
=
\frac{\theta(\theta^2+3\theta+3)}{(1+\theta)^3},
\qquad
R_*'(\theta)=\frac{3}{(1+\theta)^4}>0.
\]

If, and only if, the same discrete first/second-moment asymptotic were proved at a longer length, the formal simple-zero proportion would be:

| `theta` | formal scalar quotient |
|---:|---:|
| `1/2` | `70.3703703704%` |
| `51/101` | `70.6618072514%` |
| `17/33` | `71.2504000000%` |
| `6/11` | `72.9086098107%` |
| `4/7` | `74.2299023291%` |

These are **not proved bounds**. They quantify why even a small break of the half-length barrier is much more valuable than further optimization inside the old pair-correlation framework.

## 4. Modern comparison point

Pratt--Robles, *Perturbed moments and a longer mollifier for critical zeros of zeta*, arXiv:1706.04593, treat a **continuous** twisted second moment. For Feng-type coefficients they decompose the error into Type I and Type II sums and use Kloosterman-sum technology to allow

\[
\theta<\frac6{11}.
\]

This result does not directly imply a longer **discrete zero** mollifier. The proposed research problem is narrower:

> Can the large-modulus character sum arising in Bui--Heath--Brown equation (11), after their generalized Vaughan decomposition, be reorganized into Type I/II or bilinear Kloosterman forms with a power saving over equation (21)?

The first milestone is not `6/11`; it is any explicit pair `(delta_1, delta_2)` with

\[
\min(\delta_1,2\delta_2)>0.
\]

## 5. Concrete next reduction

Equation (21) comes after factoring the nine Dirichlet-polynomial pieces into two blocks `A` and `B` of lengths at most

\[
A_0=\max\left\{yT^{1/2},(KQT/D)^{2/3}\right\}
\]

and then applying Cauchy plus the hybrid large sieve separately to the two blocks.

That Cauchy/large-sieve step deliberately discards convolution structure. The modern attack should therefore occur **before** this final Cauchy step:

1. keep the Type I/II structure of the generalized-Vaughan factors;
2. use the squarefree/Feng coefficient structure before absolute values are taken;
3. perform reciprocity / Poisson or Voronoi transformations where the primitive-character sum creates Kloosterman phases;
4. seek a bilinear estimate that replaces at least one of the two terms in equation (21) by a power-saving version;
5. only after a concrete exponent pair is obtained, re-run the `theta` optimization.

This is the active longer-mollifier subproblem.
