a = ""
xs = 0
while a != "СТОП":
    if "Кот" in a or "кот" in a:
        print(xs)
        break
    a = input()
    xs += 1
else:
    print(-1)
