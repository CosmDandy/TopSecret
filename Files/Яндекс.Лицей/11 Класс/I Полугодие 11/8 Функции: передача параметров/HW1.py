# код создан для распределения чисел в две группы по признаку четности
numbers = [2, 5, 7, 7, 8, 4, 1, 6]
# odd = even = [] было
odd, even = list(), list()
# заменил на odd, even = list(), list()
# odd = even означает что odd = even и на протяжении всего цикла for это условие сохраняется
# поэтому списки становятся равными
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
