q = [["x x x ."], [". . . ."], ["x . x x"], ["x . . ."]]
qs = []
w = []
for i in range(len(q)):
    s = ("".join(q[i])).split(" ")
    qs.append(s)



def hor(x):
    for i in range(len(x)):
        s = x[i]
        s.reverse()
        w.append(s)
    return w


def vert(x):
    w.clear()
    for i in range(len(x) - 1, -1, -1):
        s = x[i]
        w.append(s)
    return w


def trans(x):
    w.clear()
    for i in range(len(x)):
        s = ("".join(x[0])).split(" ")[i] + ("  ".join(x[1])).split(" ")[i] + \
            ("".join(x[2])).split(" ")[i] + ("".join(x[3])).split(" ")[i]
        w.append(" ".join(s).split(" "))
    return w


print(q)
print(hor(q))
print(vert(q))
print(trans(q))

