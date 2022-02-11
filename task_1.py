# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные,
# затем выведите на экран.

number = 234
float_number = 55.435345252
test_string = 'hello world!'
test_bool = True
test_list = [45, 45, 6, 78, 4]

print(test_list)
print(type(test_list))


print(number)
print(f'int {number:05}')
print(type(number))

print(float_number)
print(f'float {float_number:.3f}')
print(type(float_number))

print(test_string)
print(type(test_string))

print(test_bool)
print(type(test_bool))



input_number = int(input('введите число:'))
print(f'вы ввели {input_number}')
print(type(input_number))

input_str = input('Введите строку:')
print(f'вы ввели {input_str}')
print(type(input_str))



