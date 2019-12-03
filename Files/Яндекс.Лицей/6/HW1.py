a = int(input())
x1 = a // 100
x2 = a // 10
x3 = a - (10 * x2)
x2 = x2 - (10 * x1)

c = min(x1, x2, x3)
a = max(x1, x2, x3)

if x2 < x1 < x3 or x3 < x1 < x2:
    x2 = x1
elif x1 < x2 < x3 or x3 < x2 < x1:
    x2 = x2
else:
    x2 = x3
if (a + c) / 2 == x2:
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")
# print(a)
# print(x2)
# print(c)
# a = list(input())
# x1 = max(a)
# x2 = min(a)
# if