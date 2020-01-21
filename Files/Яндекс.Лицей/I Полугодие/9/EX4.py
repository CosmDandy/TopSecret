a = int(input())
x = a
while x != 0:
    b = int(input())
    if b > x:
        print(x)
        continue
    elif b > 3:
        print(x)
        continue
    elif b <= 0:
        print(x)
        continue
    else:
        x -= b
        print(x)
