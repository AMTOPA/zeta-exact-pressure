# Archived record: 67.3330598288%

This directory freezes the interval-certified research-draft record that was current on `main` immediately before the epsilon/H tightening promotion on 2026-08-12.

## Recorded bound

Certified working inputs:

```text
H_floor = 0.6723338
epsilon = 0.005401
B = 3/1150
m = 204
```

The exact shifted-pressure arithmetic gave

```text
0.6733305982879586830508445665624969011279...
= 67.333059828795868305...%
```

with conservative decimal floor `0.6733305982`.

## Local verifier record

The 4000-grid, 50-digit outward-rounded interval computation reported

```text
VERIFIED=true
nodes=3171002
pruned=1585573
splits=1585429
convex=1776812
tangent=751200
max_depth=62
```

Workflow run: `31589096212`  
Artifact: `9138629773`

The six interval table hashes are preserved in the machine-readable snapshot.

## Provenance

Repository state immediately before promotion: commit `cc8b59c3ee18a7eb2dbff4b8282f386f3a4f22b8` on `main`.

The next tightening run later certified `epsilon = 0.0054022`; this archived record remains the exact predecessor state.

The full machine-readable snapshot is preserved in [`candidate.json`](candidate.json).
