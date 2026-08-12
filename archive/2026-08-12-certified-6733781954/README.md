# Archived record: 67.3378195478%

This directory freezes the interval-certified eight-point / seven-gap research-draft state that was current on `main` immediately before adding the 67.3412981907% discovery experiment on 2026-08-12.

Certified working inputs:

```text
points = 8
gaps = 7
H_floor = 0.6723338866
epsilon = 0.005482
B = 3/1150
m = 204
```

The exact shifted-pressure arithmetic gave

```text
0.67337819547776013737165417054963686201...
= 67.337819547776013737...%
```

with safe decimal floor `0.6733781954`.

The hardened outward-rounded interval verifier reported

```text
VERIFIED=true
nodes=56348888
pruned=28174468
splits=28174420
convex=21755661
tangent=9522833
max_depth=83
```

Workflow run: `31594502822`  
Artifact: `9141284166`  
Artifact digest: `sha256:e0205c8b00810e014f8068d06d59ebd4a3b8c2a6768802a98a7fdad84aeaf7ce`

Certified local source commit: `7d7b02ad4a5f4269286043973f13512216ea9127`.  
Repository state immediately before the discovery update: `3388054ddcd154ee568d2e0fa5d8ad67c241732e`.

The machine-readable snapshot is preserved in [`candidate.json`](candidate.json).
