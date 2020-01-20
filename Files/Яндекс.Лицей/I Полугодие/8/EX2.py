a = 0
x = 0
while a >= 0:
    a = float(input())
    if a > 0:
        if a >= 1000:
            x += a - ((a / 100) * 5)
        else:
            x += a
print(x)
