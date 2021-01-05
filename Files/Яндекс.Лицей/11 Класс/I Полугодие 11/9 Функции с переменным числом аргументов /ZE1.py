def solve(*coefficients):
    global x
    if len(coefficients) == 3:
        a = coefficients[0]
        b = coefficients[1]
        c = coefficients[2]
        d = b ** 2 - 4 * a * c
        if d >= 0:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            x.append(x1)
            if x1 == x2:
                return x
            else:
                x.append(x2)
                return x
        else:
            return x
    elif len(coefficients) == 2:
        b = coefficients[0]
        c = coefficients[1]
        x.append(-c / b)
        return x
    elif len(coefficients) == 1:
        if coefficients[0] == 0:
            return ['all']
        else:
            return x
    else:
        return None


x = []
