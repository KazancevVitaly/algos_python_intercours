"""
Урок 3. Задача 7.
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""
# python --version 3.9.0
from random import randint


def two_min(arr):
    min_el_1 = 0
    min_el_2 = 0
    j = 1
    for el in arr:
        if j == 1:
            min_el_1 = el
            min_el_2 = el
            j += 1
        elif el < min_el_1:
            min_el_1 = el
    arr.remove(min_el_1)
    """
    Находим первый минимальный элемент и удаляем его из списка,
    затем еще один цикл для поиска второго минимального элемента.
    """
    for el in arr:
        if (el < min_el_2) and (el >= min_el_1):
            min_el_2 = el
    return f'Первый наименьший элемент: {min_el_1}\n' \
           f'Второй наименьший элемент: {min_el_2}'


lst = [randint(1, 100) for _ in range(0, 20)]
print(f'Исходный список:\n{lst}\n')
print(two_min(lst))


# результат запуска программы
"""
Исходный список:
[58, 81, 72, 54, 50, 93, 69, 40, 63, 7, 61, 82, 62, 87, 5, 83, 74, 27, 51, 95]

Первый наименьший элемент: 5
Второй наименьший элемент: 7

Process finished with exit code 0
"""