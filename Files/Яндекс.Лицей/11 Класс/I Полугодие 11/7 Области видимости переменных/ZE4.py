x = dict()


def get_transactions(t):
    global x
    if t == "print_it":
        for i in x:
            print(x.get(i)[1], i, x.get(i)[0])
    else:
        t = (" ".join(t.split("-"))).split(":")
        if t[0].split(" ")[1] in x:
            x[t[0].split(" ")[1]][0] += int(t[1])
            x[t[0].split(" ")[1]][1] += 1
        else:
            key = t[0].split(" ")[1]
            x[key] = [int(t[1]), 1]
