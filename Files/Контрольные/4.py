n = int(input())
a = None
t = None
error = False
sm = 0
s = 0
x = 0
for i in range(n):
    while a != "КОНЕЦ СКОПЛЕНИЯ" and t != "КОНЕЦ СКОПЛЕНИЯ":
        a = input()
        if a != "КОНЕЦ СКОПЛЕНИЯ":
            t = input()
            if t != "КОНЕЦ СКОПЛЕНИЯ":
                t1 = float(t)
                dt = 200 * (1 + float(a))
                s = float(dt) + float(t1)
                if float(s) <= 13.799:
                    if s > sm:
                        sm = s
                        continue
                    if s >= 12.5:
                        x += 1
                        continue
                else:
                    error = True
                    continue
            else:
                break
        else:
            break
    else:
        break
    if error:
        print("ОШИБКА СКАНИРОВАНИЯ")
    else:
        print(x)
print("Возраст самой старой звезды", sm, "млрд лет.")