import sys


def usl(x):
    c = 0
    for i in range(len(x)):
        if shablon[i] == '0' and x[i] in 'aeiouy' or shablon[i] == '*' and x[i] not in 'aeiouy':
            c += 1
    return c


x = map(str.strip, sys.stdin)
shablon, *x = x
shablon = list(shablon)
x = sorted(x, key=lambda x: [-usl(x), x[::-1]])
print('\n'.join(x))
