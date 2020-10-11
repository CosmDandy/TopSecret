n = int(input())
A = set()
B = set()
s1 = 0
s2 = 0
a = None
b = None
a = input()
while a != "":
    b = input()
    for i in a:
        A.add(i)
    for l in b:
        B.add(l)
    for j in range(len(A)):
        x = A.symmetric_difference(B)
        xl = len(x)
    if xl <= n:
        s1 += 1
    elif xl > n:
        s2 += 1
    a = input()
    A = set()
    B = set()
print(s1)
print(s2)
