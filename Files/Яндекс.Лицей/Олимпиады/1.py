import math

hh = int(input())
mm = int(input())
x = int(input())
if x != 0:
    a = (math.ceil((x / 100) * 7.25)) + mm
    a1 = a % 60
    a2 = a // 60
    hh += 1 * a2
    mm = 0
    mm += a1
else:
    a = 0
if hh > 23:
    b = hh // 24
    hh -= 24 * b
if a >= 60:
    if mm < 10:
        print(str(hh) + ":" + ("0" + str(mm)))
    else:
        print(str(hh) + ":" + str(mm))
else:
    if mm >= 60:
        a3 = a + mm
    else:
        a3 = a
    if mm < 10:
        print(str(hh) + ":" + ("0" + str(a3)))
    else:
        print(str(hh) + ":" + str(a3))
