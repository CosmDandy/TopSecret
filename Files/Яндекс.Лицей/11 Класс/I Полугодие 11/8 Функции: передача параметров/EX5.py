def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        # sequence = sequence + [next_element] меняем на sequence += [next_element]. Это позволит
        # нам изменить переменную sequence так как в изначальном варианте она не глобальная
        # следовательно она не меняется. += позволяет нам обойти эту проблему без использования
        # global
        sequence += [next_element]


sequence = [1, 1]
continue_fibonacci_sequence(sequence, 1)
print(*sequence)
