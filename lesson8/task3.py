"""
Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
 по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""
from random import randint

n = input('Укажите число вершин:\n')  # число вершин в графе
try:
    n = int(n)
except ValueError:
    print('Неверное значение')


def gen_graph(nodes):    # генерируем граф
    graph = {}
    for i in range(nodes):
        graph[i] = [j for j in range(randint(1, nodes)) if j != i]
    return graph


gr = gen_graph(n)
visited = set()


def dfs(node):
    """
    :param node: на вход номер вершины с которой начинаем обход
    :return:
    """
    if node in visited:   # базовый случай, если вершина уже проверялась
        return
    visited.add(node)     # помечаем вершину как проверенную
    for el in gr[node]:
        if el not in visited:
            dfs(el)       # если элемент не проверялся добавляем его в множество visited


start = 0
dfs(start)
print(gr)
print(f'Из вершины {start} можно добраться до вершин {visited}')

# результат запуска программы
"""
Укажите число вершин:
10
{0: [1, 2], 1: [2], 2: [1, 3, 4], 3: [1, 2, 4, 5, 6, 7], 4: [1, 2, 3, 5, 6, 7, 8], 5: [1, 2], 6: [1, 2], 7: [1], 8: [1, 2, 3], 9: [1, 2]}
Из вершины 0 можно добраться до вершин {0, 1, 2, 3, 4, 5, 6, 7, 8}

Process finished with exit code 0
"""