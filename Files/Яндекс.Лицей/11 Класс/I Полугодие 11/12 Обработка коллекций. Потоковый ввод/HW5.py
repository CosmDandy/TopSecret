import sys
n = []
for line in sys.stdin:
    n.append(line.lstrip().rstrip())


def code(a: str):
    a = a.upper()
    return ord(a) - ord("A") + 1


print(*sorted(n, key=lambda x: (sum([code(i) for i in x]), x)), sep="\n")
