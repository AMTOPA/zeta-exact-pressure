# Local-certificate reproduction and next certification target

## Current status

`main` now tracks an 11-term **discovery candidate**. Its proposed local target is

```text
TARGET = 5405 / 1000000 = 0.005405
```

but this target is **not yet interval-certified**.

The previous certified development record at `0.0052289` is archived under [`../archive/2026-08-12-certified-6732907560/`](../archive/2026-08-12-certified-6732907560/).

## Pinned implementation reference

For reproducibility, use the predecessor at exactly

```text
repository: sxuff/zeta-positioned-pressure
commit: 6fd6c5eee6332a379a10cda4276c82e5b2bc3cd4
```

Reference implementation blobs:

```text
src/build_tables.py       fd600325f8f0a1054827613899b132ca2fcf5332
src/verify_positioned.cpp 63ff4ae342c77ec44eaea56c5f81a41d03e8a1f3
```

The predecessor repository exposes no license metadata, so its implementation is referenced rather than vendored.

## Current exact window

Use denominator `1000000000` and numerators

```text
1000000000
8421762
-9816829
1448046
1412305
-2228329
2374999
-4885560
8393483
-3137216
2381462
```

with frequencies

```text
sqrt(2), 2*pi, 4*pi, 6*pi, 8*pi, 10*pi,
12*pi, 14*pi, 16*pi, 18*pi, 20*pi
```

The position-pressure coefficients remain

```text
PRESSURE_DEN = 2300000000
PRESSURE_NUM = (
    831522,
    1096590,
    1071888,
    1071888,
    1096590,
    831522,
)
```

and sum exactly to `3/1150`.

## Discovery evidence

The current discovery loop used pressure-feasible lattice adversary starts with reflection reduction and local polishing. The recorded observed floating-point minimum is

```text
0.00540611079920...
```

across 2,823 adversarial starts.

This value is discovery evidence only. Floating-point optimization is not an acceptance criterion.

## Required certification run

To promote the candidate, the interval implementation must be generalized from the previous 7-term window to the 11-term window and must prove

```text
F(g1,...,g6) >= 0.005405
```

for all nonnegative gaps. A successful record should include:

1. exact rational window and pressure parameters;
2. interval/table generation precision and implementation version;
3. hashes of generated tables/artifacts;
4. complete branch-and-bound statistics;
5. final `VERIFIED=true` result;
6. an independent reproduction if possible.

If a terminal counterexample box is found, record that box and feed it back into the adversarial discovery set rather than lowering the target blindly.

## Historical record

The superseded seven-term result certified target

```text
52289 / 10000000 = 0.0052289
```

with the recorded development counters

```text
VERIFIED=true
nodes=2334226
pruned=1167275
splits=1166951
convex=1407996
tangent=595297
max_depth=77
```

and produced the archived 67.3290756019% research-draft candidate. See the archive directory for the frozen machine-readable snapshot and source commit.
