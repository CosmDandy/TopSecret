def vowels_in_string(line):
    s = ["а", "я", "о", "ё", "у", "ю", "э", "е", "ы", "и", "a", "e", "u", "i", "o", "y"]
    x = []
    for i in range(len(line)):
        if line[i].lower() in s:
            x.append(line[i])
    return x
