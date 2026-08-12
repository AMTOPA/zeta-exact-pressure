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

pairs = candidate["pair_weights"]
pair_den = int(pairs["denominator"])
capacity_num = int(pairs["span_capacity_numerator"])
entries = [(int(i), int(j), int(n)) for i, j, n in pairs["entries"]]
assert all(0 <= i < j <= gaps for i, j, _ in entries)
# The local-to-global argument requires nonnegative pair weights; exact zeros
# are allowed and occur in the joint-pressure optimum.
assert all(n >= 0 for _, _, n in entries)
assert len({(i, j) for i, j, _ in entries}) == len(entries)
for span in range(1, gaps + 1):
    total = sum(n for i, j, n in entries if j - i == span)
    assert total == capacity_num
assert Fraction(capacity_num, pair_den) == 2

pressure = candidate["position_pressure"]
assert len(pressure["numerators"]) == gaps
assert all(int(n) >= 0 for n in pressure["numerators"])
pressure_sum = sum(
    (Fraction(int(n), int(pressure["denominator"])) for n in pressure["numerators"]),
    Fraction(0),
)
assert pressure_sum == rational(pressure["total"])

local = candidate["local_search"]
assert rational(local["candidate_target_for_certification"]) > 0
verified = bool(local["verified"])

final = candidate["final_projection"]
assert final["pressure_shift_factor"] == f"m-{gaps}"
assert int(final["block_length"]) > gaps
assert rational(final["projected_safe_decimal"]) > 0
assert bool(final["certified"]) is verified

if verified:
    certificate = candidate["local_certificate"]
    assert certificate["verified"] is True
    assert certificate["independent_reproduction"] is False
    assert rational(certificate["target"]) == rational(local["candidate_target_for_certification"])
    assert int(certificate["grid"]) > 0
    assert int(certificate["precision_decimal_digits"]) >= 40
    stats = certificate["verifier_stats"]
    assert int(stats["nodes"]) > 0
    assert int(stats["pruned"]) > 0
    assert int(stats["splits"]) > 0
    assert int(stats["max_depth"]) > 0
    hashes = certificate["table_hashes_sha256_big_endian_float_stream"]
    for required in (
        "w_lower.bin",
        "w_second_lower.bin",
        "w_mid_lower.bin",
        "w_mid_upper.bin",
        "w_prime_mid_lower.bin",
        "w_prime_mid_upper.bin",
    ):
        assert len(hashes[required]) == 64

archive = candidate["archive"]
assert archive["previous_certified_record"].startswith("archive/")
if "previous_source_commit" in archive:
    assert len(archive["previous_source_commit"]) == 40

provenance = candidate["provenance"]["positioned_pressure_predecessor"]
assert provenance["repository"] == "sxuff/zeta-positioned-pressure"
assert len(provenance["commit"]) == 40
for item in provenance["files"].values():
    assert item["path"]
    assert len(item["blob_sha"]) == 40

print("candidate_consistency_verified=True")
print("pair_weight_span_capacity_verified=True")
print("position_pressure_total_verified=True", pressure_sum)
print("local_interval_certificate_verified=", verified)
print("predecessor_commit=", provenance["commit"])
