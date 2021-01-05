def check_password(fun):
    password = input()

    def new_func(arg):
        nonlocal password
        if password == 'пароль':
            return fun(arg)
        print('В доступе отказано')

    return new_func


@check_password
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)