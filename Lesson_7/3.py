"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

from statistics import median
from random import randint, choice


def quick_sort(my_list):
    """Алгоритм быстрой сортировки"""
    if len(my_list) <= 1:
        return my_list
    else:
        start_number = choice(my_list)
        left_array = []
        median_array = []
        rigth_array = []
        for elem in my_list:
            if elem < start_number:
                left_array.append(elem)
            elif elem > start_number:
                rigth_array.append(elem)
            else:
                median_array.append(elem)
        return quick_sort(left_array) + median_array + quick_sort(rigth_array)


LEN_LIST = int(input("Введите размер массива (2m + 1): "))
MY_LIST = [randint(-100, 100) for i in range(LEN_LIST * 2 + 1)]
print(f"Сформированный спиок:\n{MY_LIST}")
print(f"\nОтсортированный список для наглядности:\n{quick_sort(MY_LIST)}")
MEDIAN = len(quick_sort(MY_LIST)) // 2
print(f"\nМедианна: {quick_sort(MY_LIST)[MEDIAN]}\n\n{'*' * 40}")

# Проверка
print(f"\nПроверка:\nМедиана: {median(MY_LIST)}")
