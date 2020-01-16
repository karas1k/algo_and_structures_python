"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

MY_LIST = [randint(1, 12) for i in range(10)]
# MY_LIST = set([randint(1, 12) for i in range(10)]) # Так оставим уникальные значения и результат программы
# MY_LIST = list(MY_LIST)                            # будет корректнее,
# но список отсортирован будет
print(MY_LIST)

MIN_NUMBER = 0
MAX_NUMBER = 0
STEP = 1
SUM_NUMBERS = 0

for i in MY_LIST:
    if MY_LIST[MAX_NUMBER] < i:
        MAX_NUMBER = MY_LIST.index(i)
    elif MY_LIST[MIN_NUMBER] > i:
        MIN_NUMBER = MY_LIST.index(i)

if MAX_NUMBER - MIN_NUMBER < 0:
    STEP = -1
else:
    SUM_NUMBERS = 0
for i in MY_LIST[MIN_NUMBER + STEP:MAX_NUMBER:STEP]:
    SUM_NUMBERS += i
print(f"Максимальное число: {MY_LIST[MAX_NUMBER]}")
print(f"Минимальное число: {MY_LIST[MIN_NUMBER]}")
print(
    f"Сумма между {MY_LIST[MIN_NUMBER]} и {MY_LIST[MAX_NUMBER]} = {SUM_NUMBERS}")
