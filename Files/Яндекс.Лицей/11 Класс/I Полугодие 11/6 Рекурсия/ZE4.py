def rec_linear_sum(some_list):
    if some_list in (1, 2):
        return 0
    if some_list in (3,):
        return 1
    return rec_linear_sum(some_list - 1) + rec_linear_sum(some_list - 2) + rec_linear_sum(
        some_list - 3)


print(rec_linear_sum([1, 2, 3, 4]))
