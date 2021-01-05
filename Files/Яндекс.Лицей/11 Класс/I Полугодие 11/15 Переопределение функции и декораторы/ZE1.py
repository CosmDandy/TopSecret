new_print = print


def print_(*args):
    args = list(map(lambda x: x.upper(), args))
    return new_print(*args)


print = print_