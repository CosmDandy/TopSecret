print("Введите строки исходного поля: (Без пробелов и иных разделителей)")
a = []
for j in range(4):
    a.append(list(input()))  # создаем матрицу из строчек поля
print()


def hor(x):  # горизонтальное отражение
    z = []  # создает пустой список z
    for i in range(len(x)):  # перебирает матрицу
        s = x[i].copy()  # записывает копию i-того списка
        s.reverse()  # переворачивает копию i-того списка
        z.append(s)  # добавляет s(i-тый список) в матрицу z
    return z  # возвращает матрицу z


def vert(x):  # вертикальное отражение
    z = []
    for i in range(len(x) - 1, -1, -1):  # перебирает матрицу в обратном порядке
        s = x[i].copy()
        z.append(s)
    return z


def trans(x):  # транспонирование
    z = []
    for i in range(len(x)):
        s = list(x[0][i] + x[1][i] + x[2][i] + x[3][i])  # транспонирует i-тый список
        z.append(s)
    return z


def print_table(x):  # выводит поле из строчек в формате 4x4
    for i in x:
        print(" ".join(i))  # выводим i-тую строку с символами разделенным пробелами
    print()


print_table(a.copy())  # исходное поле
print_table(hor(a.copy()))  # горизонтальное отражение
print_table(vert(a.copy()))  # вертикальное отражение
print_table(trans(a.copy()))  # транспонирование
print_table((hor((vert(a.copy())))))  # отражение вдоль горизонтали и вертикали одновременно
print_table(trans(hor(a.copy())))  # горизонтальное отражение, затем транспонирование
print_table(trans(vert(a.copy())))  # вертикальное отражение, затем транспонирование
print_table((hor((vert(trans(a.copy()))))))  # транспонирование, затем два отражения
