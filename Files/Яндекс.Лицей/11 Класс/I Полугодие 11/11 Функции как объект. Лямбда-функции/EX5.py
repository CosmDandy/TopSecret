x = list(map(lambda x: sum(1 for i in x if i.lower() in 'ёуеыаоэяию'),
             input().split()))
sr = sum(x) / len(x)
x = list(filter(lambda x: x, map(lambda x: x - sr, x)))
if len(x) == 0:
    print('Парам пам-пам')
else:
    print('Пам парам')
