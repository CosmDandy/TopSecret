n = int(input())
X = list()
for i in range(n):
    a = input()
    X.append(a)
s = int(input())
for j in range(s):
    b = int(input())
    print(X[b - 1])
