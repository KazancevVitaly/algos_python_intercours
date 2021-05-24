"""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.
"""
# python --version 3.9.0
import hashlib


def substring(string):
    substring_set = set()
    for i in range(len(string)):
        for j in range(len(string)-1 if i == 0 else len(string), i, -1):
            # print(string[i], string[j])
            # print(string[i:j])
            substring_set.add(hashlib.sha256(bytes(string[i:j], 'cp1251')).hexdigest())
    return substring_set


# строка filder
# строка filfil
amount_substing = len(substring(input('Введите строку:\n')))
print(f'Количество различных подстрок в строке: {amount_substing}')