x = int(input())
n = 0
s = 0
while n != x:
    n += 1
    if x % n == 0:
        print(n, end=' ')
        s += 1
if s == 2:
    print("\nПРОСТОЕ")
else:
    print("\nНЕТ")
