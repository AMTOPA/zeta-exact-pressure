# Zeta simple-zero research

> [!IMPORTANT]
> **Current interval-certified research-draft record under the existing exact-pressure / scalar-Gram interface: 67.3416490971%.**
>
> That record is retained as the certified computational baseline. The active research direction has now moved to **discrete mollified moments of `zeta'(rho)`**, where the classical RH-conditional scalar-mollifier benchmark is `19/27 = 70.370370...%`.

This is a research project, not a peer-reviewed theorem and not a proof of the Riemann hypothesis.

## 1. Certified exact-pressure baseline

The root [`candidate.json`](candidate.json) remains the current certified computer-assisted result. It uses seven points / six gaps, exact total position pressure

\[
B=\frac{93}{23000},
\]

and a 17-term analytic window

\[
v(s)=\sum_{j=0}^{16}c_j\cos(\omega_js),
\qquad
\omega_0=\sqrt2,
\quad \omega_j=2j\pi\;(1\le j\le16).
\]

Outward-rounded interval arithmetic proves

\[
H(v)>0.6721881580
\]

and the hardened six-dimensional verifier proves

\[
F(g_1,\ldots,g_6)\ge0.0079107
\qquad(g_i\ge0).
\]

The successful local run records

```text
workflow run = 31610179703
artifact id = 9147378469
artifact digest sha256 = 871532c739d5a9e8de770cf00675381ea4fd9c81f212d8e46f86403a27a34dc1
VERIFIED=true
nodes=3768186
convex=2030240
tangent=936616
```

Under the inherited scalar finite-dimensional Gram profile, exact arithmetic selects `m=145` and gives

\[
\boxed{0.67341649097149929495\ldots},
\]

hence safe floor

\[
\boxed{0.6734164909},
\]

i.e. **67.3416490971%** before truncation.

Historical certified states are frozen under [`archive/`](archive/).

## 2. Why this route is no longer the active optimization target

The exact-pressure work established a reproducible local-certificate and interval-verification framework, but repeated optimization of windows, pressures, pair weights, longer local geometries and band-aware Gram profiles showed strong diminishing returns. Analytic extensions under [`experiments/banded-gram/`](experiments/banded-gram/) and [`experiments/pressure-frontier/`](experiments/pressure-frontier/) are retained for audit/history, not as the primary numerical race.

The new strategy changes the observable rather than continuing to optimize the same pair-energy interface.

## 3. Active direction: discrete mollified `zeta'` moments

For a zero `rho`, multiplicity at least two implies

\[
\zeta'(\rho)=0.
\]

Thus for a Dirichlet-polynomial mollifier `B`, Cauchy gives the direct simple-zero detector

