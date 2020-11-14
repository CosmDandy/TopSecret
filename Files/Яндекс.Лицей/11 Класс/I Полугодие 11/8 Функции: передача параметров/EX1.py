x = list()


def parrot(phrase):
    if phrase in x:
        print(phrase)
    else:
        x.append(phrase)
