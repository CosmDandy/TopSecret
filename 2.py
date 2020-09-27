A = [0, 1, 2, 3, 4, 5]
for i in range(len(A)):
    if i > 2:
        A[i] = i * 2
    else:
        A[i] = i * 3
    print(A[i])
