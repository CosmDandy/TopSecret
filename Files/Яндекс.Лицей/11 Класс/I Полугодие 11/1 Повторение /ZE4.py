n = int(input())
a = input().lower().split(" ")
x = list()
xs = list()
s = [0, []]
for i in range(len(a)):
    if len(a[i]) == n:
        for j in range(n):
            if a[i][j] not in xs:
                xs.append(a[i][j])
        x.append([a[i], xs.copy()])
        xs.clear()
for i in range(len(x)):
    for j in range(i + 1, len(x)):
        if len(set(x[i][1]) ^ set(x[j][1])) >= s[0]:
            s = [len(set(x[i][1]) ^ set(x[j][1])), [x[i][0], x[j][0]]]
if not s[1]:
    print(None)
else:
    print(" ".join(s[1]))
