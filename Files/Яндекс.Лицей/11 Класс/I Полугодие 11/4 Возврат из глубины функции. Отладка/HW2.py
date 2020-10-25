def supercargo_2(load, capacity):
    load_ln = list(load)
    x = list(load)
    load_lk = []
    capacity_l = list(capacity)
    for i in range(len(load)):
        if 1 <= load[i] <= 9 and capacity_l[0] != 0 and capacity_l[1] == 0 and capacity_l[2] == 0:
            capacity_l[0] -= 1
            load_lk.append(load[i])
        elif 10 <= load[i] <= 99 and capacity_l[1] != 0 and capacity_l[2] == 0:
            capacity_l[1] -= 1
            load_lk.append(load[i])
        elif 100 <= load[i] <= 999 and capacity_l[2] != 0:
            capacity_l[2] -= 1
            load_lk.append(load[i])
    for i in load_ln:
        if i in load_lk:
            x.remove(i)
            load_lk.remove(i)
    if capacity_l[0] == 0 and capacity_l[1] == 0 and capacity_l[2] == 0:
        return tuple(x), True
    else:
        return tuple(x), False
