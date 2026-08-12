import mpmath as mp
from mpmath import iv

mp.mp.dps = 80
iv.dps = 60

DEN = 1_000_000_000
NUM = [1_000_000_000, 6_907_835, -9_359_173, 528_441, 1_509_267, -4_923_883, 1_358_707]

def sinc(z):
    return mp.sin(z) / z if z else mp.mpf(1)

def C(a, b):
    return (sinc((a - b) / 2) + sinc((a + b) / 2)) / 2

def A(a, b):
    return (mp.sin(a / 2) / a + 2 * mp.cos(a / 2) / a**2) * sinc(b / 2) - 2 * C(a, b) / a**2

c = [mp.mpf(n) / DEN for n in NUM]
omega = [mp.sqrt(2)] + [2 * j * mp.pi for j in range(1, 7)]
i1 = sum(ci * sinc(w / 2) for ci, w in zip(c, omega))
i2 = sum(c[i] * c[j] * C(omega[i], omega[j]) for i in range(7) for j in range(7))
J = sum(c[i] * c[j] * A(omega[i], omega[j]) for i in range(7) for j in range(7))
c1 = i1 * i1 / (i2 + J)
H = 2 - 1 / c1

print("H =", mp.nstr(H, 70))
assert H > mp.mpf("0.6724057")

# Rigorous interval positivity check on [-1/2, 1/2].
ci = [iv.mpf(n) / DEN for n in NUM]
oi = [iv.sqrt(2)] + [2 * j * iv.pi for j in range(1, 7)]
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
