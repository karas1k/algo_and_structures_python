"""
5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.
"""
from random import randint

MY_LIST = set([randint(-15, 100) for i in range(15)])
MY_LIST = list(MY_LIST)
print(MY_LIST)
POSITION = 0

for i in MY_LIST:
    if MY_LIST[POSITION] > i:
        POSITION = MY_LIST.index(i)

if MY_LIST[POSITION] < 0:
    print(f"Максимальный отрицательный элемент: {MY_LIST[POSITION]}.",
          f"Позиция {POSITION + 1}")
else:
    print(f"Нет отрицательных элементов")
