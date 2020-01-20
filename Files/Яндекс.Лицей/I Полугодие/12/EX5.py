n = int(input())
x = 0
for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            x = x + 1
    if x == 0:
        print(i)
    else:
        x = 0
