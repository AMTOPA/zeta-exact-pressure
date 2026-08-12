#!/usr/bin/env sh
set -eu
python3 src/check_window.py
python3 src/check_multiplicity.py
python3 src/check_final_bound.py
