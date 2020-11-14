def creaks_and_groans(n, list_):
    x = list_.copy()
    for i in range(0, len(list_), n):
        x.remove(list_[i])
    print("".join(x))
