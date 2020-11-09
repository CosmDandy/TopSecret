x = list()


def print_without_duplicates(message):
    if message not in x or message != x[-1]:
        x.append(message)
        print(message)
