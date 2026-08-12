"""Shared loader for machine-readable candidate parameters."""
from __future__ import annotations

import json
import os
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CANDIDATE_PATH = ROOT / "candidate.json"


def candidate_path() -> Path:
    raw = os.environ.get("ZETA_CANDIDATE_PATH")
    if raw is None:
        return DEFAULT_CANDIDATE_PATH
    path = Path(raw)
    return path if path.is_absolute() else ROOT / path


def load_candidate() -> dict:
    return json.loads(candidate_path().read_text(encoding="utf-8"))


def rational(node: dict) -> Fraction:
    return Fraction(int(node["numerator"]), int(node["denominator"]))
