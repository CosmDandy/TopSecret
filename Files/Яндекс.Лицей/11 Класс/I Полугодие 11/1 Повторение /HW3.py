x = None
a = list()
while x != "":
    x = input()
    a.append(x)
xa = input().split(" ")
answer = 0
q = 0
flag = False
for i in range(len(a) - 1):
    b = a[i].split(" ")
    if xa[0] in b[0]:
        answer += int(b[-1])
        q += 1
        flag = True
if answer == 0:
    print("Нет предмета")
elif 4.5 < answer / 3 <= 5:
    print(0)
elif flag:
    s = 0
    while answer / q <= 4.5 or q < 3:
        q += 1
        answer += 5
        s += 1
    print(s)
