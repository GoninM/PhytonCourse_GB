# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

# 7. Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

def int_func(text):
    return text.capitalize()

# print('check empty string')
# test_string = ''
# print(f'in: "{test_string}"')
# print(f'out: "{int_func(test_string)}"')
#
# print('check string 1 letter')
# test_string = 'a'
# print(f'in: "{test_string}"')
# print(f'out: "{int_func(test_string)}"')
#
# print('check string from spaces')
# test_string = '       '
# print(f'in: "{test_string}"')
# print(f'out: "{int_func(test_string)}"')
#
# print('check string first space')
# test_string = ' bbbb'
# print(f'in: "{test_string}"')
# print(f'out: "{int_func(test_string)}"')
#
# print('check string')
# test_string = 'asdf'
# print(f'in: "{test_string}"')
# print(f'out: "{int_func(test_string)}"')


test_string = input('Введите строку: ')
result = ''

for w in test_string.split():
    result += f'{int_func(w)} '

print(result)

