"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

from random import uniform
from timeit import timeit


def merge_sort(numbers_list):
    """Сортировка слияением"""
    if len(numbers_list) > 1:
        center = len(numbers_list) // 2
        left = numbers_list[:center]
        right = numbers_list[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers_list[k] = left[i]
                i += 1
            else:
                numbers_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            numbers_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers_list[k] = right[j]
            j += 1
            k += 1
    return numbers_list


# замеры 10
NUMBERS_LIST = [round(uniform(0, 50), 2) for i in range(10)]
print(f"Исходный массив 10:\n{NUMBERS_LIST}\n")
print(f"Отсортированный массив 10:\n{merge_sort(NUMBERS_LIST)}\n")
TIME = timeit(
    "merge_sort(NUMBERS_LIST)",
    setup="from __main__ import merge_sort, NUMBERS_LIST",
    number=1000)
print(f'Время: {TIME}')

# замеры 100
NUMBERS_LIST = [round(uniform(0, 50), 2) for i in range(100)]
print(f"Исходный массив 100:\n{NUMBERS_LIST}\n")
print(f"Отсортированный массив 100:\n{merge_sort(NUMBERS_LIST)}\n")
TIME = timeit(
    "merge_sort(NUMBERS_LIST)",
    setup="from __main__ import merge_sort, NUMBERS_LIST",
    number=1000)
print(f'Время: {TIME}')

# замеры 1000
NUMBERS_LIST = [round(uniform(0, 50), 2) for i in range(1000)]
print(f"Исходный массив 1000:\n{NUMBERS_LIST}\n")
print(f"Отсортированный массив 1000:\n{merge_sort(NUMBERS_LIST)}\n")
TIME = timeit(
    "merge_sort(NUMBERS_LIST)",
    setup="from __main__ import merge_sort, NUMBERS_LIST",
    number=1000)
print(f'Время: {TIME}')
