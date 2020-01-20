x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
a = x2
b = x4
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
NOK = x2 * x4 // b
c = x1 * (NOK // x2)
d = x3 * (NOK // x4)
answer1 = c - d
answer2 = NOK
a1 = answer1
b1 = answer2
while a1 != b1:
    if a1 > b1:
        a1 -= b1
    else:
        b1 -= a1
if answer2 % b1 == 0:
    print(str(answer1 // b1) + "/" + str(answer2 // b1))
else:
    print(str(answer1) + "/" + str(answer2))
