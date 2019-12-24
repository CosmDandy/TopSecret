x = int(input())
if x == 0 or 0 < x < 2:
    print("None")
else:
    if x % 5 == 0:
        print("пентакварки")
    elif x % 4 == 0:
        print("тетракварки")
    elif x % 3 == 0:
        print("барионы")
    elif x % 2 == 0:
        print("мезоны")
    else:
        print("None")
