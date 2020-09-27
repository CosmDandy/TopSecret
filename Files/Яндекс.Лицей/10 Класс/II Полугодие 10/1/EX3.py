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
D = M.symmetric_difference(N)
Dl = len(D)
if Dl > 0:
    print(Dl)
else:
    print("NO")
