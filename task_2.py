# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

class Clothes:
    def __init__(self, name):
        # print('parent init')
        self.name = name


class Coat(Clothes):
    def __init__(self, name, size):
        # print('child coat init')
        super().__init__(name)
        self.v = size

    @property
    def calc(self):
        return self.v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, name,  height):
        # print('child costume init')
        super().__init__(name)
        self.h = height

    @property
    def calc(self):
        return self.h*2 + 0.3


coat_1 = Coat('coat 1', 5)
print(coat_1.calc)

costume_1 = Costume('costume 1', 100)
print(costume_1.calc)

