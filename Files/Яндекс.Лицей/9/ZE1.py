x = int(input())
g = 1
xs = 0
while x > 1:
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
    if x == 1:

        print("Победил Игрок")
    else:
        xs = 0
        g = 0
        while g > 3 or g < 1 or g > x:
            print("Вы  берете:")
            g = int(input())
        x -= g
        print("Осталось камней:", x)
        if x == 1:
            print("Победил ИИ")
