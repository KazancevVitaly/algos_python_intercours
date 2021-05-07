"""
Урок1. Задача4.
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят,
и сколько между ними находится букв.
"""
# python --version 3.9.0

# пользователь вводит первую букву
letter_one = input('Введиете первую букву:\n')
letter_one = letter_one.lower()

# пользователь вводит вторую букву
letter_two = input('Введите вторую букву:\n')
letter_two = letter_two.lower()

# Определяем на каком месте в алфавите находятся буквы
position_one = ord(letter_one) - ord('a') + 1
position_two = ord(letter_two) - ord('a') + 1

# Определяем сколько букв между указанными пользователем буквами
amount_letter_between = abs(position_one - position_two) - 1

# Выводим результаты вычислений
print(f'Буква {letter_one} занимает в алфавите позцию номер {position_one}\n'
      f'Буква {letter_two} занимает в алфавите позицию номер {position_two}\n'
      f'Количество букв между {letter_one} и {letter_two} равно {amount_letter_between}.')

# результат работы программы
"""
Введиете первую букву:
k
Введите вторую букву:
c
Буква k занимает в алфавите позцию номер 11
Буква c занимает в алфавите позицию номер 3
Количество букв между k и c равно 7.

Process finished with exit code 0
"""