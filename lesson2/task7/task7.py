"""
Написать программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""
# python --version 3.9.0


# через рекурсию находим сумму
def sumn(n, s=0):
    if n == 0:
        return s
    else:
        s += n
        return sumn(n - 1, s)


# проверяем утверждение
def check(n):
    if sumn(n) == n * (n + 1) / 2:
        return True
    else:
        return False


num = int(input('Введите число n:\n'))
print(check(num))

# запускаем код
"""
Введите число n:
45
True

Process finished with exit code 0
"""