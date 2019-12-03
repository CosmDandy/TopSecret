a = int(input())
b = int(input())
c = int(input())
x1 = max(a, b, c)
if b < a < c or c < a < b:
    x2 = a
elif a < b < c or c < b < a:
    x2 = b
else:
    x2 = c
x3 = min(a, b, c)
print(x1)
print(x2)
print(x3)
