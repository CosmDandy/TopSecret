a = input()
n = int(input())
if 0 < n <= len(a):
    print(a[n - 1])
else:
    print("ОШИБКА")
