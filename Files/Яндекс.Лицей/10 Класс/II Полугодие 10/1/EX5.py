nm = int(input())
nn = int(input())
nk = int(input())
M = set()
N = set()
K = set()
for i in range(nm + nn + nk):
    x = input()
    if x not in M:
        M.add(x)
    elif x not in N:
        N.add(x)
    else:
        K.add(x)
x = ((M & N) | (M & K) | (K & N)) - (M & N & K)
if len(x) != 0:
    print(len(x))
else:
    print("NO")
