# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print(f'trun {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('over speed 60')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('over speed 40')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


print('Class Car check: ')
car_1 = Car(100, 'red', 'car_1', True)
car_1.go()
car_1.stop()
car_1.turn('left')
car_1.turn('right')
print(car_1.speed)
print(car_1.color)
print(car_1.is_police)
print(car_1.name)
car_1.show_speed()
print('\n')


print('Class TownCar check: ')
car_2 = TownCar(61, 'brown', 'car_2', False)
car_2.go()
car_2.stop()
car_2.turn('left')
car_2.turn('right')
print(car_2.speed)
print(car_2.color)
print(car_2.is_police)
print(car_2.name)
car_2.show_speed()
print('\n')


print('Class SportCar check: ')
car_3 = SportCar(161, 'white', 'car_3', False)
car_3.go()
car_3.stop()
car_3.turn('left')
car_3.turn('right')
print(car_3.speed)
print(car_3.color)
print(car_3.is_police)
print(car_3.name)
car_3.show_speed()
print('\n')


print('Class WorkCar check: ')
car_4 = WorkCar(161, 'black', 'car_4', True)
car_4.go()
car_4.stop()
car_4.turn('left')
car_4.turn('right')
print(car_4.speed)
print(car_4.color)
print(car_4.is_police)
print(car_4.name)
car_4.show_speed()
print('\n')


print('Class PoliceCar check: ')
car_5 = PoliceCar(61, 'blue', 'car_5', True)
car_5.go()
car_5.stop()
car_5.turn('left')
car_5.turn('right')
print(car_5.speed)
print(car_5.color)
print(car_5.is_police)
print(car_5.name)
car_5.show_speed()
print('\n')
