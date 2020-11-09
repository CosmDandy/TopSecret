s1 = int(input())
s2 = int(input())
n = 0
while s1 != s2 and s1 < s2:
    if s1 % 2 == 0:
        s1 = s1 * 2 + 1
    else:
        s1 *= 2
    n += 1
if s1 == s2:
    print(n)
else:
    print(0)
