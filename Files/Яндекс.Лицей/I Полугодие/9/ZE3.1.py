p1 = int(input())
p2 = int(input())
p3 = int(input())
z1s = ""
z2s = ""
z3s = ""
n = 0
while p1 != 0:
    p1 //= 2
    z1s += str(p1 % 2)
print(z1s)
while p2 != 0:
    p2 //= 2
    z2s += str(p2 % 2)
print(z2s)
while p3 != 0:
    p3 //= 2
    z3s += str(p3 % 2)
print(z3s)

s = int(z1s) + int(z2s) + int(z3s)
sl = len(str(s))
print(s, sl)
while n != (sl):
    sn = str(s)[n]
    n += 1
    if int(sn) % 2 != 0:
        print(sn, n)
        continue
