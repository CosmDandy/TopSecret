X = set()
x = input()
s = 0
for i in range(len(x)):
    if ord(x[i]) not in X:
        X.add(ord(x[i]))
        s += 1
print(str(min(X)) + ",", max(X))
if s <= 32:
    print("ХВАТИТ")
else:
    print("НЕ ХВАТИТ")
