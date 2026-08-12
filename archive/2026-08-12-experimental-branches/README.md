# Experimental branch archive — 2026-08-12

This directory records the temporary research branches that existed during the 2026-08-12 optimization session. The repository is being returned to a single-main workflow; these branches are historical work lines, not active publication branches.

## Current certified main result

The certified research-draft result promoted to `main` is the robust 15-term, seven-point certificate with

- local target `epsilon = 0.005401`, interval-verified;
- `H_floor = 0.6723338` in the promoted record;
- exact-pressure optimum `m = 204`;
- safe decimal bound `0.6733305982`, i.e. 67.3330598288...% from the conservative inputs;
- squash-merge commit `0ca975c883edff70d4ac32709b138a5ccc984935`.

## Temporary branches being retired

### `research/15term-verifier-pilot`

Final head before retirement: `b89bbdeb41f5c61561aae2a1f386e10f4ce4fd8a`.

Purpose: repository-native interval verifier development and certification of the robust 15-term candidate. The successful work was squash-merged to `main` as PR #4. This branch is therefore superseded by `main`.

### `research/15term-finegrid`

Final head before retirement: `454cd28d444d3a60bb036505f06088a87255266a`.

Purpose: fine-grid lower-table experiments used while diagnosing terminal cells in the rejected `epsilon=0.005561` candidate. It is an intermediate diagnostic branch; the final accepted verifier and corrected candidate are already represented by the certified `main` result.

### `research/terminal-refiner`

Final head before retirement: `1bcef82d2c3e8c9149ccee9403cacb372a447576`.

Purpose: hybrid/global-RMQ plus direct terminal-cell refinement experiments. This was verifier engineering used during diagnosis. The key lesson was incorporated into the final interval-certification strategy; the branch is not a separate mathematical result.

### `research/epsilon-tighten`

Final head before retirement: `e762fb7ee75db81aa5e984556113b2795e4a0d6b` (workflow run 31590835765).

Purpose: probe whether the already-certified 15-term window could support a slightly larger epsilon target and a tighter `H` floor without changing the mathematical construction. At cleanup time this was an exploratory workflow-only line and had not been promoted as a new certified result. No result from this line supersedes the certified `main` record unless separately re-established on `main` later.

### `research/8point-local`

Final head before retirement: `c2aab76c7cd321be0c3c0826fa6d45778c669827` (workflow run 31591307709).

Purpose: explore an eight-point / seven-gap local functional. The branch candidate was discovery-only, not interval-certified. Its pre-optimization snapshot is preserved verbatim as [`8point-candidate.json`](8point-candidate.json). A later floating-point trust-region experiment suggested a larger possible eight-point minimum, but that result was never promoted to a rigorous certificate and is intentionally not represented as certified here.

## Policy

Historical numerical results belong under `archive/`. Temporary branches may be used during a calculation, but once an experiment is certified, rejected, or superseded, its result/provenance should be archived on `main` and the temporary branch removed. The default repository state should expose only `main` as a long-lived branch.
