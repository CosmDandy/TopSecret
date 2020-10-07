x = int(input())
y = int(input())
z = int(input())
s = 0
for i in range(x + y + z):
    if (y <= i < x) or i <= z:
        s += 1
    else:
        continue
print(s)
