n = int(input())
A = set()
B = set()
s = 0
for i in range(n):
    x = input()
    if x not in A:
        A.add(x)
    else:
        B.add(x)
        s += 1
print(s + len(B))
