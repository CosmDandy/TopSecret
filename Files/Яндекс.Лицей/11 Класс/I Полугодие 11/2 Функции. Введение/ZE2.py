def golden_ratio(i):
    fib1 = fib2 = fib3 = fib4 = 1
    if i == 1:
        print(float(1))
    else:
        for i in range(i - 1):
            fib1, fib2 = fib2, fib1 + fib2
        for i in range(i):
            fib3, fib4 = fib4, fib3 + fib4
        print(float(fib2 / fib4))
