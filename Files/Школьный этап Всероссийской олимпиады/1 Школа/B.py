k = int(input())
x = int(input())
s = x
if x + s * (k / 100) != round(x + s * (k / 100)):
    while x + s * (k / 100) != round(x + s * (k / 100)):
        s += 1
    print(s)
else:
    print(x)
