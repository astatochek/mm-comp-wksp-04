import matplotlib.pyplot as plt
import numpy as np


def F(x: float):
    return np.cos(x) + 2 * x
    # return np.sin(x)


def Lagrange(hublist: list):

    def Omega(x: float, xj: float):
        return np.prod([xi - x for xi in hublist if xi != xj])

    def func(x: float):
        return sum([F(xj) * Omega(x, xj) / Omega(xj, xj) for xj in hublist])

    return func


def Newton(hublist: list):

    num = len(hublist)

    DivDif = [[0 for j in range(num)] for i in range(num)]

    for i in range(num):
        DivDif[i][0] = F(hublist[i])

    for i in range(1, num):
        for j in range(num - i):
            DivDif[j][i] = (DivDif[j+1][i-1] - DivDif[j][i-1]) / (hublist[j+i] - hublist[j])

    def func(x: float):
        return sum([DivDif[0][i] * np.prod([x - hublist[j] for j in range(i)]) for i in range(num)])

    return func


m = 13

Zj = []


def PrepareHubs(num: int, left: float, right: float):
    step = (right - left) / num
    for i in range(num + 1):
        Zj.append(left + step * i)


a, b = 0.5, 1.8
PrepareHubs(m, a, b)
for hub in Zj:
    print(f"f({hub}) = {F(hub)}")

while True:
    print(f">>  Insert X in [{a}, {b}] and n in [1, ... , {m}]")
    line = input().split()
    if len(line) < 2:
        print(f">>  Wrong Input: not enough values")
        continue
    try:
        float(line[0])
    except ValueError:
        print(f">>  Wrong Input: {line[0]} is not a float value")
        continue
    try:
        int(line[1])
    except ValueError:
        print(f">>  Wrong Input: {line[1]} is not an int value")
        continue

    X = float(line[0])
    n = int(line[1])

    if X < a or X > b:
        print(f">>  Wrong Input: {X} is not in [{a}, {b}]")
        continue
    if n < 1 or n > m:
        print(f">>  Wrong Input: {n} is not in [1, ... , {m}]")
        continue

    Xj = [hub for hub in Zj]


    def cmp(val):
        return abs(val - X)


    Xj.sort(key=cmp)
    Xj = Xj[:n]
    # print(Xj)

    L = Lagrange(Xj)
    N = Newton(Xj)
    print(f"|F({X}) - L({X})| = {abs(F(X) - L(X))}")
    print(f"|F({X}) - N({X})| = {abs(F(X) - N(X))}")

    ptsnum = 100
    ep = 0.5
    Ox = np.linspace(min(Xj)-ep, max(Xj)+ep, ptsnum)
    y1 = [F(val) for val in Ox]
    y2 = [L(val) for val in Ox]
    # y3 = [N(val) for val in Ox]

    fig, ax = plt.subplots()
    ax.plot(Ox, y1, color="blue", alpha=0.5, label="F(x)")
    ax.plot(Ox, y2, color="red", alpha=0.5, label="P(x)")
    # ax.plot(Ox, y3, color="green", alpha=0.5, label="P(x)")
    plt.scatter(Xj, [F(xi) for xi in Xj], color="blue", sizes=[5.0 for xi in Xj])
    plt.scatter(X, F(X), color="red", sizes=[10.0])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

    plt.show()
