data = {}


def add_friends(name_of_person, list_of_friends):
    global data
    if list_of_friends != data[name_of_person]:
        data[name_of_person] = list_of_friends
    print(data[name_of_person])


add_friends("Алла", ["Марина", "Иван"])
add_friends("Алла", ["Мария"])
