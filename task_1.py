# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    __states = ['red', 'yellow', 'green']

    __durations = {'red': 7,
                   'yellow': 2,
                   'green': 5}

    __colors = {'red': '\x1b[0;30;41m',
                'yellow': '\x1b[0;30;43m',
                'green': '\x1b[0;30;42m'}

    def __init__(self):
        self.__color = 'red'

    def running(self):
        while True:
            for state in self.__states:
                counter = self.__durations[state]
                while counter > 0:
                    print(self.__colors[state] + f'{counter} {state}' + '\x1b[0m')
                    counter -= 1
                    sleep(1)


tr_light = TrafficLight()
tr_light.running()
