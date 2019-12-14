war = "Евразия"
peace = "Остазия"
e = 1
n = int(input())
for i in range(n):
    x = input()
    if x == "С кем война?":
        print(war)
    elif x == "С кем мир?":
        print(peace)
    elif x == "Меняем":
        e += 1
        if e % 2 == 0:
            war = "Остазия"
            peace = "Евразия"
        elif e % 2 >= 1:
            war = "Евразия"
            peace = "Остазия"
