import matplotlib.pyplot as plt
import numpy as np
from functions import promptPair, promptM, promptN, promptFloat


def F(x: float) -> float:
    return np.cos(x) + 2*x


def Lagrange(hublist: list):

    def Omega(x: float, xj: float):
        return np.prod([xi[0] - x for xi in hublist if xi[0] != xj])

    def func(x: float):
        return sum([xy[1] * Omega(x, xy[0]) / Omega(xy[0], xy[0]) for xy in hublist])

    return func


a, b = promptPair()

m = promptM()

h = (b - a) / m
ZYj = []
for i in range(m+1):
    ZYj.append([a + i * h, F(a + i * h)])
    print(f"F({ZYj[-1][0]}) = {ZYj[-1][1]}")

n = promptN(m)

Y = promptFloat()


def cmp(val):
    return abs(val[0] - Y)


YXj = [[zy[1], zy[0]] for zy in ZYj]
YXj.sort(key=cmp)
YXj = YXj[:n + 1]

L = Lagrange(YXj)
X = L(Y)
print("\nMethod 1:")
print(f"L({Y}) = {X}")
print(f"|F({X}) - {Y}| = {abs(F(X) - Y)}\n")






