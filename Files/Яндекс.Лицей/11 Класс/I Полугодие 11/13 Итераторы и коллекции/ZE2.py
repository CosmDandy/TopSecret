import sys


def f(x):
    x = x.split('\t')
    del x[0]
    return sum(list(map(int, x)))


d = list(map(str.strip, sys.stdin))
books, *price = d
books = books.split('\t')
price = min(price, key=f)
price = price.split('\t')
print(price[0])
out = list(zip(books, price[1:]))
for k in range(len(out)):
    print(*out[k], sep='\t')
