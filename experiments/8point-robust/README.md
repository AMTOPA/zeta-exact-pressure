# Robust eight-point experiment

Status: **discovery / certification in progress**. This directory does not replace the certified root `candidate.json` unless the seven-dimensional interval verifier closes the target.

## Construction

Use the same certified rational 15-term window as the current seven-point record, but a local block of eight consecutive atoms, hence seven gaps.

The local functional has the same form

\[
F_8(g)=\sum_{r=1}^7 b_r g_r+\sum_{0\le i<j\le7}a_{ij}W(y_j-y_i),
\qquad y_j=g_1+\cdots+g_j.
\]

The exact weights in [`candidate.json`](candidate.json) obey

\[
\sum_{i=0}^{7-s} a_{i,i+s}=2\quad(1\le s\le7),
\qquad
\sum_{r=1}^7 b_r=\frac3{1150},
\]

and are reflection symmetric. These are the same local-to-global capacity conditions used by the positioned-pressure deduction, now with seven local gap positions.

The weights were obtained from the overlap-based eight-point baseline by a reflection-symmetric trust-region LP, followed by unscreened local polishing of all 8,320 reflection representatives of `{1,2,3,4}^7` and six multi-range differential-evolution stress runs.

## Floating-point discovery result

For the exact rationalized weights, the lowest observed basin is

```text
F8_min_float = 0.005482799831021097...
```

near

```text
(1.9808064453,
 1.0440797533,
 1.9723040882,
 1.0442171158,
 1.9723040882,
 1.0440797533,
 1.9808064453)
```

The proposed rigorous target is deliberately lower:

```text
epsilon_8 = 2741/500000 = 0.005482
```

The current seven-point record would already be beaten once an eight-point target exceeds approximately `0.005409736`, so the proposed target has substantial arithmetic headroom.

## Conditional projection

With the already interval-verified window floor

```text
H_floor = 0.6723338866
B = 3/1150
epsilon_8 = 0.005482
```

the exact-pressure scan selects `m = 204` and conditionally gives

```text
0.6733781954777601373716541705496368620...
= 67.337819547776013737...%
```

with safe decimal floor `0.6733781954` **if and only if** the new seven-dimensional local target is rigorously certified.

## Certification gate

The repository-native verifier is dimension-driven through `candidate_config::gaps`, so the same outward-rounded interval-table + branch-and-bound machinery can test seven gaps. The workflow `.github/workflows/eight-point-certificate.yml` builds exact tables from this candidate and tests `F_8 >= 0.005482`.

No value in this directory is a new certified record until that workflow returns `VERIFIED=true` with no unresolved terminal cell. If it is inconclusive, the terminal boxes are to be diagnosed and fed back into the experiment rather than silently promoted.
