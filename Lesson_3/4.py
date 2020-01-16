"""
4.	Определить, какое число в массиве встречается чаще всего.
"""
from random import random

MY_LIST = [int(random() * 10) for i in range(10)]
print(MY_LIST)

MAX_NUMBER = 0
COUNTER = 0

for element in set(MY_LIST):
    count_element = MY_LIST.count(element)
    if count_element > COUNTER:
        COUNTER = count_element
        MAX_NUMBER = element

print(f"Чаще всего встречается число {MAX_NUMBER} - {COUNTER} раз(а)")
