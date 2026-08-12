"""Structural and exact-arithmetic checks for candidate.json."""
from fractions import Fraction

from candidate_data import load_candidate, rational

candidate = load_candidate()
points = int(candidate["points"])
gaps = int(candidate["gaps_per_local_window"])
assert points == gaps + 1
assert len(candidate["window"]["numerators"]) == points
assert len(candidate["window"]["frequencies"]) == points
assert len(candidate["position_pressure"]["numerators"]) == gaps

pressure = candidate["position_pressure"]
pressure_sum = sum(
    (Fraction(int(n), int(pressure["denominator"])) for n in pressure["numerators"]),
    Fraction(0),
)
assert pressure_sum == rational(pressure["total"])

final = candidate["final_deduction"]
assert final["pressure_shift_factor"] == f"m-{gaps}"
assert int(final["block_length"]) > gaps
assert rational(final["safe_published_lower"]) > 0

provenance = candidate["provenance"]["positioned_pressure_predecessor"]
assert provenance["repository"] == "sxuff/zeta-positioned-pressure"
assert len(provenance["commit"]) == 40
for item in provenance["files"].values():
    assert item["path"]
    assert len(item["blob_sha"]) == 40

print("candidate_consistency_verified=True")
print("predecessor_commit=", provenance["commit"])
