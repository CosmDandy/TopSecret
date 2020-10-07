x = input().split()
s = 0
Y = []
for i in x:
    if (i[0] != "К" and i[0] != "З") and (i[2] == "Ж" or i[2] == "К" or (i[2] == "С" and i[0] != "С")) and (
            i[3] == "С" or i[3] == "З" or (i[3] == "Г" and i[1] != "Г")):
        s += 1
        Y.append(i)
print(s)
for i in Y:
    print(i, end=" ")
