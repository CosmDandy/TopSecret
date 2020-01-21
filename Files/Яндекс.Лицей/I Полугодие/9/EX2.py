x = int(input())
x1 = 0
x2 = 1
x3 = 0
if x != 0:
    print(1)
while x3 <= x:
    x3 = x1 + x2
    x1 = x3
    if x3 <= x:
        print(x3)
    x3 = x1 + x2
    x2 = x3
    if x3 <= x:
        print(x3)
