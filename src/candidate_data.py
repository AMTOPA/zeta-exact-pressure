"""Shared loader for the machine-readable candidate parameters."""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_PATH = ROOT / "candidate.json"


def load_candidate() -> dict:
    return json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))


def rational(node: dict) -> Fraction:
    return Fraction(int(node["numerator"]), int(node["denominator"]))
