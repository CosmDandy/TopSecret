locate = 1
locate1 = 0
key = 0
while locate != 12:
    if locate == 1:
        print("Вы находитесь на развилке:")
        print("Пойти прямо (Впереди еще одна развилка)")
        print("Пойти налево (Справа темный подвал)")
        print("Пойти направо (Слева длинная лестница)")
        answer = input()
        if answer == "Пойти прямо":
            locate = 8
            continue
        elif answer == "Пойти налево":
            locate = 2
        elif answer == "Пойти направо":
            locate = 3
        else:
            locate1 = 1
    elif locate1 == 1:
        locate = locate + 1
        print("ошибка")
        answer = input()
        locate1 = 0
        continue

    elif locate == 2:
        print("Вы спустились в подвал и вас там закрыли")
        print("Конец")
        break
    elif locate == 3:
        print("Вы находитесь на развилке:")
        print("Пойти прямо (Впереди еще одна развилка)")
        print("Пойти налево (Слева комната)")
        print("Пойти назад")
        answer = input()
        if answer == "Пойти прямо":
            locate = 5
        elif answer == "Пойти налево":
            locate = 4
        elif answer == "Пойти назад":
            locate = 1
            continue
        else:
            locate1 = 0
    elif locate == 4:
        print("Вы нашли тупик")
        print("Пойти назад")
        answer = input()
        if answer == "Пойти назад":
            locate = 3
            continue
        else:
            locate1 = 0
    elif locate == 5:
        print("Вы находитесь на развилке:")
        print("Пойти налево (Слева еще одна развилка)")
        print("Пойти назад")
        answer = input()
        if answer == "Пойти налево":
            locate = 6
        elif answer == "Пойти назад":
            locate = 3
            continue
        else:
            locate1 = 0
    elif locate == 6:
        print("Вы находитесь на развилке:")
        print("Пойти прямо (Впереди тунель)")
        print("Пойти назад")
        answer = input()
        if answer == "Пойти прямо":
            locate = 7
        elif answer == "Пойти назад":
            locate = 5
            continue
        else:
            locate1 = 0
    elif locate == 7:
        print("Вы находитесь на развилке:")
        print("Пойти налево (Впереди еще одна развилка)")
        print("Пойти направо (Слева еще одна развилка)")
        print("Пойти назад")
        answer = input()
        if answer == "Пойти налево":
            locate = 8
            print("За вами закрылась дверь")
        elif answer == "Пойти направо":
            locate = 1
            print("Вы вернулись в начало")
            print("ВЫ НАШЛИ КЛЮЧ !!!")
            key = 4625
            print("Код от замка: 4625")
        elif answer == "Пойти назад":
            locate = 5
            continue
        else:
            locate1 = 0
    elif locate == 8:
        print("Вы находитесь на развилке:")
        print("Пойти прямо (Впереди гермодверь)")
        print("Пойти налево (Справа тонель)")
        print("Пойти направо (Слева тонель)")
        print("Пойти назад")
        answer = input()
        if answer == "Пойти прямо":
            locate = 11
            continue
        elif answer == "Пойти налево":
            locate = 9
        elif answer == "Пойти направо":
            locate = 10
        elif answer == "Пойти назад":
            locate = 1
            continue
        else:
            locate1 = 0
    elif locate == 9:
        print("Вы вернулись в начало")
        locate = 1
    elif locate == 10:
        print("Вы попали в другую временную петлю, где нет лабиринта")
        break
    elif locate == 11:
        print("Перед вами гермодверь")
        print("ВВЕДИТЕ ПАРОЛЬ")
        password = input()
        if key == 4625:
            print("Вы выбрались из ЛАБИРИНТА !!!")
            break
        elif password != key:
            locate = 8
            continue
        else:
            locate1 = 0
