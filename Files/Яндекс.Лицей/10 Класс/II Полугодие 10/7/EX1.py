A = list(input())
B = list(input())
s = 0
for i in range(int(B[0]), int(B[3]) + 1):
    s += A[i]
print(s)