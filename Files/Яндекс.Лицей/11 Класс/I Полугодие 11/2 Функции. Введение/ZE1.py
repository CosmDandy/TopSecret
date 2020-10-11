def print_statistics(arr):
    if not arr:
        n = 0
        v = 0
        min_n = 0
        max_n = 0
        med = 0
    else:
        n = len(arr)
        v = float(sum(arr) / n)
        min_n = float(min(arr))
        max_n = float(max(arr))
        sorted(arr)
        if len(arr) % 2 != 0:
            med = float(round(arr[len(arr) // 2]))
        else:
            med = float((arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2)
    print(n)
    print(v)
    print(min_n)
    print(max_n)
    print(med)


print_statistics([73, 34, 41, 46, 51])
