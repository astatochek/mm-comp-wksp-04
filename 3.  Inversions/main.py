import matplotlib.pyplot as plt
import numpy as np
from functions import promptPair, promptM


def F(x: float) -> float:
    return np.cos(x) + 2*x


def Lagrange(hublist: list):

    def Omega(x: float, xj: float):
        return np.prod([xi - x for xi in hublist if xi != xj])

    def func(x: float):
        return sum([F(xj) * Omega(x, xj) / Omega(xj, xj) for xj in hublist])

    return func


a, b = promptPair()

m = promptM()

h = (b - a) / m
Xj = []
for i in range(m+1):
    Xj.append(a + i * h)
Yj = [F(x) for x in Xj]






