"""
2.	Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""
from random import randint
LIST_ONE = [randint(1, 15) for i in range(10)]
LIST_TWO = [i + 1 for i, j in enumerate(LIST_ONE) if j % 2 == 0]
print(LIST_ONE)
print(LIST_TWO)

# Решение без enumerate
LIST_TWO = [i + 1 for i in range(len(LIST_ONE)) if LIST_ONE[i] % 2 == 0]
print(f"\nРешение без enumerate:\n{LIST_TWO}")
