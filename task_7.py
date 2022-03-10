# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        result = ''
        if self.re == 0 and self.im == 0:
            result = f'0'
        elif self.re == 0:
            result = f'{str(self.im)}*i'
        elif self.im == 0:
            result = f'{str(self.re)}'
        else:
            if self.im > 0:
                sign = '+'
            else:
                sign = '-'

            result = f'{str(self.re)} {sign} {str(abs(self.im))}*i'

        return result

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)


c_number_1 = ComplexNumber(-2, 1)
c_number_2 = ComplexNumber(2, -1)


print(f'{c_number_1}')
print(f'{c_number_2}')

print(f'({c_number_1}) + ({c_number_2}) = {c_number_1 + c_number_2}')
print(f'({c_number_1}) * ({c_number_2}) = {c_number_1 * c_number_2}')
