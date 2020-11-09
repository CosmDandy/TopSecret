x = list()
n = 0


def add_item(item_name, item_cost):
    x.append([item_name, item_cost])


def print_receipt():
    global n
    s = 0
    if len(x) != 0:
        n += 1
        print("Чек " + str(n) + ".", "Всего предметов:", len(x))
        for i in range(len(x)):
            print(x[i][0], "-", x[i][1])
            s += x[i][1]
        print("Итого:", s)
        print("-----")
    x.clear()
