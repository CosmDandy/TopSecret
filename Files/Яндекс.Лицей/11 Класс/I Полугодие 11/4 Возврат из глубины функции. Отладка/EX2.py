def warmer_day(temperature):
    a = []
    s = 0
    for i in range(len(temperature)):
        a.extend(temperature[i])
    x = sum(a) // len(a)
    for i in a:
        s += 1
        if i > x:
            return s
