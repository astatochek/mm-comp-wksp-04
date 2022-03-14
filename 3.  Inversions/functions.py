

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
    print(f">>    Insert values for m")
    inpt = input()
    try:
        m = int(inpt[0]) - 1
    except ValueError:
        print(f">>    Error: {inpt} is not an int value")
        return promptM()
    if m < 10:
        print(f">>    Error: {m} < 10 and m must be more or equal to 10")
        return promptM()
    return m


