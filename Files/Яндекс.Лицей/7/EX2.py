a = input()
b = input()
if len(a) >= 8:
    if a == b:
        print("OK")
    else:
        print("Различаются.")
else:
    print("Короткий!")