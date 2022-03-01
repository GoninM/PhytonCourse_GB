# 1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.


while True:
    input_str = input('Введите строку: ')
    if not input_str:
        break
    else:
        with open('task1_result.txt', 'a') as f_obj:
            f_obj.write(input_str + '\n')


