count = 0


def spring_outside(item):
    global count
    if "spring" in item.lower():
        count += 1
        return "This is about spring " + str(count) + " times."
    else:
        return "It's not about spring."
