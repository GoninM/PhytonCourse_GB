# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).

# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Store:
    def __init__(self, area, number_of_places):
        self.area = area
        self.number_of_places = number_of_places


class OfficeEquipment:
    def __init__(self, manufacture: str, model: str, weight: float):
        self.manufacture = manufacture
        self.model = model
        self.weight = weight


class Printer(OfficeEquipment):
    def __init__(self, manufacture: str, model: str, weight: float, is_color: bool, page_per_minute: int):
        super().__init__(manufacture, model, weight)
        self.is_color = is_color
        self.page_per_minute = page_per_minute


class Scaner(OfficeEquipment):
    def __init__(self, manufacture: str, model: str, weight: float, page_per_minute: int, page_size):
        super().__init__(manufacture, model, weight)
        self.page_per_minute = page_per_minute
        self.page_size = page_size


class Xerox(OfficeEquipment):
    def __init__(self, manufacture: str, model: str, weight: float, page_per_minute: int, page_size):
        super().__init__(manufacture, model, weight)
        self.page_per_minute = page_per_minute
        self.page_size = page_size

