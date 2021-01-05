def choose_coffee(*like_coffee):
    resepts = {"Эспрессо": [1, 0, 0], "Капучино": [1, 3, 0], "Маккиато": [2, 1, 0],
               "Кофе по-венски": [1, 0, 2], "Латте Маккиато": [1, 2, 1],
               "Кон Панна": [1, 0, 1]}
    for i in like_coffee:
        if ingredients[0] - resepts[i][0] >= 0 and \
                ingredients[1] - resepts[i][1] >= 0 and \
                ingredients[2] - resepts[i][2] >= 0:
            ingredients[0] -= resepts[i][0]
            ingredients[1] -= resepts[i][1]
            ingredients[2] -= resepts[i][2]
            return i
    return 'К сожалению, не можем предложить Вам напиток'
