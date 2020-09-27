a = input()
m = []
while a != '':
    m.append(a)
    a = input()
for i in range(int(input())):
    b = input()
    f = 0
    for j in range(len(m)):
        if m[j] == b:
            del m[j]
            f = 1
            break
    if f == 1:
        print('Есть в наличии')
    else:
        print('Нет в наличии')
