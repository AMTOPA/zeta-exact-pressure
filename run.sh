#!/usr/bin/env sh
set -eu
python3 src/check_candidate.py
python3 src/check_window.py
python3 src/check_multiplicity.py
python3 src/check_final_bound.py
python3 src/check_banded_gram.py
python3 src/check_multilag.py
python3 src/check_trace_banded_gram.py
python3 src/check_trace_root_tightening.py
python3 experiments/discrete-mollifier/one_piece.py --check
python3 experiments/discrete-mollifier/feng_k2.py --check
rm -rf .interval-smoke
python3 src/build_interval_tables.py --output .interval-smoke --smoke-cells 32 --precision 45
python3 src/write_verifier_config.py --output .interval-smoke/candidate_config.hpp
g++ -std=c++17 -O2 -Wall -Wextra -pedantic -ffp-contract=off -I.interval-smoke src/verify_local_tables.cpp -o .interval-smoke/verify_local_tables
.interval-smoke/verify_local_tables 1 1000000 .interval-smoke 10000
rm -rf .interval-smoke
