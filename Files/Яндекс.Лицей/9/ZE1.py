a = int(input())
if a <= 0:
    while a <= 0:
        a = int(input())
if a > 0:
    while a >= 0:
        if a >= 4:
            b = a // 4
            c = a - b * 4
            if c > 0:
                print("Взято:", c)
                a -= c
                print("Осталось:", a)
                b = int(input())
                if b <= 3 and b > 0:
                    a -= b
                    print("Осталось:", a)
                else:
                    while b > 3 or b < 1:
                        print("Осталось:", a,
                              "Вы взяли некорректное число камней")
                        b = int(input())
                    if (b <= 3) and (b > 0):
                        print("Взято:", b)
                        a -= b
                        print("Осталось:", a)
            elif c == 0:
                print("Взято:", 1)
                a -= 1
                print("Осталось:", a)
                b = int(input())
                if b <= 3 and b > 0:
                    a -= b
                    print("Осталось:", a)
                else:
                    while b > 3 or b < 1:
                        print("Осталось:", a,
                              "Вы взяли некорректное число камней")
                        b = int(input())
                    if (b <= 3) and (b > 0):
                        print("Взято:", b)
                        a -= b
                        print("Осталось:", a)
        elif a < 4:
            if a == 3:
                print("Взято:", 3)
                print("Осталось: 0")
                print("Победил ИИ")
                a = -1
            elif a == 2:
                print("Взято:", 2)
                print("Осталось: 0")
                print("Победил ИИ")
                a = -1
            elif a == 1:
                print("Взято:", 1)
                print("Осталось: 0")
                print("Победил ИИ")
                a = -1
            elif a == 0:
                print("Победил Игрок")
                a = -1
