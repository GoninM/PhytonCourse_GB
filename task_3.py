# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(number1, number2, number3):
    return number1 + number2 + number3 - min(number1, number2, number3)


print(my_func(1, 3, 5))
print(my_func(100, 3, 5))
print(my_func(0, 1, 1))
print(my_func(1, 1, 1))
print(my_func(0, 0, 5))
