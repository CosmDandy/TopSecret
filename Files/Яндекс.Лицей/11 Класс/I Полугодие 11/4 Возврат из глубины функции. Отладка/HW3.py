def create_polygon_number(n, q):
    return int(n + (q - 2) * (n * (n - 1) / 2))


def check_polygon_number(number):
    num2n1 = list()
    num2n2 = list()
    num2 = list()
    kl = list()
    if number == 2:
        return None, None
    else:
        for i in range((2 * number) - 1, 0, -1):
            if (2 * number) % i == 0:
                num2n1.append(i)
        for i in range(((2 * number) - 2) - 1, 0, -1):
            if ((2 * number) - 2) % i == 0:
                num2n2.append(i)
        for i in range(len(num2n1)):
            if num2n1[i] - 1 in num2n2:
                num2.append(num2n1[i])
        num2.sort()
        for i in range(len(num2)):
            k = int(((2 * number - 2) / (num2[i] - 1)) - ((2 * number) / num2[i]) + 2)
            if 3 <= k:
                kl.append([num2[i], k])
        a = (kl[-1:][0][0], kl[-1:][0][1])
        return a
