n = int(input())
x1 = 0
x2 = 0
x3 = 0
x4 = 0
for i in range(n):
    t = int(input())
    if t > 30000:
        x1 += 1
    elif 10000 < t <= 30000:
        x2 += 1
    elif 7500 < t <= 10000:
        x3 += 1
    elif 6000 < t <= 7500:
        x4 += 1
print("Класс O:", x1)
print("Класс B:", x2)
print("Класс A:", x3)
print("Класс F:", x4)
