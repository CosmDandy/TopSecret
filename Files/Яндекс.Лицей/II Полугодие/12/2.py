b = {'янв': [], 'фев': [], 'мар': [], 'апр': [],
     'май': [], 'июн': [], 'июл': [], 'авг': [],
     'сен': [], 'окт': [], 'ноя': [], 'дек': []}
for i in range(int(input())):
    a = input().split()
    b[a[2]].append([a[0], a[1]])
    if a[2] not in b:
        continue
for i in range(int(input())):
    a = input()
    c = []
    if a in b:
        if len(b[a]) >= 2:
            b[a].sort()
            for k in range(len(b[a]) - 1):
                for j in range(len(b[a]) - 1 - k):
                    if int(b[a][j][1]) > int(b[a][j + 1][1]):
                        b[a][j], b[a][j + 1] = b[a][j + 1], b[a][j]
            for k in range(len(b[a])):
                n = ' '.join(b[a][k])
                c.append(n)
            print(' '.join(c))
        elif len(b[a]) == 1:
            n = ' '.join(b[a][0])
            c.append(n)
            print(' '.join(c))
        else:
            print()