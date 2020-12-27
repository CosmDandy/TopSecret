def search_fruit(shops, fruit):
    n = False
    for i in shops:
        for j in shops[i]:
            for k in shops[i][j]:
                if fruit in k:
                    n = True
                    return i, j
    if not n:
        return None, None
