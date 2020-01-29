"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.

x64 WIN 10
Python 3.8.0
Lesson_3_9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import math
import memory_profiler


@memory_profiler.profile
def sieve_without_eratosthenes(i):
    """
    Функция поиска i-го простого числа,
    без использования алгоритма Решето Эратосфена
    """

    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]


def prime_counting_function(i):
    """
    Функция возвращает верхнюю границу отрезка на котором лежат
    i-e количество простых чисел. Количество простых чисел на отрезке
    [1;n] растёт с увеличением n как n / ln(n).
    """

    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


@memory_profiler.profile
def eratosthen_search_number(i):
    """
    Функция поиска i-го простого числа,
    используя алгоритм Решето Эратосфена
    """
    i_max = prime_counting_function(i)
    lst_prime = [i for i in range(2, i_max)]
    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[i - 1]


USER_NUMBER = int(input('Введите номер по счету простого числа: '))
# print(sieve_without_eratosthenes(USER_NUMBER))

print('Алгоритм 1 без использования алгоритма Решето Эратосфена')
print(
    f'{sieve_without_eratosthenes(USER_NUMBER)} - {USER_NUMBER}-ое \
по счёту простое число. Алгоритм без решета занимает {memory_profiler.memory_usage()[0]} Мб.'
)

print('Алгоритм 2 с использованием алгоритма Решето Эратосфена')
print(
    f'{eratosthen_search_number(USER_NUMBER)} - {USER_NUMBER}-ое по счёту простое число.\
    Алгоритм с решетом занимает {memory_profiler.memory_usage()[0]} Мб.')

'''
Поиск 100-го простого числа показал следующие результыта:
Без использования Решета Эратосфена: Mem usage = 13.1 MiB, Increment = 0 MiB, 13.1171875 Мб.
С использованием Решета Эратосфена: Mem usage = 13.2 MiB, Increment = 0.2 MiB, 13.1953125 Мб.
Поиск 1000-го простого числа показал следующие результыта:
Без использования Решета Эратосфена: Mem usage = 13.2 MiB, Increment = 0 MiB, 13.265625 Мб.
С использованием Решета Эратосфена: Mem usage = 13.3 MiB, Increment = 0.2 MiB, 13.4359375 Мб.
Отсюда следует, что алгоритм Решето Эратосфена потребляет больше памяти чем больше массив.
'''
