# Repository workflow policy

This repository uses a **single long-lived branch: `main`**.

- `main` contains the current research-draft result, reproducibility code, and active documentation.
- Historical certified results, rejected candidates, and superseded experiments are preserved under `archive/` with enough provenance to identify the exact result and its status.
- Temporary research branches may be created only for short-lived experiments. They must not become long-lived parallel histories.
- When an experiment is finished, rejected, or superseded, preserve the result/provenance under `archive/` on `main`, then remove the temporary branch.
- Do not open a pull request merely to preserve history. History belongs in `archive/`; pull requests are only for changes intended to become the current `main` state.
- Discovery-only numerical values must remain explicitly marked as uncertified and must not replace the current certified record until the relevant interval checks close.

The intended steady state of the repository is therefore one visible working branch (`main`) plus archived result snapshots in the tree.
