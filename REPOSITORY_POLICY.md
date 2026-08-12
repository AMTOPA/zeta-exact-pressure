# Repository workflow policy

This repository uses **one remote branch only: `main`**.

- `main` contains the current research-draft result, reproducibility code, active experiments, and current documentation.
- Historical certified results, rejected candidates, and superseded experiments are preserved under `archive/` with enough provenance to identify the exact result and its status.
- Do **not** create remote `research/*`, feature, staging, or history branches. Isolated exploratory work should happen in a local workspace; only the resulting current state or an archive snapshot is pushed to `main`.
- Do not open a pull request merely to preserve history. History belongs in `archive/`.
- If an experimental result is rejected or superseded, record its parameters/result/provenance under `archive/` on `main` rather than keeping a parallel branch alive.
- Discovery-only numerical values must remain explicitly marked as uncertified and must not replace the current certified record until the relevant interval checks close.
- Heavy certificate workflows should be invoked manually from `main` rather than being tied to temporary branch names.

The intended steady state is therefore exactly one visible branch (`main`) plus archived result snapshots in the repository tree.
