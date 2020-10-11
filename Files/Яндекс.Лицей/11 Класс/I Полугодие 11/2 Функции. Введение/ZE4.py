def squared():
    for i in range(11, 100):
        x = i ** 2
        if i % 10 == 9:
            if len(str(x)) == 3:
                print(str(x), end="")
            else:
                print(str(x), end="")
        elif i % 10 == 0:
            print()
            continue
        else:
            if len(str(x)) == 3:
                print(str(x), end="  ")
            else:
                print(str(x), end=" ")
