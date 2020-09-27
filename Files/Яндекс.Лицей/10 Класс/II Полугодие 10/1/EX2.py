n = int(input())
A = set()
for i in range(n):
    x = input()
    A.add(x)
a = input()
if a in A:
    print("TRY ANOTHER")
else:
    print("OK")
