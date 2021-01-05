def matrix(n=1, m=-1, a=0):
    if m == -1:
        m = n
    matr = []
    for i in range(n):
        matr.append([a] * m)
    return matr