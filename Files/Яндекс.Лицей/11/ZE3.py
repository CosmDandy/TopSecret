x1 = int(input())
x2 = int(input())
xl = 0
xh = 0
flag = False
while x2 != 0:
    if flag is False:
        if x1 < x2:
            xl = x2
            flag = True
    if flag:
        if x1 > x2:
            xh = x2
            break
    x1 = x2
    x2 = int(input())
print(xl, xh, xh - xl)
