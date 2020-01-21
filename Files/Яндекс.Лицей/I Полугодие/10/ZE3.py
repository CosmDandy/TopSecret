n = int(input())
s = 0
if n > 0:
    for i in range(1, n + 1):
        x = int(input())
        if i % 2 == 0:
            s -= x
        else:
            s += x
print(s)