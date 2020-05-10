s = 0
for i in range(6):
    n = int(input())
    if n % 10 == 5:
        s += n
print(s)


s = 0
while n != -1:
    n = int(input())
    if n % 10 == 6 or n % 10 == 8:
        s += n
print(s / 2)


max = 0
for i in range(10):
    n = int(input())
    if n > max:
        max = n
print(max)

