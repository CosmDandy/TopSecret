x1 = int(input())
x2 = int(input())
print("Ход ИИ:")
if x1 > x2:
    xr = x1 - x2
    x1 -= xr
    print("Я взял из первой кучи", xr)
elif x2 > x1:
    xr = x2 - x1
    x2 -= xr
    print("Я взял из второй кучи", xr)
else:
    x1 -= 1
    print("Я взял из первой кучи 1")
print(x1, x2)
while (x1 + x2) > 0:
    print("Ваш ход:")
    y = int(input("Куча "))
    c = int(input("Кол-во камней "))
    if 0 < y <= 2:
        if c > 0:
            if c <= x1 or c <= x2:
                if y == 1:
                    x1 -= c
                elif y == 2:
                    x2 -= c
                print(x1, x2)
                print("Ход ИИ:")
                if y == 1:
                    x2 -= c
                    print("Я взял из первой кучи", c)
                elif y == 2:
                    x1 -= c
                    print("Я взял из второй кучи", c)
                print(x1, x2)
            else:
                print("Неправильный ввод")
                continue
        else:
            print("Неправильный ввод")
            continue
    else:
        print("Неправильный ввод")
        continue
