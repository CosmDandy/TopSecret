def lucky(ticket):
    global lastTicket
    if lastTicket == 0:
        return "Счастливый"
    else:
        sx1, sx2, sy1, sy2 = 0, 0, 0, 0
        if len(str(ticket)) < 6:
            nx = len(str(ticket)) // 2
        else:
            nx = 3
        if len(str(lastTicket)) < 6:
            ny = len(str(lastTicket)) // 2
        else:
            ny = 3
        x1 = (" ".join(str(ticket)[:nx])).split(" ")
        for i in x1:
            sx1 += int(i)
        x2 = (" ".join(str(ticket)[-nx:])).split(" ")
        for i in x2:
            sx2 += int(i)
        y1 = (" ".join(str(lastTicket)[:ny])).split(" ")
        for i in y1:
            sy1 += int(i)
        y2 = (" ".join(str(lastTicket)[-ny:])).split(" ")
        for i in y2:
            sy2 += int(i)
        if sx1 == sx2 and sy1 == sy2:
            return "Счастливый"
        else:
            return "Несчастливый"
