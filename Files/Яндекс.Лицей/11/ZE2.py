s = int(input())
z = 1
answer = ""
y = 0
while s != 0:
    a = input()
    if z == 1:
        answer = "раз"
    elif z == 2:
        answer = "два"
    elif z == 3:
        answer = "три"
    elif z == 4:
        answer = "четыре"
    if z < 4:
        if a == answer:
            y += 1
            z += 1
        else:
            print("Правильных отсчётов было", str(y) + ",",
                  "но теперь вы ошиблись.")
            y = 0
            z = 1
            s -= 1
    else:
        y += 1
        z = 1
        continue
print("На сегодня хватит.")
