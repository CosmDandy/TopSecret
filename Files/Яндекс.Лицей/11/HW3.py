a = ""
x = 0
y = 0
i = 0
while a != "СТОП":
    a = input()
    y += 1
    if "Кот" in a or "кот" in a:
        x += 1
        if i == 0:
            i = y
    else:
        continue
if x >= 1:
    print(x)
    print(i)
else:
    print(x)
    print(-1)
