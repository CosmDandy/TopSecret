x = filter(lambda x: x % 9 == 0, range(10, 100))
x = map(lambda x: x ** 2, x)
print(sum(x))