def solve(*coefficients):
    korn = []
    dl = len(coefficients)
    if dl == 3:
        a, b, c = coefficients[0], coefficients[1], coefficients[2]
        d = b ** 2 - 4 * a * c
        if d > 0:
            x1 = (-b + d ** 0.5) // (a + a)
            x2 = (-b - d ** 0.5) // (a + a)
            korn.append(x1)
            korn.append(x2)
        elif d == 0:
            korn.append(-b // 2 * a)
    if dl == 2:
        b, c = coefficients[0], coefficients[1]
        korn.append(-c / b)
        print(*korn)
    if dl == 1:
        if coefficients[0] == 0:
            korn.append('all')
    print(*korn)


n = [int(i) for i in input().split()]
if len(n) == 1:
    solve(n[0])
if len(n) == 2:
    solve(n[0], n[1])
if len(n) == 3:
    solve(n[0], n[1], n[2])
