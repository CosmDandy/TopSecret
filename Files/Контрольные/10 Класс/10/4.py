Y = ["аиёеоуыэюя"]
x = input()
S = 0
s = 0
for i in range(len(x)):
    if x[i] in Y:
        S += 1
        print(x)
while x != "ПОЛЮС!":
    x = input()
    for i in range(len(x)):
        if x[i] in Y:
            s += 1
    if s <= S:
        print(x)
