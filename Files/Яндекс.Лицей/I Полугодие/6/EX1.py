a = float(input())
if abs(a) <= 1 * (10**-6) or a == 0:
    print(float(1000000))
else:
    print(1 / a)
