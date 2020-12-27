def late(now, classes, bus):
    time = (int(classes.split(":")[0]) - int(now.split(":")[0])) * 60 + int(
        classes.split(":")[1]) - int(now.split(":")[1])
    for i in range(len(bus) - 1, 0, -1):
        if 5 < bus[i] < time:
            if bus[i] + 15 <= time:
                answer = "Выйти через " + str(bus[i] - 5) + " минут"
                return answer
    else:
        return "Опоздание"
