def print_average(arr):
    s = 0
    n = 0
    for i in range(len(list(arr))):
        s += arr[i]
        n += 1
    if not list(arr):
        print(0)
    else:
        print(s / n)
