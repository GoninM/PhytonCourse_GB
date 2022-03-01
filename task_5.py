# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import random


digits_number = 10
min_number = 1
max_number = 100

with open('task5_out.txt', 'w') as f_obg:
    while digits_number > 0:
        f_obg.write(str(random.randint(min_number, max_number)) + ' ')
        digits_number -= 1

digits = []
with open('task5_out.txt', 'r') as f_obg:
    for d in f_obg.read().split():
        digits.append(int(d))

result_str = ''
summa = sum(digits)

for d in digits[:-1]:
    result_str += str(d)
    result_str += ' + '

result_str += str(digits[-1]) + ' = ' + str(summa)

print(result_str)
