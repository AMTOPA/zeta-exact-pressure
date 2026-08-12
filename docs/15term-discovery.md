# 15-term search history and robust repair

This note records an important failed discovery step as well as the retained candidate.

## 1. Rejected score-screened candidate

The first 15-term search polished only a selected subset of integer-lattice starts. It proposed a window with an observed floating-point minimum near `0.0055619915` and target `0.005561`.

The interval verifier did **not** certify that target. More importantly, its unresolved boxes pointed to a basin reachable from the resonance template `(1,1,1,3,1,1)` that had been discarded because the unpolished integer point did not rank among the lowest score-screened starts. Continuous optimization from that region found successively lower values, ultimately showing that the proposed target was false for that window.

This candidate was rejected. The episode demonstrates that ranking integer templates by their starting value is not a safe discovery heuristic near the kernel-zero lattice.

## 2. Adversarial exchange repair

The missed basins were fed back into the window optimization. Pair weights and position-pressure weights were kept fixed; only the 15-term window was re-optimized against the accumulated adversarial set.

The retained rational window has denominator `1000000000` and numerators

```text
1000000000
   8629738
 -10085378
   1746803
   1125700
  -2203905
   1904615
  -4559603
   7930665
  -3022627
   2165339
    398121
   -255934
    188899
   -148305
```

with frequencies

```text
sqrt(2), 2*pi, 4*pi, ..., 28*pi.
```

High-precision evaluation gives

```text
H(v) = 0.672333886657942...
```

and interval arithmetic verifies

```text
H(v) > 0.6723338.
```

## 3. Unscreened stress policy

The corrected discovery policy does not select starts by their unpolished score. It includes:

- every template in `{1,2,3,4}^6` (4096 starts), each locally polished;
- every template in `{1,2,3,5}^6` (another 4096 starts), each locally polished;
- multi-range differential-evolution runs over substantially larger boxes.

The lowest floating-point basin observed for the rounded rational window is

```text
0.005402429240910082...
```

near a family of configurations containing gaps close to `1`, `2`, and `2.92` normalized spacings.

The rigorous target was deliberately set lower:

```text
EPS_TARGET = 0.005401 = 5401 / 1000000.
```

## 4. Rigorous certification

The repository-native table builder generated outward-rounded interval tables on a 4000 grid at 50 decimal digits. The C++ branch-and-bound verifier used direct lower bounds plus interval Hessian LDL and convex supporting-hyperplane pruning.

The full run closed the domain:

```text
VERIFIED=true
nodes=3171002
pruned=1585573
splits=1585429
convex=1776812
tangent=751200
max_depth=62
```

Exact table hashes, workflow provenance, and artifact identifiers are recorded in `candidate.json` and `certificates/latest-verification.txt`.

## 5. Final projection

With

```text
H_floor = 0.6723338
EPS = 0.005401
B = 3/1150
```

the exact-pressure scan selects `m=204` and gives

```text
0.67333059828795868305084456656...
= 67.3330598287958683... %
```

with safe decimal floor

```text
0.6733305982.
```

The previous 67.3290756019% research-draft record remains archived for comparison.

## Lesson for subsequent optimization

The main discovery change is methodological: **adversary selection must be based on resonance-template coverage and exchange, not on the objective value of the unpolished start**. Future window or weight optimization should preserve this rule and should feed every interval-verifier obstruction back into the discovery set before attempting a higher target.
