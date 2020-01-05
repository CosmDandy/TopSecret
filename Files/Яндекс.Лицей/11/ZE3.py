a = -1
value_l = 0
value_h = 0
s = 0
while a != 0:
    a = int(input())
    if value_l == 0:
        value_l = a
    if a != 0:
        if a > value_h:
            s += 1
            if a > value_h:
                value_h = a
                s += 1
            else:
                s = 0
            if a < value_l:
                value_l = a
        else:
            s = 0

    else:
        break
print(value_l, value_h)
