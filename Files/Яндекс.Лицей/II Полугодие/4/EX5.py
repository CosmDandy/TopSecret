n = int(input())
A = list()
a = None
for i in range(n):
    x = input()
    A.append(x)
sa = int(input())
for u in range(sa):
    a = input()
    for j in range(len(A)):
        if a not in A[j]:
            del A[j]
            print(A)
        else:
            continue
for l in A:
    print(l)
