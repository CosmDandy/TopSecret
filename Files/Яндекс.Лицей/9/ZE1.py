x = int(input())
g = 1
xs = 0
if x == 0:
    print("В куче нет камней")
else:
    while x > 0:
        xs = x % 4
        if xs == 0:
            xs = 3
        elif xs == 1:
            xs = 1
        else:
            xs -= 1
        print("ИИ взял", xs)
        x -= xs
        print("Осталось камней:", x)
        if x == 0:
            print("Победил ИИ")
        else:
            xs = 0
            g = 0
            while g > 3 or g < 1 or g > x:
                print("Вы  берете:")
                g = int(input())
            x -= g
            print("Осталось камней:", x)
i