def cached(func):
    d = dict()

    def decorated_func(*args, **kwargs):
        nonlocal d
        if args[0] not in d:
            result = func(*args, **kwargs)
            d[args[0]] = result
        else:
            result = d[args[0]]
        return result

    return decorated_func
