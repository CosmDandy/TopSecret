targetx = int(input())
targety = int(input())
direction = int(0)
directiont = ""
a = ""
x = 0
y = 0
answer1 = 0
answer2 = ""
while a != "стоп":
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
    if x == targetx and y == targety:
        answer1 = 0
    elif x == targetx or y == targety:
        answer1 = 2
    elif x != targetx or y != targety:
        answer1 = 3
print(answer1)
print(directiont)
