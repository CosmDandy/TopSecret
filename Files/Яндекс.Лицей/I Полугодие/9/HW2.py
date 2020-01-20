a = int(input())
x = 0
while a > 1:
    x += 1 + a % 2
    a //= 2
    print(a)
print(x)
