import math

y = int(input())
y1s = (2397 + y) // 60
if (2397 + y) % 60 == 0:
    y1s -= 1
y2s = abs((2397 + y) - (((2397 + y) // 12) * 12))
if y2s == 0:
    y2s = 12
y3s = math.ceil(((2397 + y) % 10) / 2)
if y3s == 0:
    y3s = 5
if (2397 + y) % 2 != 0:
    y4s = 1
else:
    y4s = 2
print(y1s, y2s, y3s, y4s, sep="\n")
