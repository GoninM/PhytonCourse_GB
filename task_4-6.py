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

class ErrorType(Exception):
    def __init__(self, txt):
        self.txt = txt


class Store:
    __store = {}
    __departments = {}

    # __places = {}

    def __init__(self, area: float, number_of_places: int):
        # инициализируем площадь склада и количество мест, пока что нигде не используется
        self.area = area
        self.number_of_places = number_of_places

    def store_item(self, item: str, number: int):
        # указываем, что получаем на склад, в каком кол-ве. возможно стоит добавить место, где хранится

        try:
            if type(1) != type(number):
                raise ErrorType(f'тип {number} - {type(number)}')

            if item in self.__store:
                self.__store[item] += number
            else:
                self.__store[item] = number
        except ErrorType as err:
            print(err)

    def get_store(self):
        return self.__store

    def move_to_department(self, item, department, number):
        # указываем в какой отдел отправляем, что именно и в каком кол-ве.
        try:
            if type(1) != type(number):
                raise ErrorType(f'тип {number} - {type(number)}')

            if not item in self.__store:
                print(f'на складе нет позиции "{item}"')
            else:
                if self.__store[item] <= number:
                    number = self.__store[item]

                if department in self.__departments:
                    if item in self.__departments[department]:
                        self.__departments[department][item] += number
                    else:
                        self.__departments[department][item] = number
                else:
                    self.__departments[department] = {item: number}

                self.__store[item] -= number
                if self.__store[item] == 0:
                    self.__store.pop(item)

        except ErrorType as err:
            print(err)


    def get_departments(self):
        return self.__departments


class OfficeEquipment:
    def __init__(self, equipment: str, manufacture: str, model: str, weight: float):
        self.manufacture = manufacture
        self.model = model
        self.weight = weight
        self.equipment = equipment

    @property
    def name(self):
        return f'{self.equipment} {self.manufacture} {self.model}'


class Printer(OfficeEquipment):
    def __init__(self, manufacture: str, model: str, weight: float, is_color: bool, page_per_minute: int):
        super().__init__('Printer', manufacture, model, weight)
        self.is_color = is_color
        self.page_per_minute = page_per_minute


class Scaner(OfficeEquipment):
    def __init__(self, manufacture: str, model: str, weight: float, page_per_minute: int, page_size):
        super().__init__('Scaner', manufacture, model, weight)
        self.page_per_minute = page_per_minute
        self.page_size = page_size


class Xerox(OfficeEquipment):
    def __init__(self, manufacture: str, model: str, weight: float, page_per_minute: int, page_size):
        super().__init__('Xerox', manufacture, model, weight)
        self.page_per_minute = page_per_minute
        self.page_size = page_size


printer_1 = Printer('Canon', 'model-1', 15, True, 22)
printer_2 = Printer('Brother', 'model-2', 10, False, 10)

store_1 = Store(1000, 100)
store_1.store_item(printer_1.name, '7')
store_1.store_item(printer_2.name, 20)
store_1.store_item('xerox', 30)
store_1.store_item('scaner', 40)
store_1.store_item('printer', 4)

print(store_1.get_store())

store_1.move_to_department('printer', 'helpdesk', "3")
store_1.move_to_department('printer', 'soft_room', 5)
store_1.move_to_department('scaner', 'helpdesk', 1)
store_1.move_to_department(printer_1.name, 'helpdesk', 4)

print(store_1.get_departments())
print(store_1.get_store())
