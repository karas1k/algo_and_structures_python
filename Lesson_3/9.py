"""
9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random

COLUMNS = 5
ROWS = 5
MATRIX = []
for i in range(COLUMNS):
    MATRIX.append([])
    MATRIX[i].extend([random.randint(0, 99) for i in range(ROWS)])

MIN_LIST = []
MIN_LIST.extend(MATRIX[0])

for string in MATRIX:
    print(("{:3d} " * len(string)).format(* string))
    i = 0
    for j in string:
        if j < MIN_LIST[i]:
            MIN_LIST[i] = j
        i += 1

print("\nМинимальные элементы столбцов матрицы")
print(MIN_LIST)
print("\nМаксимальный элемент среди минимальных элементов столбцов матрицы: ",
      sorted(MIN_LIST, reverse=True)[0]
      )
