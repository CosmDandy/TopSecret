n = int(input())
A = list()
for i in range(n):
    x = input()
    A.append(x)
a = input()
for j in range(len(A)):
    if a in A[j]:
        print(A[j])
    else:
        continue
