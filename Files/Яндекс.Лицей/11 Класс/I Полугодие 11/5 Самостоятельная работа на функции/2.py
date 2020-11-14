def dict_wishes(lines):
    data = {}
    x = []
    for i in range(len(lines)):
        if lines[i].split()[0] not in data:
            x.clear()
        x.append(" ".join(lines[i].split()[1::]))
        data[lines[i].split()[0]] = x.copy()
    return data


lines = ['Страшила мозги',
 'Страшила острый ум',
 'Железный_Дровосек '
 'доброе сердце',
 'Дороти вернуться '
 'домой',
 'Дороти вместе с Тото']
result = dict_wishes(lines)
print(result)