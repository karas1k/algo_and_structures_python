"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

column = 5
row = 4
matrix = [[] for i in range(row)]
# print(matrix)
for r in range(row):
    LAST_COLUMN_SUM = 0
    for c in range(column - 1):
        user_number = int(input(f'Введите цифру {r + 1}-ой строки, {c + 1}-го столбца: '))
        LAST_COLUMN_SUM += user_number
        matrix[r].append(user_number)
    matrix[r].append(LAST_COLUMN_SUM)

for element in matrix:
    print(("{:<4d}" * column).format(* element))