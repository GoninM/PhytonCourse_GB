# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def date_to_int(cls, date: str):
        date_list = []
        try:
            for n in date.split('-'):
                date_list.append(int(n))
            print(f'{date_list[0]}-{date_list[1]}-{date_list[1]}, '
                  f'{type(date_list[0])}-{type(date_list[1])}-{type(date_list[2])}')
        except ValueError:
            print('Format is incorrect')

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

    Date.date_to_int('00-00-00')
    Date.date_to_int('12-12-22')
    Date.date_to_int('2-1-2033')
    Date.date_to_int('v-b-n')

    test_date = Date('12-12-2012')
    test_date.date_to_int('11-11-2011')




