x1 = int(input(""))
x2 = int(input(""))
x3 = int(input(""))
step = 0
n = x1 ^ x2 ^ x3
if n > 0:
    if x1 ^ n < x1:
        s = x1 - (x1 ^ n)
        x1 -= s
        ng = x1
        xn = 1
    elif x2 ^ n < x2:
        s = x2 - (x2 ^ n)
        x2 -= s
        ng = x2
        xn = 2
    else:
        s = x3 - (x3 ^ n)
        x3 -= s
        ng = x3
        xn = 3
else:
    x1 -= 1
    s = 1
    xn = 1
    ng = x1
print("ИИ забрал:", str(s))
print("Из кучи:", str(xn))
print("В этой куче осталось:", str(ng), "камня(ей).")
while x1 + x2 + x3 > 0:
    step = 2
    xn = 0
    while xn < 1 or xn > 3:
        xn = int(input("Из какой кучи взять? "))
        if xn == 1 and x1 == 0 or xn == 2 and x2 == 0 or xn == 3 and x3 == 0:
            print("В этой куче нет камней")
            xn = 0
    con = True
    while con:
        if xn == 1:
            ng = x1
        elif xn == 2:
            ng = x2
        else:
            ng = x3
        s = int(input("Сколько взять(Не больше" + str(ng) + ")?"))
        if s > 0 and s <= ng:
            if xn == 1:
                x1 -= s
                ng = x1
            elif xn == 2:
                x2 -= s
                ng = x2
            else:
                x3 -= s
                ng = x3
            print("Игрок забрал:", str(s))
            print("Из кучи:", str(xn))
            print("В этой куче осталось:", str(ng), "камня(ей).")
            con = False
    if x1 + x2 + x3 > 0:
        step = 1
        n = x1 ^ x2 ^ x3
        if n > 0:
            if x1 ^ n < x1:
                s = x1 - (x1 ^ n)
                x1 -= s
                ng = x1
                xn = 1
            elif x2 ^ n < x2:
                s = x2 - (x2 ^ n)
                x2 -= s
                ng = x2
                xn = 2
            else:
                s = x3 - (x3 ^ n)
                x3 -= s
                ng = x3
                xn = 3
        else:
            if x1 > 0:
                x1 -= 1
                xn = 1
                ng = x1
            elif x2 > 0:
                x2 -= 1
                xn = 2
                ng = x2
            else:
                x3 -= 1
                xn = 3
                ng = x3
            s = 1
        print("ИИ забрал:", str(s))
        print("Из кучи:", str(xn))
        print("В этой куче осталось:", str(ng), "камня(ей).")
if step == 1:
    print("Победил ИИ")
else:
    print("Победил Игрок")
