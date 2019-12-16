n = int(input())
xm = 10 ** 6
x = 0
ts = 0
for i in range(n):
    t = int(input())
    for j in range(t):
        ts = int(input())
        if ts < xm:
            x = n
            xm = ts
        else:
            continue
    if ts < t:
        xm =
print(x, xm)
