n = int(input())
x_min = 10 ** 6
x = 0
xm = 0
ts = 0
max = 0
for i in range(1, n + 1):
    t = int(input())
    for j in range(t):
        ts = int(input())
        if ts < x_min:
            x = i
            x_min = ts
        else:
            continue
    if x_min > max:
        xm = i
        max = x_min
    x_min = 10 ** 6
print(xm, max)
