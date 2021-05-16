"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
# python --version 3.9.0
from collections import deque, namedtuple


def hexadecimal():
    nums1 = deque(input('Введите шестнадцатеричное число, '
                        '(шестнадцатеричное число состоит из цифр от 0 до 9 и букв A, B, C, D, E, F):\n').upper())
    nums2 = deque(input('Введите второе шестнадцатеричное число, '
                        '(шестнадцатеричное число состоит из цифр от 0 до 9 и букв A, B, C, D, E, F):\n').upper())
    """
    Пользователь вводит первое и второе число
    """
    o = '0x'
    nums1.appendleft(o)
    nums2.appendleft(o)
    try:
        ten_nums1 = int(''.join(nums1), 16)
        ten_nums2 = int(''.join(nums2), 16)
    except ValueError:
        return 'шестнадцатеричное число может содержать только цифры от 0 до 9 и буквы A, B, C, D, E, F'
    nums1.popleft()
    nums2.popleft()
    sum_result = hex(ten_nums1 + ten_nums2).upper()
    m_result = hex(ten_nums1 * ten_nums2).upper()
    return f'Первое шестнадцатеричное число: {list(nums1)}\n' \
           f'Второе шестнадцатеричное число: {list(nums2)}\n' \
           f'Сумма чисел равна: {list(deque(sum_result[2:]))}\n' \
           f'Произведение чисел: {list(deque(m_result[2:]))}'


ex = ''
while ex == '':
    print(hexadecimal())
    ex = input('Для продолжения нажмите клавишу Enter,'
               'для завершения любую другую клавишу+Enter:\n')


# вариант без hex() и int()
class HexAddMul(object):
    def __init__(self, num):
        """
        Магичиский метод инит, принимает в себя число num
        в шестнадцатиричном формате,
        переводим num в десятичный формат методом to_10.
        Также здесь инициализируем именованный кортеж
        """
        Hl = namedtuple('Hl', 'A B C D E F')
        self.hex_letters = Hl(A=10, B=11, C=12, D=13, E=14, F=15)
        self.num = self.to_10(num)

    def __add__(self, other):
        """
        переопределяем сложение
        """
        return self.to_hex(self.num + other.num)

    def __mul__(self, other):
        """
        переопределяем умножение
        """
        return self.to_hex(self.num * other.num)

    def to_10(self, num):
        """
        :param num: число в шестнадцатиричном формате
        :return: возвращаем переведенное в десятиричную систему число
        """
        dec = 0
        for i in num:
            if i in self.hex_letters._fields:
                v = self.hex_letters.__getattribute__(i)
            else:
                v = int(i)
            dec += v * (16 ** abs(len(num) - 1 - num.index(i)))
        return dec

    def to_hex(self, num):
        """
        :param num: на вход число в дусятеричной системе счисления
        :return: на выход списко из символов шестнадцатеричного числа
        """
        if num < 16:
            return [str(num)]
        else:
            r = deque()
            while num > 15:
                d = num % 16
                r.appendleft(str(d) if d < 10 else self.hex_letters._fields[d - 10])
                num = num // 16
            r.appendleft(str(num) if num < 10 else self.hex_letters._fields[num - 10])
            return list(r)


a = input("Введите перове число в шестнадцатиричном формате: ").upper()
b = input("Введите второе число в шестнадцатиричном формате: ").upper()

hc_a = HexAddMul(a)
hc_b = HexAddMul(b)

print(f"Сумма:          {hc_a + hc_b}")
print(f"Произведение:   {hc_a * hc_b}")

# результат
"""
Введите перове число в шестнадцатиричном формате: a2
Введите второе число в шестнадцатиричном формате: c4f
Сумма:          ['C', 'F', '1']
Произведение:   ['7', 'C', '9', 'F', 'E']

Process finished with exit code 
"""