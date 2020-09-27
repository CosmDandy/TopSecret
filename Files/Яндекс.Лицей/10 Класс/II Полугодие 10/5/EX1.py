n = int(input())
X = list()
flag = False
for i in range(n):
    x = int(input())
    X.append(x)
y = int(input())
for i in range(n):
    for j in range(i + 1, n):
        if X[i] * X[j] == y:
            print("ДА")
            flag = True
            break
    if flag:
        break
else:
    print("НЕТ")
