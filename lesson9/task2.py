"""
Закодируйте любую строку по алгоритму Хаффмана.
"""
import heapq
from collections import Counter, namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    def way(self, code, a):
        self.left.way(code, a + '0')
        self.right.way(code, a + '1')
    """
    Задаем структуру для нашего дерева
    """


class Leaf(namedtuple('Leaf', ['char'])):
    def way(self, code, a):
        code[self.char] = a or '0'
    """
    Листья без потомков но со значением символа
    """


# функция для кодирования символов в коды Хаффмана
def huffman_coder(str_obj):
    h = []
    for i, j in Counter(str_obj).items():
        h.append((j, len(h), Leaf(i)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        j1, count1, left = heapq.heappop(h)
        j2, count2, right = heapq.heappop(h)
        heapq.heappush(h, (j1 + j2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(freq, count, root)] = h
        root.way(code, '')
    return code


# функция для принятия строки, которую будем кодировать.
def huffman_clench():
    s = input('Строка для сжатия алгоритмом Хаффмана:\n')
    str_cod = huffman_coder(s)
    for i in s:
        print(str_cod[i], end=' ')
    return


huffman_clench()

"""
Результат:
Строка для сжатия алгоритмом Хаффмана:
Алгоритмы и структуры данных на Python.
00010 00011 00100 00101 1011 11110 1100 00110 1101 100 11110 100 00111 1100 1011 11111 01000 1100 11111 1011 1101 100 01001 0000 1110 1110 1101 01010 100 1110 0000 100 01011 01100 01101 01110 01111 10100 10101 
Process finished with exit code 0
"""