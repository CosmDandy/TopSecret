A = input()
A = A.split()
x = 0
for i in A:
    x += 1
    if x % 3 == 0:
        print(i, ' ', sep='', end='')