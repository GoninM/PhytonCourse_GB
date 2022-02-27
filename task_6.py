# 6. Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее. Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
# #### Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
# # Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from itertools import count
from itertools import cycle

start_number = 5
stop_number = 10

print('part 1:')
for n in count(start_number):
    if n > stop_number:
        break
    else:
        print(n)

print('\n')
print('part 2:')

counter = 0
counter_stop_value = 10

data_list = [True, 'a', 'b', 123]

for el in cycle(data_list):
    if counter > counter_stop_value:
        break

    print(el)
    counter += 1
