a = float(input())
t = float(input())
p = float(input())
if 1.88 <= a <= 1.92:
    if 2.72491 <= t <= 2.72605:
        if 400 <= p <= 500:
            print("Реликтовое")
        else:
            print("Не реликтовое")
    else:
        print("Не реликтовое")
else:
    print("Не реликтовое")
