expression = input()
s = 0
for velocity in range(5, 5000):
    if eval(expression):
        s += 1
print(s)
