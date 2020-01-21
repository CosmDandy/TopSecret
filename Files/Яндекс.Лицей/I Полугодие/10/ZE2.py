import math
n = int(input())
nz = 0
s = 0
x = 0
if n > 1300000:
    print("Error")
else:
    for i in range(1, n + 1):
        x = 1 / (i ** 2)
        s += x
    print((math.pi ** 2) / s)
