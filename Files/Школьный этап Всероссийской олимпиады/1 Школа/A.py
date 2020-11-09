n = list(input())
a = str(input())
while str(n).count(a) != 0:
    n.remove(a)
if n != list():
    while n[0] == "0":
        del n[0]
    print("".join(n))
else:
    print(-1)