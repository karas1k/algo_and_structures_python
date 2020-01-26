"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections
import functools
from collections import deque
NUMS = collections.defaultdict(list)
for i in range(2):
    n = input(f"Введите {i + 1}-е натуральное шестнадцатиричное число: ")
    NUMS[i + 1] = list(n)
print(NUMS)

SUM_NUMBERS = sum([int("".join(i), 16) for i in NUMS.values()])
print(f"Сумма: {SUM_NUMBERS:X}")
MULT_NUMBERS = functools.reduce(lambda a, b: a *
                                b, [int("".join(i), 16) for i in NUMS.values()])
print(f"Произведение: {MULT_NUMBERS:X}")

# deque
FIRST_NUMBER = deque(input("Введите 1-ое число: "))
SECOND_NUMBER = deque(input("Введите 2-ое число: "))


def get_sum(argument_one, argument_two):
    """Сумма"""
    first_number = "".join([i for i in argument_one])
    second_number = "".join([i for i in argument_two])
    result = hex((int(
        float.fromhex(first_number) +
        float.fromhex(second_number))))
    result = deque(result[2::].upper())
    print(f"Сумма: {result}")


def get_mult(argument_one, argument_two):
    """Произведение"""
    first_number = "".join([i for i in argument_one])
    second_number = "".join([i for i in argument_two])
    result = hex(
        (int(
            float.fromhex(first_number) *
            float.fromhex(second_number))))
    result = deque(result[2::].upper())
    print(f"Произведение: {result}")


get_sum(FIRST_NUMBER, SECOND_NUMBER)
get_mult(FIRST_NUMBER, SECOND_NUMBER)

# OOP


class HexOperation:
    """Класс вычисления шестнадцатиричных чисел"""

    def __init__(self, num_first, num_second):
        """Main function"""
        self.num_first = num_first
        self.num_second = num_second

    def __add__(self, other):
        """Перегрузка сумма"""
        return list(hex(int("".join(self.num_first), 16) +
                        int("".join(other.num_second), 16)))[2:]

    def __mul__(self, other):
        """Перегрузка произведение"""
        return list(hex(int("".join(self.num_first), 16) *
                        int("".join(other.num_second), 16)))[2:]


HEX_NUM_FIRST = list(input("Введите 1-ое шестнадцатиричное число: "))
HEX_NUM_SECOND = list(input("Введите 2-ое шестнадцатиричное число: "))

RES_SUM = HexOperation(HEX_NUM_FIRST, HEX_NUM_SECOND) + \
    HexOperation(HEX_NUM_FIRST, HEX_NUM_SECOND)
RES_MUL = HexOperation(HEX_NUM_FIRST, HEX_NUM_SECOND) * \
    HexOperation(HEX_NUM_FIRST, HEX_NUM_SECOND)
print(
    f"Сумма: {[i.upper() for i in RES_SUM]}\nПроизведение: {[i.upper() for i in RES_MUL]}")
