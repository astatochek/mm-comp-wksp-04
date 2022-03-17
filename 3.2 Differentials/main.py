import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from functions import promptM, promptA, promptH


def F(x: float) -> float:
    return np.exp(1.5 * x)


def dF(x: float) -> float:
    return 1.5 * np.exp(1.5 * x)


def ddF(x: float) -> float:
    return 2.25 * np.exp(1.5 * x)


def Lagrange(hublist: list):

    def Omega(x: float, xj: float):
        return np.prod([xi[0] - x for xi in hublist if xi[0] != xj])

    def func(x: float):
        return sum([xy[1] * Omega(x, xy[0]) / Omega(xy[0], xy[0]) for xy in hublist])

    return func


def getFirstDerivative(f, segment: list, h: float):
    left = segment[0]
    right = segment[1]

    def func(x: float) -> float:
        if x <= left:
            return (-25 * f(x) + 48 * f(x + h) - 36 * f(x + 2 * h) + 16 * f(x + 3 * h) - 3 * f(x + 4 * h)) / (6 * h)
        if x >= right:
            return (-25 * f(x) + 48 * f(x - h) - 36 * f(x - 2 * h) + 16 * f(x - 3 * h) - 3 * f(x - 4 * h)) / (-6 * h)
        return (f(x - 2 * h) - 8 * f(x - h) + 8 * f(x + h) - f(x + 2 * h)) / (12 * h)

    return func


m = promptM()
a = promptA()
h = promptH()

data = {'X': [a + i * h for i in range(m+1)], 'F(X)': [F(a + i * h) for i in range(m+1)]}
df = pd.DataFrame(data, index=[f"X{i}" for i in range(m+1)])
print(df)

XY = [[a + i * h, F(a + i * h)] for i in range(m+1)]

L = Lagrange(XY)

dL = getFirstDerivative(L, [a, a + h * m], h)

data = {'X': [a + i * h for i in range(m+1)],
        'F(X)': [F(a + i * h) for i in range(m+1)],
        'dL(X)': [dL(a + i * h) for i in range(m+1)],
        '|dF(X) - dL(X)|': [abs(dF(a + i * h) - dL(a + i * h)) for i in range(m+1)]
        }

df = pd.DataFrame(data, index=[f"X{i}" for i in range(m+1)])
print(df)

ptsnum = 1000
ep = 0.5
Ox = np.linspace(a - ep, a + h * m + ep, ptsnum)
y1 = [dF(x) for x in Ox]
y2 = [dL(x) for x in Ox]

fig, ax = plt.subplots()
ax.plot(Ox, y1, color="blue", alpha=0.5, label="dF(x)")
ax.plot(Ox, y2, color="red", alpha=0.5, label="dL(x)")
#[ax.vlines(xy[0], min(min(y1), min(y2)), dF(xi), color="blue", alpha=0.2, linestyle="--") for xi in Xj]
#ax.vlines(X, min(min(y1), min(y2)), dF(X), color="red", alpha=0.2, linestyle="--")
plt.scatter([xy[0] for xy in XY], [dF(xy[0]) for xy in XY], color="blue", sizes=[5.0 for xy in XY])
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

plt.show()








