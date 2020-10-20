def decimal_translator(number, base):
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
    else:
        return None
