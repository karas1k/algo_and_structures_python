"""
1.	В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""


def get_number():
    """Получаем кратные числа"""
    result = [i for i in RANGE_NUMBERS if i % DIVIDER == 0]
    return result


STEP_NUMBER = 0
DIVIDER = 2
RANGE_NUMBERS = range(2, 100)

while STEP_NUMBER < len(range(2, 10)):
    print(
        f"Для числа {DIVIDER} кратны {len(get_number())} чисел: {get_number()}")
    STEP_NUMBER += 1
    DIVIDER += 1
