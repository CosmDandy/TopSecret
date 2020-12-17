def late(now, classes, bus):
    time = (int(classes.split(":")[0]) - int(now.split(":")[0])) * 60 + int(
        classes.split(":")[1]) - int(now.split(":")[1])
    for i in range(len(bus) - 1, 0, -1):
        if time - bus[i] + 5 - 15 > 0:
            answer = "Выйти через " + str(bus[i] - 5) + " минут"
            return answer
    else:
        return "Опоздание"


print(late('12:00', '12:40', [0, 1, 4, 6, 25]))
print(late('9:20', '9:35', [4, 25, 30]))

print(late('12:59', '13:45', [3, 35, 46, 55]))
print(late('13:50', '14:30', [7, 17, 35, 48]))
