x1 = int(input())
x2 = int(input())
x3 = int(input())
a = x1
b = x2
c = x3
while (a + b + c) > 0:
    y1 = int(input())
    z = int(input())
    if y1 == 1:
        a -= z
    elif y1 == 2:
        b -= z
    elif y1 == 3:
        c -= z
    print(a, b, c)
