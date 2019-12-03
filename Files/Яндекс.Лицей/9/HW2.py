n = int(input())
x = 1
s = 0
while x <= n:
    if x % 2 >= 1:
        x -= 1
    else:
        x *= 2
    s += 1
print(s)
