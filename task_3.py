# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = int(input('Введите число n:'))

degree = 0
n_copy = n

while n_copy > 0:
    n_copy //= 10
    degree += 1

nn = (10 ** degree) * n + n
nnn = nn + (100 ** degree) * n
result = n + nn + nnn

print(f'{n} + {nn} + {nnn} = {result}')
