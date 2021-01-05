start, *data, finish = input().split()
for i in range(len(data) - 1, -1, -1):
    if start.lower() > data[i].lower() or data[i].lower() > finish.lower():
        del data[i]
print(*data)