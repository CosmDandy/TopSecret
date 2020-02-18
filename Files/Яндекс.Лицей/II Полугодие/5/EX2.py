n = int(input())
X = list()
for i in range(n):
    a = input()
    X.append(a)
for i in X:
    print(i)
print()
for j in range(n):
    if X[j][-1] == "5" or X[j][-1] == "4":
        print(X[j])
    else:
        continue
