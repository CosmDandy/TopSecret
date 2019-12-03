A = int(input())
B = int(input())
C = int(input())
D = int(input())
A1 = str(A)
B1 = str(B)
C1 = str(C)
D1 = str(D)
s = 0
d = 0
y = -1
A0 = [i for i in range(0, 10001, 2)]
while d <= 5000:
    y += 1
    F = A0[y]
    if F < 10:
        x = "000" + str(F)
    elif 10 <= F < 100:
        x = "00" + str(F)
    elif 100 <= F < 1000:
        x = "0" + str(F)
    elif 1000 <= F <= 10000:
        x = str(F)
    d += 1
    if A1 not in x:
        if x[0] == B1 or x[0] == C1 or x[0] == D1:
            f4_1 = int(x[0]) + int(x[1])
            f4_2 = int(x[2]) + int(x[3])
            if f4_1 == f4_2:
                if f4_1 % 2 != 0:
                    s += 1
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        continue
print(s)
