#!/usr/bin/env python3
"""Generate a tiny C++ header containing the exact local-certificate constants."""
from __future__ import annotations

import argparse
from pathlib import Path

from candidate_data import load_candidate, rational


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    c = load_candidate()
    q = int(c["gaps_per_local_window"])
    pairs = c["pair_weights"]
    pressure = c["position_pressure"]
    target = rational(c["local_search"]["candidate_target_for_certification"])
    entries = [(int(i), int(j), int(n)) for i, j, n in pairs["entries"]]
    pnums = [int(x) for x in pressure["numerators"]]
    pressure_den = int(pressure["denominator"])
    pressure_total = rational(pressure["total"])
    pressure_total_scaled = pressure_total * pressure_den
    if pressure_total_scaled.denominator != 1:
        raise ValueError("declared pressure total is incompatible with pressure denominator")

    lines = [
        "#pragma once",
        "#include <array>",
        "#include <cstdint>",
        "",
        "namespace candidate_config {",
        f"inline constexpr int gaps = {q};",
        f"inline constexpr std::int64_t pair_den = {int(pairs['denominator'])}LL;",
        f"inline constexpr std::int64_t span_capacity_num = {int(pairs['span_capacity_numerator'])}LL;",
        f"inline constexpr std::int64_t pressure_den = {pressure_den}LL;",
        f"inline constexpr std::int64_t pressure_total_num = {pressure_total_scaled.numerator}LL;",
        f"inline constexpr std::int64_t target_num = {target.numerator}LL;",
        f"inline constexpr std::int64_t target_den = {target.denominator}LL;",
        "struct PairEntry { int i; int j; std::int64_t num; };",
        f"inline constexpr std::array<PairEntry, {len(entries)}> pairs = {{{{",
    ]
    for i, j, n in entries:
        lines.append(f"    {{{i}, {j}, {n}LL}},")
    lines.extend([
        "}};",
        f"inline constexpr std::array<std::int64_t, {q}> pressure_num = {{{{",
        "    " + ", ".join(f"{x}LL" for x in pnums),
        "}};",
        "} // namespace candidate_config",
        "",
    ])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines), encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
