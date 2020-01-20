a = -1
x = 10
s = 0
while a != 0:
    a = int(input())
    if x != 0:
        x -= a
        s += 1
    else:
        continue
print(s)
