a = int(input())
x1 = a // 100
x2 = a // 10
x3 = a - (10 * x2)
x2 = x2 - (10 * x1)
if x1 == x2 == x3:
    print("В числе все цифры одинаковые")
elif x1 == x2 or x2 == x3 or x1 == x3:
    print("В числе две одинаковые цифры")
else:
    print("ОК")
