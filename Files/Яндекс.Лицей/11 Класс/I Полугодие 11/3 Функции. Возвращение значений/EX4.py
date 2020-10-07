def average(arr):
    s = 0
    n = 0
    for i in range(len(list(arr))):
        s += arr[i]
        n += 1
    if len(list(arr)) == 0:
        return 0
    else:
        return s / n
