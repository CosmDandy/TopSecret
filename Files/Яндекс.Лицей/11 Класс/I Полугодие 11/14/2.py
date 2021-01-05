def peak(x):
    d = dict()
    x = x.split(" ")

    for i in x:
        if i[-1] not in d:
            key = i[-1]
            d[key] = [i]
        else:
            d[i[-1]].append(i)
        if d[i[-1]].count(i) == 2:
            del d[i[-1]][-1]
    return d
