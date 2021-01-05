def patagonian_growth():
    for i in range(len(growth)):
        for j in range(len(growth[i])):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                growth[i][j] = growth[i][j] + growth[i][j - 1]
            elif j == 0:
                growth[i][j] = growth[i][j] + growth[i - 1][j]
            else:
                growth[i][j] = growth[i][j] + min(growth[i][j - 1], growth[i - 1][j])
    return growth
