n = int(input())
m = int(input())
x = list()
xn = xk = s = 0
y = set()
y0 = []
flag = False
for i in range(n):
    x.append(i)
for i in range(m):
    x1 = int(input())
    x2 = int(input())
    if x2 - x1 != n - 1:
        if x2 < n - 1:
            y.add(x[x2 + 1])
        elif x2 == n - 1:
            y.add(x[x2])
        y.add(x[x1 - 1])
    else:
        flag = True
        print(0)
if not flag:
    print(x, y)
    y = sorted(y)
    x.clear()
    print(x, y)
    for i in range(0, m + 1, 2):
        x.append([y[i], y[i + 1]])
    for i in range(len(x)):
        if x[i][1] - x[i][0] >= s:
            s = x[i][1] - x[i][0]
            xn = x[i][0]
            xk = x[i][1]
    print(s + 1)
    print(xn, xk)
