a = int(input())
x = []
for i in range(a):
    b = int(input())
    x.append(any([int(input()[-1]) == 5 for j in range(b)]))
if all(x):
    print('ДА')
else:
    print('НЕТ')
