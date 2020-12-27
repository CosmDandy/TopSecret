def palindrome(n):
    x = []
    y = []
    n = n.split(" ")
    n1 = "".join(n)
    for i in range(len(n1)):
        x.append(n1[i].lower())
        y.append(n1[i].lower())
    x.reverse()
    if "".join(x) == "".join(y):
        return True
    else:
        return False


def prime(number):
    d = 2
    while d * d <= number and number % d != 0:
        d += 1
    if d * d > number:
        return True
    else:
        return False


def check_pin(pinCode):
    pinCode = pinCode.split("-")
    if prime(int(pinCode[0])) and palindrome(pinCode[1]) and (
            int(pinCode[2]) ** 0.5 == int(int(pinCode[2]) ** 0.5) or int(pinCode[2]) == 2):
        return "Корректен"
    else:
        return "Некорректен"
