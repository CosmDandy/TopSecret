n = int(input())
x = 1
xs = 0
ns = 0
while ns != n:
    if ns < n:
        y = x + xs
        xs += 1
        ns += y
    else:
        x += 1
        ns = 0
        xs = 0
        continue
print(x)
