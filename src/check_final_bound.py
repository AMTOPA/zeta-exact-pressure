"""High precision arithmetic verification of the current final bound."""
from fractions import Fraction

import mpmath as mp

from candidate_data import load_candidate, rational

mp.mp.dps = 100
candidate = load_candidate()
EPS = rational(candidate["local_certificate"]["target"])
B = rational(candidate["position_pressure"]["total"])
H = rational(candidate["window"]["analytic_h_cert"])
SAFE = rational(candidate["final_deduction"]["safe_published_lower"])
Q = int(candidate["gaps_per_local_window"])
EXPECTED_M = int(candidate["final_deduction"]["block_length"])


def q(x: Fraction):
    return mp.mpf(x.numerator) / x.denominator


def h(m, e):
    if e <= mp.mpf(m) / (m - 1):
        return e
    return e / m + 2 * mp.sqrt(mp.mpf(m - 1) * e / m) - 1


best = None
for m in range(Q + 1, 5000):
    a = q(EPS) * (m - Q)
    r = h(m, a)
    eta = r / a
    v = (m * q(H) - eta * q(B) * (m - Q)) / (m - r)
    if best is None or v > best[0]:
        best = (v, m)

print("scan_best_m=", best[1])
print("float_bound=", mp.nstr(best[0], 100))
assert best[1] == EXPECTED_M
assert best[0] > q(SAFE)
print("interval_verified=True")
