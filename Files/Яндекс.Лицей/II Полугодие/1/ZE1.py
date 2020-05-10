P = set()
PT = set()
m = int(input())
for i in range(m):
    P.add(input())
n = int(input())
for i in range(n):
    a = input()
    na = int(input())
    for j in range(na):
        PT.add(input())
        if PT in P:
            print(a)
            P.discard(PT)
