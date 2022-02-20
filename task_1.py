# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(dividend, divider):
    if divider == 0:
        return 'Ошибка! деление на 0'
    else:
        return dividend/divider


number_1 = int(input('Введите делимое: '))
number_2 = int(input('Введите делитель: '))

print(division(number_1, number_2))
