a = None
x = 0
y = 1000
p = 500
while a != "=":
    print(p)
    a = input()
    if a == ">":
        x = p
        p = (x + (y - x) // 2)
        continue
    elif a == "<":
        y = p
        p = (y - (y - x) // 2)
        continue
    elif a == "=":
        break
