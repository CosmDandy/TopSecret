import sys
x = list(map(int, map(str.strip, sys.stdin)))
if x:
    print(sum(x) / len(x))
else:
    print(-1)
