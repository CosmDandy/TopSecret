n = int(input())
ship = 1
sx = 1
s = 0
for i in range(n):
    s = sx
    for j in range(sx):
        s -= 1
        print("Осталось секунд:", s)
    print("Пуск", ship)
    sx += 1
    ship += 1
