x = None
i = 3
X = set()
s = 0
i = 1
while x != "Всегда найдется что съесть":
    x = input()
    for j in x[::(i * 2)]:
        if s <= 4:
            X.add(j)
            xl = len(X)
        else:
            break
    if (xl - (i + 2)) >= 8:
        print(x)
        X.clear()
        s += 1
        i += 1
    else:
        X.clear()
        break
