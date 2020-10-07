def print_document(pages):
    flag = False
    for i in pages:
        if "Секретно" in i:
            flag = True
            break
        else:
            print(i)
    if not flag:
        print("Напечатано без купюр")
    else:
        print('Дальнейшие материалы засекречены')
