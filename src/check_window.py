import math

import mpmath as mp
from mpmath import iv

from candidate_data import load_candidate, rational

mp.mp.dps = 80
iv.dps = 70

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


def sinc_interval(z):
    radius = max(abs(float(z.a)), abs(float(z.b)))
    if radius < 0.5:
        value = iv.mpf(1)
        for n in range(1, 30):
            value += (-1 if n & 1 else 1) * z ** (2 * n) / math.factorial(2 * n + 1)
        return value + iv.mpf([-1e-65, 1e-65])
    return iv.sin(z) / z


def C_interval(a, b):
    return (sinc_interval((a - b) / 2) + sinc_interval((a + b) / 2)) / 2


def A_interval(a, b):
    return (
        (iv.sin(a / 2) / a + 2 * iv.cos(a / 2) / a**2) * sinc_interval(b / 2)
        - 2 * C_interval(a, b) / a**2
    )


# High-precision point evaluation for a readable reference value.
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

# Rigorous interval enclosure for the same analytic quantity.
ci = [iv.mpf(n) / DEN for n in NUM]
oi = [iv.sqrt(2)] + [2 * j * iv.pi for j in range(1, len(NUM))]
i1_iv = iv.mpf(0)
i2_iv = iv.mpf(0)
J_iv = iv.mpf(0)
for a, w in zip(ci, oi):
    i1_iv += a * sinc_interval(w / 2)
for i in range(len(NUM)):
    for j in range(len(NUM)):
        i2_iv += ci[i] * ci[j] * C_interval(oi[i], oi[j])
        J_iv += ci[i] * ci[j] * A_interval(oi[i], oi[j])
c1_iv = i1_iv * i1_iv / (i2_iv + J_iv)
H_iv = 2 - 1 / c1_iv
h_floor_iv = iv.mpf(H_FLOOR.numerator) / H_FLOOR.denominator
print("H_interval =", H_iv)
assert H_iv > h_floor_iv
print("H_floor_interval_verified=True")

# Rigorous interval positivity subdivision on [-1/2, 1/2].
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
