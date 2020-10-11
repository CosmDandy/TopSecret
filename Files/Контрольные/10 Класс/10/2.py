x = input()
X = list()
flag = 1
Q = list("-0123456789")
while x[0] not in Q:
    X.append(x)
    x = input()
    if x[0] in Q:
        break
U = x.split()
for j in range(len(U)):
    if "-" not in U[j]:
        flag = 1
    else:
        flag = 0
        print(-1)
        break
if flag == 1:
    F = list()
    y = 0
    for i in range(len(X)):
        if len(X[i]) > int(U[i]):
            F.append(X[i][int(U[i]) - 1].upper())
            y += 1
        else:
            break
    if y == len(X):
        print(''.join(F))
    else:
        print(-1)
