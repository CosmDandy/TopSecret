a = None
x0 = 0
hmax = 150
hmin = 190
while a != "!":
    a = input()
    if a != "!":
        x = int(a)
        if 150 <= x <= 190:
            x0 += 1
            if x > hmax:
                hmax = x
            if x < hmin:
                hmin = x
print(x0)
print(hmin, hmax)
