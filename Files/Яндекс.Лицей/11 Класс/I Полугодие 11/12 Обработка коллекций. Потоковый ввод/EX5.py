import sys
x = list(filter(lambda x: x != '' and x[0] == '#', map(str.strip, sys.stdin)))
print(len(x))
