def larger_root(p, q):
    x1 = ((-p) + discriminant(1, p, q) ** 0.5) / 2
    x2 = ((-p) - discriminant(1, p, q) ** 0.5) / 2
    if x1 > x2:
        return x1
    else:
        return x2


def smaller_root(p, q):
    x1 = ((-p) + discriminant(1, p, q) ** 0.5) / 2
    x2 = ((-p) - discriminant(1, p, q) ** 0.5) / 2
    if x1 < x2:
        return x1
    else:
        return x2


def discriminant(a, b, c):
    d = b ** 2 - 4 * a * c
    return d


def main():
    p = float(input())
    q = float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))
