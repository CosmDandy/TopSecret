b = {}
for i in range(int(input())):
    a = input().split()
    if a[2] not in b:
        b[a[2]] = [a[0]]
    elif a[2] in b:
        b[a[2]].append(a[0])
        b[a[2]].sort()
for i in range(int(input())):
    a = input()
    if a in b:
        print(' '.join(b[a]))
    else:
        print()