# Reproducing the local seven-point certificate

The current certificate uses the positioned-pressure layout from `sxuff/zeta-positioned-pressure`, with the same pair weights and pressure weights, but a new seven-term window and a new target.

## Pinned upstream provenance

For reproducibility, use the predecessor at exactly

```text
repository: sxuff/zeta-positioned-pressure
commit: 6fd6c5eee6332a379a10cda4276c82e5b2bc3cd4
```

The two implementation files used as the adaptation reference at that commit are

```text
src/build_tables.py       blob fd600325f8f0a1054827613899b132ca2fcf5332
src/verify_positioned.cpp blob 63ff4ae342c77ec44eaea56c5f81a41d03e8a1f3
```

These identifiers are also recorded in `candidate.json` and checked by the repository self-check. The predecessor repository currently exposes no license metadata, so its source is referenced rather than vendored here.

A reproduction should check out the pinned commit rather than a moving `main` branch:

```bash
git clone https://github.com/sxuff/zeta-positioned-pressure.git
git -C zeta-positioned-pressure checkout 6fd6c5eee6332a379a10cda4276c82e5b2bc3cd4
```

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

1. the pinned predecessor commit above;
2. independently generated interval tables;
3. ideally a second interval implementation such as Arb/FLINT;
4. the exact rational parameters above.

Record the platform, compiler/interpreter versions, generated table hashes, verifier counters, and final `VERIFIED` result so that the reproduction can be compared with the current certificate record.
