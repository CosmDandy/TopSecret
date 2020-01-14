x1 = int(input(""))
x2 = int(input(""))
step = 1
n = x1 ^ x2
if x1 == 0 and x2 == 0:
    print("Нет камней")
else:
    if n > 0:
        if x1 ^ n < x1:
            s = x1 - (x1 ^ n)
            x1 -= s
            ng = x1
            xn = 1
        else:
            s = x2 - (x2 ^ n)
            x2 -= s
            ng = x2
            xn = 2
    else:
        x1 -= 1
        s = 1
        xn = 1
        ng = x1
    print("ИИ забрал:", str(s))
    print("Из кучи:", str(xn))
    print("В этой куче осталось:", str(ng), "камня(ей).")
    while x1 + x2 > 0:
        step = 2
        xn = 0
        while xn < 1 or xn > 2:
            xn = int(input("Из какой кучи взять? "))
            if xn == 1 and x1 == 0 or xn == 2 and x2 == 0:
                print("В этой куче нет камней")
                xn = 0
        con = True
        while con:
            if xn == 1:
                ng = x1
            else:
                ng = x2
            s = int(input("Сколько взять(Не больше" + str(ng) + ")?"))
            if s > 0 and s <= ng:
                if xn == 1:
                    x1 -= s
                    ng = x1
                else:
                    x2 -= s
                    ng = x2
                print("Игрок забрал:", str(s))
                print("Из кучи:", str(xn))
                print("В этой куче осталось:", str(ng), "камня(ей).")
                con = False
        if x1 + x2 > 0:
            step = 1
            n = x1 ^ x2
            if n > 0:
                if x1 ^ n < x1:
                    s = x1 - (x1 ^ n)
                    x1 -= s
                    ng = x1
                    xn = 1
                else:
                    s = x2 - (x2 ^ n)
                    x2 -= s
                    ng = x2
                    xn = 2
            else:
                if x1 > 0:
                    x1 -= 1
                    xn = 1
                    ng = x1
                else:
                    x2 -= 1
                    xn = 2
                    ng = x2
                s = 1
            print("ИИ забрал:", str(s))
            print("Из кучи:", str(xn))
            print("В этой куче осталось:", str(ng), "камня(ей).")
    if step == 1:
        print("Победил ИИ")
    else:
        print("Победил Игрок")
