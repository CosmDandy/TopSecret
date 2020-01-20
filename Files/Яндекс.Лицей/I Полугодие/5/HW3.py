a = float(input())
b = float(input())
c = str(input())
if (c == '+' or c == "-" or c == "*" or c == "/") and b != 0:
    if c == '+':
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        print(a / b)
else:
    print("888888")