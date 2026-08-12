#!/usr/bin/env sh
set -eu
python3 src/check_candidate.py
python3 src/check_window.py
python3 src/check_multiplicity.py
python3 src/check_final_bound.py
rm -rf .interval-smoke
python3 src/build_interval_tables.py --output .interval-smoke --smoke-cells 32 --precision 45
rm -rf .interval-smoke
