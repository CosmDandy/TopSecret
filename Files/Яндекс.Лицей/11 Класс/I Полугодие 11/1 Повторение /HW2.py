x = input().split()
for i in range(len(x)):
    xn = x[i]
    if xn[-1] == "m" and xn[-2] == "u" and len(xn) <= 8:
        print(xn.capitalize())
