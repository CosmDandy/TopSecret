m = int(input())
M = set()
X = set()
s = 1
for i in range(m):
    n = int(input())
    for j in range(n):
        x = input()
        if m % 2 == 0:
            if x not in M:
                M.add(x)
                s += 1
            else:
                if s % 2 != 0:
                    X.add(x)
                else:
                    X.discard(x)
        else:
            print(1)
print(M, X, s)