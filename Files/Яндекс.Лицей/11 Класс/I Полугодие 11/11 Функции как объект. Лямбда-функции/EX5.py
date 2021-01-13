x = list(map(lambda x: sum(1 for i in x if i.lower() in 'ёуеыаоэяию'),
             input().split()))
s = sum(x) / len(x)
x = list(filter(lambda x: x, map(lambda x: x - s, x)))
if len(x) == 0:
    print('Парам пам-пам')
else:
    print('Пам парам')
