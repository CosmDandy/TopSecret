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
        return "Палиндром"
    else:
        return "Не палиндром"
