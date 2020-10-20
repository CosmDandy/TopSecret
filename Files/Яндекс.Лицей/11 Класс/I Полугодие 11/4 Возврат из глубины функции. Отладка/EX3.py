def triangle(n):
    alp = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11,
           "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21,
           "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    d = 0
    x = []
    if n.isdigit():
        n = int(n)
    elif n.isalpha():
        for key in n.upper():
            x.append(alp[key])
        n = sum(x)
    else:
        return False
    d = 1 - 4 * (-2 * n)
    x1 = (-1 + (d ** 0.5)) / 2
    x2 = (-1 - (d ** 0.5)) / 2
    if x1 > 0 and x1 == int(x1):
        return int(x1)
    elif x2 > 0 and x2 == int(x2):
        return int(x2)
    else:
        return False
