x = []


def sorting_logs(data, asc):
    for i in range(len(data)):
        if asc == "True":
            x.append(data[i].copy().sort())
        else:
            x.append(data[i].copy().sort(reverse=True))
        return x


original = [
    [2, 1, 5, 3, 4],
    [6, 1, 3, 5, 2],
    [4, 2, 0, 1, 7]
]
asc = True
result = sorting_logs(original, asc)
print('Original:')
print(*original, sep='\n')
print('Result:')
print(*result, sep='\n')
