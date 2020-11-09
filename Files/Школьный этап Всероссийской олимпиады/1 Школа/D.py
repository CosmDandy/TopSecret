a = int(input())
n = int(input())
m = int(input())
sl = sm = 0
if n == 0 and m == 0:
    print("0 0")
elif n == 0 and m > 0:
    print("-1 -1")
else:
    if m > 0:
        if n > m:
            sl = n
        else:
            sl = a * n + a * (m - n)
        if 2 * n == m and n > 1:
            sm = a * n + a * m
        else:
            sm = a * n + a * (m - 1)
    else:
        sl = sm = a * n
    print(sl, sm)
