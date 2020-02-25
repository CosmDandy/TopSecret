a = input().split()
b = ['*' * int(i) for i in a]
for i in a:
    print('*' * int(i))