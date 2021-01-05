def from_string_to_list(string, container):
    if string != "":
        x = list()
        for i in string.split():
            x.append(int(i))
        container.extend(x)
