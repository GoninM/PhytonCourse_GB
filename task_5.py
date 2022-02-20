# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def sum_elements(list_to_sum):
    result = 0
    for n in list_to_sum:
        try:
            result += int(n)
        except ValueError:
            print(f'{n} не является числом')

    return result


special_symbol = '#'
result_sum = 0
numbers = []
is_break = False

while not is_break:
    numbers = input('введите числа для суммирования через пробел: ').split()

    if numbers[-1] == special_symbol:
        is_break = True
        result_sum += sum_elements(numbers[:-1])
    else:
        result_sum += sum_elements(numbers[:])

    print(result_sum)

