import matplotlib.pyplot as plt
import numpy as np


def F(x: float):
    # return np.cos(x) + 2 * x
    return np.sin(x)


def Lagrange(hublist: list):

    def Omega(x: float, xj: float):
        return np.prod([xi - x for xi in hublist if xi != xj])

    def func(x: float):
        return sum([F(xj) * Omega(x, xj) / Omega(xj, xj) for xj in hublist])

    return func


m = 10

Zj = []


def PrepareHubs(num: int, left: float, right: float):
    step = (right - left) / num
    for i in range(num + 1):
        Zj.append(left + step * i)


a, b = -10, 10
PrepareHubs(m, a, b)
for hub in Zj:
    print(f"f({hub}) = {F(hub)}")

n = 8

while True:
    X = input()
    try:
        float(X)
    except ValueError:
        print(f">>  Wrong Input: {X} is not a float value")
        continue
    X = float(X)
    if X < a or X > b:
        print(f">>  Wrong Input: {X} is not in [{a}, {b}]")
        continue
    Xj = [hub for hub in Zj]


    def cmp(val):
        return abs(val - X)


    Xj.sort(key=cmp)
    Xj = Xj[:n + 1]
    # print(Xj)

    L = Lagrange(Xj)
    print(f"|F({X}) - L({X})| = {abs(F(X) - L(X))}")

    ptsnum = 100
    ep = 0.5
    Ox = np.linspace(min(Xj)-ep, max(Xj)+ep, ptsnum)
    y1 = [F(val) for val in Ox]
    y2 = [L(val) for val in Ox]

    fig, ax = plt.subplots()
    ax.plot(Ox, y1, color="blue", alpha=0.5, label="F(x)")
    ax.plot(Ox, y2, color="red", alpha=0.5, label="L(x)")
    plt.scatter(Xj, [F(xi) for xi in Xj], color="blue", sizes=[5.0 for xi in Xj])
    plt.scatter(X, F(X), color="red", sizes=[10.0])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

    plt.show()
