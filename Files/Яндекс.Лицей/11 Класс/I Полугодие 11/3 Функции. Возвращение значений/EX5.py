def find_mountain(heightsMap):
    row = -1
    x = 0
    for i in heightsMap:
        if max(i) > x:
            x = max(i)
    for i in heightsMap:
        row += 1
        column = -1
        for j in i:
            column += 1
            if j == x:
                return row, column
