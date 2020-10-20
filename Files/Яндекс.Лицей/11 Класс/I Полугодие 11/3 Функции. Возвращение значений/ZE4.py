import copy

# a = []
# z = []
# print("Введите строки исходного поля: (Без пробелов и иных разделителей)")
# for i in range(4):
#    a.append(list(input()))
#    print(a)

a = [['x', 'x', 'x', '.'], ['.', '.', '.', '.'], ['x', '.', 'x', 'x'], ['x', '.', '.', '.']]
z = []


def hor(x):
    z.clear()
    for i in range(len(x)):
        s = x[i]
        s.reverse()
        z.append(s)
    return z


def vert(x):
    z.clear()
    for i in range(len(x) - 1, -1, -1):
        s = x[i]
        z.append(s)
    return z


def trans(x):
    z.clear()
    for i in range(len(x)):
        s = list(x[0][i] + x[1][i] + x[2][i] + x[3][i])
        z.append(s)
    return z


print(a)
print(hor(a))
print(vert(a))
print(trans(a))
print(list(hor(list(vert(a)))))
