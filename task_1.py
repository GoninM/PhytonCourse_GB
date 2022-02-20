# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(dividend, divider):
    try:
        return dividend/divider
    except ZeroDivisionError:
        return 'Ошибка! Деление на ноль!'

number_1 = int(input('Введите делимое: '))
number_2 = int(input('Введите делитель: '))

print(division(number_1, number_2))
