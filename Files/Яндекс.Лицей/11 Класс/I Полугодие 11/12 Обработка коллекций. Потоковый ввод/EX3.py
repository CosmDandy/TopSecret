rooms = int(input())
x = []
for i in range(rooms):
    kolvo = int(input())
    x.append(any([int(input()[-1]) == 5 for j in range(kolvo)]))
if all(x):
    print('ДА')
else:
    print('НЕТ')