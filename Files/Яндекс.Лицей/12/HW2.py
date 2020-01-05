y1 = int(input())
x1 = int(input())
symbol = input()
x = 0
y = 0
for i in range(y1):
    if i == 0 or i == y1 - 1:
        print(symbol * x1)
    else:
        print(symbol + " " * (x1 - 2) + symbol)
