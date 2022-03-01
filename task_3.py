# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

employees = []

with open('task3_in.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        employees.append(line.split())

# не делаю проверку на пустые строки или неправильного формата файла
avg_salary = 0
employees_under_20 = []

for emp in employees:
    avg_salary += float(emp[1])
    if float(emp[1]) < 20000:
        employees_under_20.append(emp[0])

avg_salary /= len(employees)

print(f'Средняя величина дохода = {avg_salary:.02f}')
print('Сотрудники с доходом меньше 20000.00')
for emp in employees_under_20:
    print(emp)
