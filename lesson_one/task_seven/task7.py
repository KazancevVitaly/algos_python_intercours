"""
Определить, является ли год,
который ввел пользователь, високосным или не високосным.
"""
# python --version 3.9.0

# получаем данные от пользователя
year = int(input('Укажите год:\n'))

"""
В решении задачи ориентируемся на григорианский календарь,
по правилам которого года кратные 400 -- високосные, например год 2000 или 1600
года кратные 100, но некратные 400 -- не високосные, например год 1900 или 2100
года не кратные 100 и 400, но кратные 4 -- високосные,
все остальные года -- не високосные
"""

# если год кратен 400, то он високосный
if year % 400 != 0:
    # если год не кратен 400, но кратен 100, то он не високосный
    if year % 100 != 0:
        # если год не кратен 100 и 400, но кратен 4, то он високосный
        if year % 4 != 0:
            print(f'Год {year} -- не високосный.')
        else:
            print(f'Год {year} -- високосный.')
    else:
        print(f'Год {year} -- не високосный.')
else:
    print(f'Год {year} -- високосный.')


# тестирую на разных датах
"""
Укажите год:
2000
Год 2000 -- високосный.

Process finished with exit code 0
__________________________________

Укажите год:
1900
Год 1900 -- не високосный.

Process finished with exit code 0
_________________________________
Укажите год:
1999
Год 1999 -- не високосный.

Process finished with exit code 0
---------------------------------
Укажите год:
1996
Год 1996 -- високосный.

Process finished with exit code 0
"""