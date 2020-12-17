# это зависит от уровня вложенности
# когда value глобальная переменная,
# то нет разницы между value = value + addition и value += addition
# как в данном примере
numbers = [2, 5, 7, 8, 4, 1, 6]
s1, s2 = 0, 0
for number in numbers:
    if number % 2 == 0:
        s1 += 1
    else:
        s2 = s2 + 1
print(s1, s2)


# но в случае когда мы работаем, допустим, с функциями, и нам нужно изменить переменную
# которая не является глобальной и находится в цикле
# в таком случае и появляются отличия между value = value + addition и value += addition


def mirror(arr):
    arr_copy = arr.copy()
    arr_copy.reverse()
    arr += arr_copy


arr = [1, 2]
mirror(arr)
print(*arr)


# += позволяет нам менять исходный список без добавления атрибута global


def mirror(arr):
    arr_copy = arr.copy()
    arr_copy.reverse()
    arr = arr + arr_copy


arr = [1, 2]
mirror(arr)
print(*arr)

# с arr = arr + arr_copy как мы можем видеть такие вещи не работают
