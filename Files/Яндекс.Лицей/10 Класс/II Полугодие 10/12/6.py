a = [float(i) for i in input().split()]
b = {'до 10': [], 'от 10 до 100': [], 'от 100 до 1000': [], 'свыше 1000': []}
e = 'до 10'
r = 'от 10 до 100'
t = 'от 100 до 1000'
y = 'свыше 1000'
for i in range(len(a)):
    if a[i] < 10:
        b[e].append(a[i])
    elif (a[i] > 10) and (a[i] < 100):
        b[r].append(a[i])
    elif (a[i] >= 100) and (a[i] <= 1000):
        b[t].append(a[i])
    else:
        b[y].append(a[i])
if len(b[e]) > 0:
    print(e + ':', str(len(b[e])) + ',', round(sum(b[e]) / len(b[e]), 1))
if len(b[r]) > 0:
    print(r + ':', str(len(b[r])) + ',', round(sum(b[r]) / len(b[r]), 1))
if len(b[t]) > 0:
    print(t + ':', str(len(b[t])) + ',', round(sum(b[t]) / len(b[t]), 1))
if len(b[y]) > 0:
    print(y + ':', str(len(b[y])) + ',', round(sum(b[y]) / len(b[y]), 1))
