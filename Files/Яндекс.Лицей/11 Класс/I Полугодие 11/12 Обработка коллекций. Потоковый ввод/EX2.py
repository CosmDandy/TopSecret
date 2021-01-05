import sys


def mis(x):
    x = list(x)
    for i in range(len(x)):
        x[i] = int(x[i])
    return sum(x)


x = []
for line in sys.stdin:
    x.append(line.rstrip('\n'))
x = sorted(x, key=lambda x: mis(x))
ms = mis(x[0])
x = filter(lambda x: mis(x) == ms, x)
x = sorted(x, reverse=True, key=lambda x: len(x))
ml = len(x[0])
x = filter(lambda x: len(x) == ml, x)
x = min(x, key=int)
print(x)
