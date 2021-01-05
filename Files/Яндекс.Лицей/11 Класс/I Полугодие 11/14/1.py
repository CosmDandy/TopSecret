import sys

x = sys.stdin.readlines()
a = list()
for i in x:
    i = i.strip().split(" ")
    for j in range(len(i)):
        if i[j][-3:] != "...":
            if len(i[j]) >= 1:
                a.append(i[j])
    print("; ".join(a))
    a.clear()
