n = int(input())
c = []
for i in range(n):
    a = input().split()
    c.append(a)
t = []
while len(c) != 0:
    k = 1
    b = []
    f = int(c[0][0]) // 10 * 10
    d = int(c[0][1]) // 10 * 10
    for i in range(1, len(c)):
        x = int(c[i][0]) // 10 * 10
        y = int(c[i][1]) // 10 * 10
        if x == f and y == d:
            b.append(i)
            k += 1
    t.append(k)
    del c[0]
    d = 1
    for p in b:
        del c[p - d]
        d += 1
t.sort()
print(t[len(t) - 1])
