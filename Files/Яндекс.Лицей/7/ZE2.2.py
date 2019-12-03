targetx = int(input())
targety = int(input())
direction = int(0)
directiont = "север"
a = ""
x = 0
y = 0
answer = 0
while a != "стоп":
    if x == targetx:
        if y == targety:
            print(answer)
            print(directiont)
            break
    a = input()
    if a == "налево" or a == "направо" or a == "разворот":
        if a == "налево":
            direction -= 1
        elif a == "направо":
            direction += 1
        elif a == "разворот":
            direction += 2
            if direction >= 4:
                direction -= 4
        if direction >= 4:
            direction -= 4
        if direction <= -4:
            direction += 4
    elif a == "вперёд":
        b = input()
        if direction == 0:
            y += int(b)
            directiont = "север"
        elif direction == 2 or direction == -2:
            y -= int(b)
            directiont = "юг"
        elif direction == 1 or direction == -3:
            x += int(b)
            directiont = "восток"
        elif direction == 3 or direction == -1:
            x -= int(b)
            directiont = "запад"
    answer += 1
