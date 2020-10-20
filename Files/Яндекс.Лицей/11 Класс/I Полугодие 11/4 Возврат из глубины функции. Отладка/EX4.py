def supercargo(load, capacity):
    load_ln = list(load)
    load_lk = []
    capacity_l = list(capacity)
    for i in range(len(load)):
        if 1 <= load[i] <= 9 and capacity_l[0] != 0:
            capacity_l[0] -= 1
            load_lk.append(load[i])
        elif 10 <= load[i] <= 99 and capacity_l[1] != 0:
            capacity_l[1] -= 1
            load_lk.append(load[i])
        elif 100 <= load[i] <= 999 and capacity_l[2] != 0:
            capacity_l[2] -= 1
            load_lk.append(load[i])
    x = list(set(load_ln) - set(load_lk))
    if capacity_l[0] == 0 and capacity_l[1] == 0 and capacity_l[2] == 0:
        return tuple(x), True
    else:
        return tuple(x), False
