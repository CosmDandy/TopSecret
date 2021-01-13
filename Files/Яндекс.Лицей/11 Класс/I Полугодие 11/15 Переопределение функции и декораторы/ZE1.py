new_print = print


def printh(*args):
    args = list(map(lambda x: x.upper(), args))
    return new_print(*args)


print = printh
