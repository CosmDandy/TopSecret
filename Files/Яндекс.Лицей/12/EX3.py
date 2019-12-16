n = int(input())
x = 1
w = 1
while x <= n:
    for i in range(w):
        if x <= n:
            x += 1
            print(x - 1, end=" ")
        else:
            break
    w += 1
    print()
