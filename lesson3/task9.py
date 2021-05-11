"""
Урок 3. Задача 9.
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
# python --version 3.9.0
from random import randint


def matrix_method(mtrx):
    min_elms_matrix = []
    max_el = -1
    for i in range(len(mtrx[0])):
        min_el = 0
        j = 1
        for el in mtrx:
            if j == 1:
                min_el = el[i]
                j += 1
            elif el[i] < min_el:
                min_el = el[i]
        min_elms_matrix.append(min_el)
        if min_el > max_el:
            max_el = min_el
    return f'Список минимальных элемнтов столбцов матрицы:\n{min_elms_matrix}\n' \
           f'\nМаксимальное число среди этих элементов равно {max_el}'


matrix = [[randint(1, 99) for _ in range(10)] for _ in range(5)]
"""
выведем матрицу на экран
"""
for line in matrix:
    for i in line:
        print(f'{i:>4}', end='')
    print()

print()
print(matrix_method(matrix))


# результат запуска программы
"""
  87  12  39  37  70  70  13  93  97  22
  50  87  78  67  22  42   4  63  28  58
   1  72   2  88   3  53   6  74  88  99
  54   9  11  41  52  61  93  83  17  31
  94  55  67  10  46  51  73  10  82  79

Список минимальных элемнтов столбцов матрицы:
[1, 9, 2, 10, 3, 42, 4, 10, 17, 22]

Максимальное число среди этих элементов равно 42

Process finished with exit code 0
"""