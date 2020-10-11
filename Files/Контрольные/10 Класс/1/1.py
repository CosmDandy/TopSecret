n = int(input())
if n > 3:
    a = 0
    print(str(a) + ',', end=" ")
    b = 0
    print(str(b) + ',', end=" ")
    c = 1
    print(str(c) + ',', end=" ")
    for i in range(n - 3):
        x = a + b + c
        print(str(x) + ',', end=" ")
        a = b
        b = c
        c = x
elif n == 3:
    a = 0
    print(str(a) + ',', end=" ")
    b = 0
    print(str(b) + ',', end=" ")
    c = 1
    print(str(c) + ',', end=" ")