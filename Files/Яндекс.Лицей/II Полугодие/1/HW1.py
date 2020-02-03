nm = int(input())
nn = int(input())
M = set()
N = set()
for i in range(nm):
    m = input()
    M.add(m)
for j in range(nn):
    n = input()
    N.add(n)
    if n in M:
        print("YES")
    else:
        print("NO")

