a = int(input())
x1 = a // 100
x2 = a // 10
x3 = a - (10 * x2)
x2 = x2 - (10 * x1)
a = x1 + x2
b = x2 + x3
y1 = max(a, b)
y2 = min(a, b)
q = str(y1) + str(y2)
print(q)