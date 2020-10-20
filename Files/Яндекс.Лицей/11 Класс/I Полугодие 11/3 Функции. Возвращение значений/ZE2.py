def prime(number):
    d = 2
    while d * d <= number and number % d != 0:
        d += 1
    if d * d > number:
        return "Простое число"
    else:
        return "Составное число"
