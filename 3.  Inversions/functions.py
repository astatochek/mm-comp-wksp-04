

def promptPair() -> list:
    print(f">>    Insert values for [a, b]")
    inpt = [x for x in input().split()]
    if len(inpt) < 2:
        print(f">>    Error: Not enough values")
        return promptPair()
    try:
        a = float(inpt[0])
    except ValueError:
        print(f">>    Error: {inpt[0]} is not a float value")
        return promptPair()
    try:
        b = float(inpt[1])
    except ValueError:
        print(f">>    Error: {inpt[1]} is not a float value")
        return promptPair()
    if b <= a:
        print(f">>    Error: {a} >= {b} but a must be less than b")
        return promptPair()
    return [a, b]


def promptM() -> int:
    print(f">>    Insert m+1 - the number of points")
    inpt = input()
    try:
        m = int(inpt) - 1
    except ValueError:
        print(f">>    Error: {inpt} is not an int value")
        return promptM()
    if m < 9:
        print(f">>    Error: {m+1} < 10 and m+1 must be more or equal to 10")
        return promptM()
    return m


def promptN(m: int) -> int:
    print(f">>    Insert value for n - degree of an interpolation polynome")
    inpt = input()
    try:
        n = int(inpt)
    except ValueError:
        print(f">>    Error: {inpt} is not an int value")
        return promptN(m)
    if n > m:
        print(f">>    Error: {n} > {m} and n must be less than of equal to m")
        return promptN(m)
    return n


def promptFloat() -> float:
    print(f">>    Insert value for Y")
    inpt = input()
    try:
        Y = float(inpt)
    except ValueError:
        print(f">>    Error: {inpt} is not a float value")
        return promptFloat()
    return Y
