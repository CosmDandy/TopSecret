x = list()


def print_only_new(message):
    if message not in x:
        x.append(message)
        print(message)
