a = input()
b = input()
if "@" not in a and "@" in b:
    print("OK")
elif "@" in a:
    print("Некорректный логин")
elif "@" not in b:
    print("Некорректный адрес")
else:
    print()