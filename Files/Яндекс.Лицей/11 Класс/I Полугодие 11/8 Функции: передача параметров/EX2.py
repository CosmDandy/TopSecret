def count_food(days):
    x = 0
    for i in range(len(days)):
        x += daily_food[days[i] - 1]
    return x
