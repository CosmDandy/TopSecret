for i in range(10000):
    s = 0
    for j in range(1, i):
        if i % j == 0:
            s += j
    if s > i:
        result = 0
        for j in range(1, s):
            if s % j == 0:
                result += j
        if result == i:
            print(i, s)
