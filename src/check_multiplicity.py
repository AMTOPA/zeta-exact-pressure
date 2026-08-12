from fractions import Fraction

from candidate_data import load_candidate, rational

candidate = load_candidate()
M = int(candidate["final_deduction"]["block_length"])
Q = int(candidate["gaps_per_local_window"])
pressure = candidate["position_pressure"]
DEN = int(pressure["denominator"])
NUMS = [int(x) for x in pressure["numerators"]]

b = [Fraction(x, DEN) for x in NUMS]
B = sum(b, Fraction(0))
assert B == rational(pressure["total"])

coefficients = []
for j in range(1, M):
    coefficients.append(
        sum(
            (b[r - 1] for t in range(M - Q) if 1 <= (r := j - t) <= Q),
            Fraction(0),
        )
    )

assert sum(coefficients, Fraction(0)) == (M - Q) * B
print("identity_verified=True")
