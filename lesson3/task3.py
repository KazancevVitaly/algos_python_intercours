"""
Урок 3. Задача 3.
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
# python --version 3.9.0
from random import randint


def min_change_max(lst):
    max_el = lst[0]
    min_el = lst[0]
    """
    Функция принимает в себя список, минимальный и максимальные элементы которго
    нужно поменять местами.  
    """
    for el in lst:
        """
        Сравниваем el со значениямми max_el и min_el.
        Если el больше max_el, то помещаем значение el в переменную max_el,
        ложность данного утверждения не рассматривем, т.к. в  данном случае это излишне.
        Если el меньше min_el, то помещаем значение el в переменную min_el,
        ложность данного утверждения также не рассматривем, т.к. в  данном случае это излишне.
        """
        if el > max_el:
            max_el = el
        if el < min_el:   # В данном случае именно if, ни в коем случае не elif и не else
            min_el = el
    index_max = lst.index(max_el)   # Получаем индекс максимального элемента
    index_min = lst.index(min_el)   # Получаем индекс минимального элемента
    lst[index_max] = min_el    # Максимальный элемент заменяем минимальным
    lst[index_min] = max_el    # Минимальный элемент заменяем максимальным
    print(f'Максимальный элемент в списке -- {max_el}\n'
          f'Минимальный  элемент в списке -- {min_el}\n'
          f'Новый список:\n{lst}')


arr = [randint(1,101) for i in range(0,10)]
print(f'Исходный список:\n{arr}')
min_change_max(arr)


# Результат запуска программы
"""
Исходный список:
[89, 36, 25, 68, 97, 87, 75, 2, 90, 14]
Максимальный элемент в списке -- 97
Минимальный  элемент в списке -- 2
Новый список:
[89, 36, 25, 68, 2, 87, 75, 97, 90, 14]

Process finished with exit code 0
"""