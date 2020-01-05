x = int(input())
n = 1
s = 0
while n != x:
    n += 1
    for i in range(1, n + 1):
        if n % i != 0 and n == 0:
            continue
        else:
            if i == 1 or i == n:
                print(n)
                break
