"""Structural and exact-arithmetic checks for candidate.json."""
from fractions import Fraction

from candidate_data import load_candidate, rational

candidate = load_candidate()
points = int(candidate["points"])
gaps = int(candidate["gaps_per_local_window"])
assert points == gaps + 1

window = candidate["window"]
term_count = int(window["term_count"])
assert len(window["numerators"]) == term_count
assert len(window["frequencies"]) == term_count
assert term_count >= points

pressure = candidate["position_pressure"]
assert len(pressure["numerators"]) == gaps
pressure_sum = sum(
    (Fraction(int(n), int(pressure["denominator"])) for n in pressure["numerators"]),
    Fraction(0),
)
assert pressure_sum == rational(pressure["total"])

local = candidate["local_search"]
assert local["verified"] is False
assert rational(local["candidate_target_for_certification"]) > 0

final = candidate["final_projection"]
assert final["pressure_shift_factor"] == f"m-{gaps}"
assert int(final["block_length"]) > gaps
assert rational(final["projected_safe_decimal"]) > 0
assert final["certified"] is False

archive = candidate["archive"]
assert archive["previous_certified_record"].startswith("archive/")
assert len(archive["previous_source_commit"]) == 40

provenance = candidate["provenance"]["positioned_pressure_predecessor"]
assert provenance["repository"] == "sxuff/zeta-positioned-pressure"
assert len(provenance["commit"]) == 40
for item in provenance["files"].values():
    assert item["path"]
    assert len(item["blob_sha"]) == 40

print("candidate_consistency_verified=True")
print("candidate_status=discovery_not_interval_certified")
print("predecessor_commit=", provenance["commit"])
