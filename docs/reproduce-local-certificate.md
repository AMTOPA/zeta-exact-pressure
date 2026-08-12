# Reproducing the local seven-point certificate

The current certificate uses the positioned-pressure layout from `sxuff/zeta-positioned-pressure`, with the same pair weights and pressure weights, but a new seven-term window and a new target.

## Parameters

Replace the window coefficients in the table builder by

```text
WINDOW_DEN = 1000000000
WINDOW_NUM = (
    1000000000,
    6907835,
    -9359173,
    528441,
    1509267,
    -4923883,
    1358707,
)
```

and set

```text
TARGET = 52289 / 10000000
```

Keep the positioned pressure coefficients unchanged:

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

The pair-weight layout is unchanged from the predecessor.

## Expected verifier record

The development run with outward-rounded interval tables and tangent/convexity acceleration returned

```text
VERIFIED=true
nodes=2334226
pruned=1167275
splits=1166951
convex=1407996
tangent=595297
max_depth=77
```

A proposed higher target `0.00522895` was not accepted, so this repository uses the lower certified target `0.0052289`.

## Independent reproduction requested

For publication-quality confidence, reproduce the certificate using:

1. a fresh checkout of the predecessor verifier;
2. independently generated interval tables;
3. ideally a second interval implementation such as Arb/FLINT;
4. the exact rational parameters above.

This repository deliberately does not vendor the predecessor verifier until its redistribution terms and provenance are reviewed.
