x1 = int(input(""))
x2 = int(input(""))
x3 = int(input(""))
nim = x1 ^ x2 ^ x3
print(nim)
if nim > 0:
    if x1 ^ nim < x1:
        dif = x1 - (x1 ^ nim)
        x1 -= dif
        get = x1
        num = 1
    elif x2 ^ nim < x2:
        dif = x2 - (x2 ^ nim)
        x2 -= dif
        get = x2
        num = 2
    else:
        dif = x3 - (x3 ^ nim)
        x3 -= dif
        get = x3
        num = 3
else:
    x1 -= 1
    dif = 1
    num = 1
    get = x1
print("Я забрал " + str(dif) + " камней из " + str(
    num) + " кучи, теперь там " + str(get) + " камней. Твой ход")
while x1 + x2 + x3 > 0:
    step = 2
    num = 0
    while num < 1 or num > 3:
        num = int(input("Из какой кучи? "))
        if num == 1 and x1 == 0 or num == 2 and x2 == 0 or num == 3 and x3 == 0:
            print("Здесь уже нет камней!")
            num = 0
    con = True
    while con:
        if num == 1:
            get = x1
        elif num == 2:
            get = x2
        else:
            get = x3
        dif = int(input("Сколько (но не больше " + str(get) + ")?"))
        if dif > 0 and dif <= get:
            if num == 1:
                x1 -= dif
                get = x1
            elif num == 2:
                x2 -= dif
                get = x2
            else:
                x3 -= dif
                get = x3
            print("Ты забрал " + str(dif) + " камней из " + str(
                num) + " кучи, теперь там " + str(get) + " камней. Мой ход")
            con = False
    if x1 + x2 + x3 > 0:
        step = 1
        nim = x1 ^ x2 ^ x3
        if nim > 0:
            if x1 ^ nim < x1:
                dif = x1 - (x1 ^ nim)
                x1 -= dif
                get = x1
                num = 1
            elif x2 ^ nim < x2:
                dif = x2 - (x2 ^ nim)
                x2 -= dif
                get = x2
                num = 2
            else:
                dif = x3 - (x3 ^ nim)
                x3 -= dif
                get = x3
                num = 3
        else:
            if x1 > 0:
                x1 -= 1
                num = 1
                get = x1
            elif x2 > 0:
                x2 -= 1
                num = 2
                get = x2
            else:
                x3 -= 1
                num = 3
                get = x3
            dif = 1
        print("Я забрал " + str(dif) + " камней из " + str(
            num) + " кучи, теперь там " + str(get) + " камней. Твой ход")
if step == 1:
    print("Я победил")
else:
    print("Ты победил")
