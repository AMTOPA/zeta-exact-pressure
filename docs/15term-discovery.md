# 15-term discovery candidate

> Status: floating-point discovery result only. The local target below is **not** interval-certified.

## Motivation

The 11-term candidate improved the local defect by enlarging the window basis while keeping the predecessor pair weights and exact position-pressure vector fixed. Further experiments showed that freely re-optimizing pair/pressure weights is fragile: cutting-plane LP solutions can overfit the current counterexample set and expose new mixed 1/3-resonance valleys under differential-evolution stress. The present candidate therefore freezes the established pair/pressure weights and spends the remaining freedom only on the window.

## Exact window

Use

\[
v(s)=\sum_{j=0}^{14}c_j\cos(\omega_j s),\qquad
\omega_0=\sqrt2,\quad \omega_j=2j\pi\ (1\le j\le14),
\]

with common denominator `1000000000` and numerators

```text
1000000000
   7715770
 -15127849
   -277796
   1460676
  -4061917
   4967584
  -4903364
   5054213
  -2570688
   3857592
    459037
   -292106
    211779
   -164957
```

High-precision evaluation gives

```text
H(v) = 0.6722654286963972986928429055204711746749537758314228...
```

The conservative projection input is

```text
H_floor = 0.6722654
```

## Adversarial discovery search

The pair-weight layout and position-pressure vector are unchanged from the predecessor/current main candidate.

The candidate was stress-tested with:

- all `9^6 = 531441` integer gap patterns in `{0,...,8}^6` scored before polishing;
- analytic-gradient L-BFGS-B polishing of the 220 lowest integer-lattice starts;
- accumulated low configurations from the preceding 11-term and alternating-minimax experiments;
- 9 differential-evolution runs over boxes `[0,6]^6`, `[0,10]^6`, and `[0,16]^6`.

For the rounded rational coefficients above, the lowest floating-point value observed in the strong lattice-polish pass was

```text
F_min_float = 0.005561991478045605...
```

The independent differential-evolution stress runs did not find a lower value; their lowest result in this pass was approximately `0.00571099837`.

This is discovery evidence, not a proof that the global minimum has been found.

## Proposed rigorous target

The next interval-verifier target is

```text
EPS_TARGET = 0.005561 = 5561 / 1000000
```

which leaves about `9.91e-7` between the target and the current floating-point minimum.

A verifier success must prove

\[
F(g_1,\ldots,g_6)\ge 0.005561
\]

for all nonnegative gaps, using outward-rounded interval arithmetic/branch-and-bound. Any terminal counterexample box should be fed back into the discovery set rather than hidden by lowering the target without analysis.

## Conditional global projection

With

```text
H_floor = 0.6722654
EPS_TARGET = 0.005561
B = 3/1150
```

the exact-pressure integer scan selects

```text
m = 199
```

and gives

```text
0.67336590025702537190754388355895632950...
= 67.33659002570253719... %
```

so the safe decimal floor conditional on certifying the local target is

```text
0.6733659002
```

Using the floating-point `H(v)` and observed local minimum instead gives a discovery projection of roughly `67.33665733%`.

## Basis-size check

A 17-term follow-up optimization did not improve the active-set objective over the 15-term solution. This suggests the straightforward high-harmonic extension is already near diminishing returns; the next useful work should prioritize rigorous certification or a genuinely different window family rather than simply adding more Fourier terms.
