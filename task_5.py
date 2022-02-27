# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def multiply(number1, number2):
    return number1 * number2


data = [number for number in range(100, 1001, 2)]

# print(data)
print(reduce(multiply, data))

