import mpmath as mp
from mpmath import iv

from candidate_data import load_candidate, rational

mp.mp.dps = 80
iv.dps = 60

candidate = load_candidate()
window = candidate["window"]
DEN = int(window["denominator"])
NUM = [int(x) for x in window["numerators"]]
H_FLOOR = rational(window["projection_h_floor"])


def sinc(z):
    return mp.sin(z) / z if z else mp.mpf(1)


def C(a, b):
    return (sinc((a - b) / 2) + sinc((a + b) / 2)) / 2


def A(a, b):
    return (
        (mp.sin(a / 2) / a + 2 * mp.cos(a / 2) / a**2) * sinc(b / 2)
        - 2 * C(a, b) / a**2
    )


c = [mp.mpf(n) / DEN for n in NUM]
omega = [mp.sqrt(2)] + [2 * j * mp.pi for j in range(1, len(NUM))]
i1 = sum(ci * sinc(w / 2) for ci, w in zip(c, omega))
i2 = sum(
    c[i] * c[j] * C(omega[i], omega[j])
    for i in range(len(NUM))
    for j in range(len(NUM))
)
J = sum(
    c[i] * c[j] * A(omega[i], omega[j])
    for i in range(len(NUM))
    for j in range(len(NUM))
)
c1 = i1 * i1 / (i2 + J)
H = 2 - 1 / c1

print("H =", mp.nstr(H, 70))
h_floor = mp.mpf(H_FLOOR.numerator) / H_FLOOR.denominator
assert H > h_floor

# Rigorous interval positivity subdivision on [-1/2, 1/2].
ci = [iv.mpf(n) / DEN for n in NUM]
oi = [iv.sqrt(2)] + [2 * j * iv.pi for j in range(1, len(NUM))]
N = 4096
global_lo = float("inf")
for k in range(N):
    s = iv.mpf([k / (2 * N), (k + 1) / (2 * N)])
    v = iv.mpf(0)
    for a, w in zip(ci, oi):
        v += a * iv.cos(w * s)
    global_lo = min(global_lo, float(v.a))

print("interval_window_lower_bound =", global_lo)
assert global_lo > 0
