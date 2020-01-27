b1 = float(input())
q = float(input())
n = float(input())
if q == 1:
    print(b1 * n)
else:
    s = (b1 * (1 - (q ** n))) / (1 - q)
    print(s)