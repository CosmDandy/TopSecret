import sys


d = map(str.strip, sys.stdin)
d0 = []
for i in d:
    i = ''.join(list(filter(lambda x: x.isalpha() or x == ' ', list(i))))
    d0 += i.split()
d = list(filter(lambda x: x[1][0] == x[1][0].upper(), enumerate(d0)))
d = sorted(d, key=lambda x: x[1])
for i in range(len(d) - 1, 0, -1):
    if d[i][1] == d[i - 1][1]:
        del d[i]
for i in d:
    print(i[0], i[1], sep=' - ')
