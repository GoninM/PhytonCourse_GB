# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_int(cls):
        pass #??? как это сделать


    @staticmethod
    def validate(date: str):
        date_list = []
        try:
            for n in date.split('-'):
                date_list.append(int(n))

            if (1 <= date_list[0] <= 31) and (1 <= date_list[1] <= 12) and (date_list[2] >= 0):
                print('Format is correct')
            else:
                print('Format is incorrect')
        except ValueError:
            print('Format is incorrect')


if __name__ == '__main__':
    Date.validate('00-00-00')
    Date.validate('01-00-00')
    Date.validate('01-01-00')
    Date.validate('1-1-1')
    Date.validate('a-b-c')
    Date.validate('22-2-2022')


