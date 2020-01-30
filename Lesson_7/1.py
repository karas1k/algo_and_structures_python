"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
from random import randint
import timeit


def smart_bubble(numbers_list):
    """bubble_sort_optimization"""
    for i in range(len(numbers_list) - 1, 0, -1):
        flag = True
        for j in range(i):
            if numbers_list[j] < numbers_list[j + 1]:
                numbers_list[j], numbers_list[j + \
                    1] = numbers_list[j + 1], numbers_list[j]
                flag = False
        if flag:
            break
    return numbers_list


def no_smart_bubble(numbers_list):
    """bubble_sort_NOT_optimization"""
    for i in range(len(numbers_list) - 1, 0, -1):
        for j in range(i):
            if numbers_list[j] < numbers_list[j + 1]:
                numbers_list[j], numbers_list[j +
                                              1] = numbers_list[j + 1], numbers_list[j]

    return numbers_list


def standart_sort_func(numbers_list):
    """Стандартная функция сортировки"""
    numbers_list.sort(reverse=True)
    return numbers_list

# Замеры 10
NUMBERS_LIST = [randint(-100, 100) for i in range(10)]
print(NUMBERS_LIST)
print(smart_bubble(NUMBERS_LIST))

TIME_SMART_BUBBLE = timeit.timeit(
    "smart_bubble(NUMBERS_LIST)",
    setup="from __main__ import smart_bubble, NUMBERS_LIST",
    number=1000)

TIME_NOT_SMART_BUBBLE = timeit.timeit(
    "no_smart_bubble(NUMBERS_LIST)",
    setup="from __main__ import no_smart_bubble, NUMBERS_LIST",
    number=1000)

TIME_SORTED_FUNC = timeit.timeit(
    "standart_sort_func(NUMBERS_LIST)",
    setup="from __main__ import standart_sort_func, NUMBERS_LIST",
    number=1000)

print(f'Время на сортировку "умным пузырьком": {TIME_SMART_BUBBLE}')
print(
    f'Время на сортировку НЕ "умным пузырьком": {TIME_NOT_SMART_BUBBLE}')
print(
    f'Время на сортировку функцией sort(): {TIME_SORTED_FUNC}\n{"*" * 70}\n')

# Замеры 100

NUMBERS_LIST = [randint(-100, 100) for i in range(100)]
print(NUMBERS_LIST)
print(smart_bubble(NUMBERS_LIST))

TIME_SMART_BUBBLE = timeit.timeit(
    "smart_bubble(NUMBERS_LIST)",
    setup="from __main__ import smart_bubble, NUMBERS_LIST",
    number=1000)

TIME_NOT_SMART_BUBBLE = timeit.timeit(
    "no_smart_bubble(NUMBERS_LIST)",
    setup="from __main__ import no_smart_bubble, NUMBERS_LIST",
    number=1000)

TIME_SORTED_FUNC = timeit.timeit(
    "standart_sort_func(NUMBERS_LIST)",
    setup="from __main__ import standart_sort_func, NUMBERS_LIST",
    number=1000)

print(f'Время на сортировку "умным пузырьком": {TIME_SMART_BUBBLE}')
print(
    f'Время на сортировку НЕ "умным пузырьком": {TIME_NOT_SMART_BUBBLE}')
print(
    f'Время на сортировку функцией sort(): {TIME_SORTED_FUNC}\n{"*" * 70}\n')

# Замеры 1000

NUMBERS_LIST = [randint(-100, 100) for i in range(1000)]
print(NUMBERS_LIST)
print(smart_bubble(NUMBERS_LIST))

TIME_SMART_BUBBLE = timeit.timeit(
    "smart_bubble(NUMBERS_LIST)",
    setup="from __main__ import smart_bubble, NUMBERS_LIST",
    number=1000)

TIME_NOT_SMART_BUBBLE = timeit.timeit(
    "no_smart_bubble(NUMBERS_LIST)",
    setup="from __main__ import no_smart_bubble, NUMBERS_LIST",
    number=1000)

TIME_SORTED_FUNC = timeit.timeit(
    "standart_sort_func(NUMBERS_LIST)",
    setup="from __main__ import standart_sort_func, NUMBERS_LIST",
    number=1000)

print(f'Время на сортировку "умным пузырьком": {TIME_SMART_BUBBLE}')
print(
    f'Время на сортировку НЕ "умным пузырьком": {TIME_NOT_SMART_BUBBLE}')
print(
    f'Время на сортировку функцией sort(): {TIME_SORTED_FUNC}\n{"*" * 70}\n')

"""
Замеры 10:
    Время на сортировку "умным пузырьком": 0.0024717999999999997
    Время на сортировку НЕ "умным пузырьком": 0.011228600000000002
    Время на сортировку функцией sort(): 0.00035389999999999727
Замеры 100:
    Время на сортировку "умным пузырьком": 0.016413999999999998
    Время на сортировку НЕ "умным пузырьком": 0.8214319
    Время на сортировку функцией sort(): 0.0010989999999999611
Замеры 1000:
    Время на сортировку "умным пузырьком": 0.18817909999999993
    Время на сортировку НЕ "умным пузырьком": 87.9788297
    Время на сортировку функцией sort(): 0.008549799999997276
"""
