import sys
m = 0
n = []
for line in sys.stdin:
    line = line.split()
    a = []
    b = list(line)
    for i in line:
        if i.isdigit():
            a.append(i)
    if len(a) > m:
        m = len(a)
        n.clear()
        if m == 1:
            for i in a:
                n.append(i)
        else:
            k = 0
            for i in a:
                k += int(i)
            n.append(k)
    elif len(a) == m and len(a) > 0:
        if m == 1:
            for i in a:
                n.append(i)
        else:
            k = 0
            for i in a:
                k += int(i)
            n.append(k)
if bool(n):
    n = list(n)
    print(min(n))
else:
    print('-1')