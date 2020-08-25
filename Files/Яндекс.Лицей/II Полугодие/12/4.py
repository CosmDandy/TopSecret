a = input()
m = {}
while a != '':
    b = a.split()
    m[b[1]] = b[0][:len(b[0]) - 1]
    a = input()
for i in range(int(input())):
    a = input()
    print(m[a])