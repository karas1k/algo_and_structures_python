"""
3.	В массиве случайных целых чисел поменять местами минимальный
и максимальный элементы.

"""
from random import randint
MY_LIST = set([randint(1, 15) for i in range(15)])
MY_LIST = list(MY_LIST)
print(MY_LIST)
MAX_NUMBER = MY_LIST[0]
MIN_NUMBER = MY_LIST[0]

for i in MY_LIST:
    if i > MAX_NUMBER:
        MAX_NUMBER = i
    elif i < MIN_NUMBER:
        MIN_NUMBER = i
MIN_INDEX = MY_LIST.index(MIN_NUMBER)
MAX_INDEX = MY_LIST.index(MAX_NUMBER)
MY_LIST[MIN_INDEX], MY_LIST[MAX_INDEX] = MY_LIST[MAX_INDEX], MY_LIST[MIN_INDEX]
print(f'Меняем местами элементы {MIN_INDEX + 1} и {MAX_INDEX + 1}:\n{MY_LIST}')
