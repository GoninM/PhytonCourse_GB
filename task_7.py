# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

firms = []

with open('task7_in.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        firms.append(line.split())

# print(firms)

result_firms = {}

for firm in firms:
    result_firms[firm[0]] = float(firm[2]) - float(firm[3])

# print(result_firms)

average_profit = 0
count = 0

for firm in result_firms:
    if result_firms[firm] > 0:
        average_profit += result_firms[firm]
        count += 1
    else:
        continue

average_profit /= count
result_list = [result_firms, {'average_profit': average_profit}]
print(result_list)

with open("task7_out.json", "w") as write_f:
    json.dump(result_list, write_f)
