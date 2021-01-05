data = {}


def add_friends(name_of_person, list_of_friends):
    global data
    if name_of_person in data:
        key = name_of_person
        for i in list_of_friends:
            data[key].append(i)
    else:
        key = name_of_person
        data[key] = list_of_friends


def are_friends(name_of_person1, name_of_person2):
    key = name_of_person1
    if name_of_person2 in data[key]:
        return True
    return False


def print_friends(name_of_person):
    key = name_of_person
    x = data[key]
    print(" ".join(sorted(x)))
