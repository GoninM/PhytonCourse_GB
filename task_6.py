# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

revenue = int(input("Введите значение выручки:"))
costs = int(input("Введите значение издержек:"))

if revenue > costs:
    print('Прибыль')
    profitability = (revenue - costs) / revenue

    number_of_staff = int(input('введите численность персонала :'))

    profitability_per_person = profitability / number_of_staff

    print(profitability_per_person)
elif revenue < costs:
    print('Убыток')
else:
    print('выручка равна издержкам')
