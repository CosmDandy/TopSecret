b = {}
c = []
n = int(input())
for i in range(n):
    a = input().split()
    b[a[0]] = a[1]
    c.append(a[0])
c.sort()
f = []
for j in c:
    print(j + ':', b[j])
    k = b.pop(j)
    if k not in b:
        b[k] = []
        b[k].append(j)
    else:
        b[k].append(j)
        b[k].sort()
        f.append(b[k])
print()
d = []
m = 0
for p in b:
    d.append(int(p))
    d.sort()
for p in d:
    p = str(p)
    print(p + ':', ', '.join(b[p]))
    if len(b[p]) >= m:
        m = len(b[p])
        n = p
print()
print(n)
