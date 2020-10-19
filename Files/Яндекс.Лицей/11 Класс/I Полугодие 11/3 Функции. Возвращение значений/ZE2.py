def prime(number):
    if number == 2 or number == 3 or number == 5 or number == 7:
        return "Простое число"
    else:
        if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
            return "Простое число"
        else:
            return "Составное число"
