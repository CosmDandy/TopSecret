def decimal_translator_2(number, base):
    alp = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11,
           "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21,
           "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    answer = 0
    a = []
    flag = True
    for i in range((len(str(number)))):
        if int(str(number)[i]) < base:
            a.append(str(number)[i])
        else:
            flag = False
            return None
    a.reverse()
    if flag and (2 <= base <= 9):
        for i in range(len(str(number))):
            x = int(a[i]) * (base ** i)
            answer += x
        return answer
    elif:

    else:
        return None
