"""
Урок 8. Задача1.
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""
# python --version 3.9.0

"""
На диаграме хорошо видно(диаграма прилагается), что количество рукопожатй - это количество ребер.
Поэтому логично будет создать программно граф ввиде списка ребер с количеством вершин, которое укажет пользователь.
Проверим результат формулой n * (n -1) / 2.
"""


def lemma_handshake(n):
    """
    :param n: на вход количество друзей
    :return: возвращаем count_handshake - количество рукопожатий
    """
    handshake_graph = []
    for i in range(n):
        """
        В первом цикле берем i-ю вершину
        """
        for j in range(i + 1, n):
            """
            Во втором цикле i-ю вершину соединяем ребрами с другими вершинами.
            Вершины взятые на предыдущих итерациях не трогаем.
            В конце цикла получаем граф представленный списком ребер.
            """
            handshake = (i, j)
            handshake_graph.append(handshake)
    count_handshake = len(handshake_graph)
    # print(handshake_graph)
    return f'Количество рукопожатий которой совершили {n} друзей(друга) равно {count_handshake}'


try:
    amount_friend = abs(int(input('Введите количество друзей:\n')))
    print(lemma_handshake(amount_friend))
    # проверка
    check = int(amount_friend * (amount_friend - 1) / 2)
    print(f'{"*" * 50}\nКоличество рукопожатий по формуле n * (n - 1) / 2 для проверки:\n{check}')
except ValueError:
    print('Нужно указать количество друзей числовым значением')


# результат работы программы
"""
Введите количество друзей:
7
Количество рукопожатий которой совершили 7 друзей(друга) равно 21
**************************************************
Количество рукопожатий по формуле n * (n - 1) / 2 для проверки:
21

Process finished with exit code 0
"""