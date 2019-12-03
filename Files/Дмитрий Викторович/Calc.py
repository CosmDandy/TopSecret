import math
x0 = ""
while x0 != "stop":
    x = input()
    a = float(input())
    if x == "!":
        print(math.factorial(a))
    elif x == "/":
        b = float(input())
        print(a / b)
    elif x == "*":
        b = float(input())
        print(a * b)
    elif x == "-":
        b = float(input())
        print(a - b)
    elif x == "+":
        b = float(input())
        print(a + b)
    else:
        print("888888")
        continue
