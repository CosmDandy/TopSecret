def possible_turns(cell):
    n = 0
    sx = []
    letter = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    number = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}
    x = [letter[cell[0]], int(cell[1])]
    s = [[x[0] - 2, x[1] - 1], [x[0] - 2, x[1] + 1], [x[0] - 1, x[1] - 2], [x[0] - 1, x[1] + 2],
         [x[0] + 1, x[1] - 2], [x[0] + 1, x[1] + 2], [x[0] + 2, x[1] - 1], [x[0] + 2, x[1] + 1]]
    while s:
        a = s[n]
        if 0 < a[0] <= 8 and 0 < a[1] <= 8:
            n += 1
            if n == len(s):
                break
            continue
        else:
            del s[n]
            n = 0
    for i in s:
        x = [str(number[i[0]]), str(i[1])]
        sx.append("".join(x))
    return sx
