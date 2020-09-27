n = int(input())
X = list()
for i in range(n):
    a = input()
    X.append(a)
s = int(input())
for j in X:
    if len(j) >= s:
        print(j[s - 1], end="")
    else:
        continue