\[
N^*(T)
\ge
\frac{\left|\sum_{0<\gamma\le T}B(\rho)\zeta'(\rho)\right|^2}
{\sum_{0<\gamma\le T}|B(\rho)\zeta'(\rho)|^2}.
\]

Bui--Heath--Brown (arXiv:1302.5018), following Conrey--Ghosh--Gonek, prove under RH that the standard Möbius mollifier with length `T^theta`, `theta<1/2`, yields

\[
\boxed{\frac{19}{27}=70.370370\ldots\%}.
\]

The active work is under [`experiments/vector-mollifier/`](experiments/vector-mollifier/).

### 3.1 Exact scalar ceiling

For the whole scalar class

\[
b(n)=\mu(n)P\!\left(\frac{\log(y/n)}{\log y}\right),
\qquad y=T^\theta,
\]

the Bui--Heath--Brown main terms reduce to

\[
U=\frac12+\theta I,
\qquad
Q=\frac13+\theta I+\theta^2I^2+\frac{K}{12\theta},
\]

where `I=int P` and `K=int (P')^2`.

Optimizing over the full `H^1` scalar class gives exactly

\[
\boxed{
R_*(\theta)=
\frac{\theta(\theta^2+3\theta+3)}{(1+\theta)^3}
},
\qquad
R_*'(\theta)=\frac3{(1+\theta)^4}>0.
\]

Therefore the scalar `theta<1/2` class has the sharp limiting ceiling `19/27`. Merely increasing polynomial degree or adding pieces that remain `mu(n)` times a one-variable function of `log n` cannot break it. [`check_scalar_ceiling.py`](experiments/vector-mollifier/check_scalar_ceiling.py) checks the endpoint identities exactly.

### 3.2 Genuine arithmetic coefficient geometry

The first genuine enlargement uses Feng-type prime-tuple information while retaining outer Möbius/squarefree support. Define

\[
E_2(n;y)=
\sum_{p<q,\;pq\mid n}
\frac{\log p\log q}{\log^2y}.
\]

Unlike `log n`, this is not determined by the total size of `n`. The first vector family is

\[
B_0(s)=\sum_{n\le y}\frac{\mu(n)P_0(u_n)}{n^s},
\qquad
B_2(s)=\sum_{n\le y}\frac{\mu(n)P_2(u_n)E_2(n;y)}{n^s}.
\]

If the mixed discrete first/second moment asymptotics have vector `u` and positive matrix `Q`, the optimized Cauchy quotient is

\[
\boxed{u^*Q^{-1}u}.
\]

A finite-zero probe shows a stable positive incremental `E2` direction after allowing scalar polynomial reoptimization, but it is explicitly **discovery only** and is not an asymptotic bound. The next analytic task is the mixed second-moment first variation at the scalar `19/27` extremizer.

### 3.3 Break the half-length barrier

Bui--Heath--Brown's large-modulus analysis, before using `theta<=1/2`, contains two power-size errors

\[
yT^{1/2+\varepsilon}
\quad\text{and}\quad
y^{1/2}T^{3/4+\varepsilon}.
\]

Both hit size `T` at `theta=1/2`. If a modern off-diagonal estimate saves `T^{-delta_1}` and `T^{-delta_2}` respectively, the power-counting range becomes

\[
\theta<\frac12+\delta_1,
\qquad
\theta<\frac12+2\delta_2.
\]

See [`length-barrier.md`](experiments/vector-mollifier/length-barrier.md) and [`check_length_payoff.py`](experiments/vector-mollifier/check_length_payoff.py).

For scale only: if the same scalar main term could be proved at `theta=51/101`, it would formally give about **70.66180725%**; at `theta=6/11`, about **72.90860981%**. These are targets, **not proved results**.

Pratt--Robles (arXiv:1706.04593) show in the related continuous twisted-second-moment problem that Type I/II decomposition plus Kloosterman-sum estimates allows Feng-type mollifiers of length `theta<6/11`. The research question here is whether analogous structure can be exposed before the final Cauchy/hybrid-large-sieve step in the **discrete-zero** argument.

## 4. Current go/no-go priorities

1. Derive the asymptotic mixed second moment for the Feng `E2` direction and test whether `19/27` remains a stationary point in the enlarged coefficient space.
2. Audit the Bui--Heath--Brown large-modulus character sum before their final Cauchy/hybrid-large-sieve step and seek a genuine power saving using Type I/II and Kloosterman structure.
3. Continue a direction only when it changes the asymptotic functional or the admissible mollifier length; finite-height improvements alone are not promoted.

## 5. Reproduction and trust boundary

Run

```bash
sh run.sh
```

for the existing exact-pressure certified baseline and its historical analytic checks.

The new vector-mollifier directory is currently analytic/discovery work. `check_scalar_ceiling.py` and `check_length_payoff.py` verify exact algebra; `finite_zero_probe.py` is deliberately non-rigorous and labels its output accordingly.

Imported analytic inputs are cited rather than vendored; see [`THIRD_PARTY.md`](THIRD_PARTY.md). Historical results remain under `archive/` in accordance with [`REPOSITORY_POLICY.md`](REPOSITORY_POLICY.md).
