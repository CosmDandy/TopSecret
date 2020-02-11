M = set()
N = set()
nm = int(input())
for i in range(nm):
    m = input()
    M.add(m)
nn = int(input())
for j in range(nn):
    n = input()
    N.add(n)
D = M.symmetric_difference(N)
for i in D:
    print(i)
