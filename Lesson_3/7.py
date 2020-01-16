"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
from random import randint

MY_LIST = [randint(1, 12) for i in range(13)]
print(MY_LIST)
MY_LIST.sort()
print(f"Наименьшие числа: {MY_LIST[0]}, {MY_LIST[1]}")
