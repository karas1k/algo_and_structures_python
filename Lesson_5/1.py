"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
from collections import namedtuple


Company = namedtuple(
    'Company', [
        'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'])

ARR_COMPANY = {}

QUANTITY_COMPANY = int(input("Количество предприятий: "))

for i in range(QUANTITY_COMPANY):
    name = input(f"{str(i + 1)}-е предприятие: ")
    ARR_COMPANY[name] = Company(
        quarter_1=int(input("Прибыль за 1-й квартал: ")),
        quarter_2=int(input("Прибыль за 2-й квартал: ")),
        quarter_3=int(input("Прибыль за 3-й квартал: ")),
        quarter_4=int(input("Прибыль за 4-й квартал: "))
    )
print(ARR_COMPANY)

TOTAL_PROFIT = ()

for key, value in ARR_COMPANY.items():
    print(f"Предприятие: {key}, прибыль за год = {sum(value)}")
    TOTAL_PROFIT += value

AVG_PROFIT = round(sum(TOTAL_PROFIT) / len(ARR_COMPANY), 2)
print(f"Средняя прибыль за год для всех предприятий {AVG_PROFIT}")

for key, value in ARR_COMPANY.items():
    if sum(value) > AVG_PROFIT:
        print(
            f"Прибыль предприятия {key} = {sum(value)}, что выше средней прибыли всех предприятий")
    elif sum(value) < AVG_PROFIT:
        print(
            f"Прибыль предприятия {key} = {sum(value)}, что ниже средней прибыли всех предприятий")
    else:
        print(
            f"Прибыль предприятия {key} = {sum(value)}, что равно средней прибыли всех предприятий")
