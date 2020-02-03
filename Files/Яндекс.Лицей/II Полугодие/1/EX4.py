nm = int(input())
nn = int(input())
M = set()
N = set()
for i in range(nm + nn):
    x = input()
    if x not in M:
        M.add(x)
    else:
        N.add(x)
n = len(M) - len(N)
if n != 0:
    print(n)
else:
    print("NO")