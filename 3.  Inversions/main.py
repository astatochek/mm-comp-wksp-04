import pandas as pd
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


def getF(f, val: float):
    def func(x: float) -> float:
        return f(x) - val
    return func


def Secants(segment: list, f):
    x0 = segment[0]
    x1 = segment[1]
    xp = x0
    xc = x1
    xn = xc - (f(xc) / (f(xc) - f(xp))) * (xc - xp)
    while abs(xn - xc) >= 10**(-8):
        xn, xc, xp = xn - (f(xn) / (f(xn) - f(xc))) * (xn - xc), xn, xc
    return xn


a, b = promptPair()

m = promptM()

h = (b - a) / m
ZYj = []
for i in range(m+1):
    ZYj.append([a + i * h, F(a + i * h)])

data = {'Xi': [zy[0] for zy in ZYj], 'F(Xi)': [zy[1] for zy in ZYj]}
df = pd.DataFrame(data)
print(df)

n = promptN(m, True)

Y = promptFloat()


def cmp(val):
    return abs(val[0] - Y)


YXj = [[zy[1], zy[0]] for zy in ZYj]
YXj.sort(key=cmp)
YXj = YXj[:n + 1]

L = Lagrange(YXj)
X = L(Y)
print("\nMethod 1:")
print(f"invPn({Y}) = {X}")
print(f"|F({X}) - {Y}| = {abs(F(X) - Y)}\n")

n = promptN(m, False)
XYj = [zy for zy in ZYj]
XYj.sort(key=cmp)
XYj = XYj[:n + 1]

L = Lagrange(XYj)
Func = getF(L, Y)









