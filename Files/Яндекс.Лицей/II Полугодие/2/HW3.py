n = int(input())
x = input()
X = set()
for i in range(len(x)):
    print(chr(ord(x) + n))
