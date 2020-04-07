x = input().split(" Спичечник ")
A = list()
for i in range(len(x)):
    if "солнце" in x[i]:
        A.append(x[i])
print("! ".join(A))