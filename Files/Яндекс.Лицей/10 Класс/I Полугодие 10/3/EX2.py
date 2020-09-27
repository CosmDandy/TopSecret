a = str(input())
b = str(input())
c = str(input())
if c == '>' and a > b:
    print(a)
elif c == '<':
    print(b)
elif b > a:
    print(b)
else:
    print(a)
