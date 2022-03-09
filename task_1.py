# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, data):
        self.matrix = data

    def __str__(self):
        result = ''
        for row in self.matrix:
            for element in row:
                if row.index(element) != len(row) - 1:
                    result += f'{element} '
                else:
                    result += f'{element}'
            if self.matrix.index(row) != len(self.matrix) - 1:
                result += '\n'
        return result

    def __add__(self, other):
        result = []

        try:
            for i in range(len(self.matrix)):
                result.append([])
                for j in range(len(self.matrix[i])):
                    result[i].append(self.matrix[i][j] + other.matrix[i][j])
            return Matrix(result)

        except IndexError:
            return 'матрицы разного размера, сложение невозможно!'


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print('Матрица а = ')
print(f'{a}')
print('Матрица b = ')
print(b)
print('Матрица а + b = ')
print(a + b)

a = Matrix([[1], [2]])
b = Matrix([[3], [4]])

print('Матрица а = ')
print(f'{a}')
print('Матрица b = ')
print(b)
print('Матрица а + b = ')
print(a + b)

a = Matrix([[1, 2]])
b = Matrix([[3, 4]])

print('Матрица а = ')
print(f'{a}')
print('Матрица b = ')
print(b)
print('Матрица а + b = ')
print(a + b)
