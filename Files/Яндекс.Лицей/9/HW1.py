x1 = int(input())
x2 = int(input())
a = x1
b = x2
while (a + b) > 0:
    y = int(input())
    c = int(input())
    if y == 1:
        a -= c
    elif y == 2:
        b -= c
    print(a, b)
