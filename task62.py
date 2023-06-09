"""
Создать класс "Робот" с атрибутами "имя", "скорость" и методом "движение", который
выводит на экран, какой путь прошел робот за указанное время с учетом его скорости.
Создать двух наследников класса "Робот": "Гусеничный робот" с атрибутом
"территория" и "Робот на колесах" с атрибутом "марка автомобиля".

"""


class Robot:
    def __init__(self, name, speed):
        self.name = name               # Аттрибут Имя
        self.speed = speed             # Аттрибут Скорость

    # Поиск пройденного пути
    def movement(self, time):
        traveled = time * self.speed
        return print(f"Робот {self.name} пройдет {traveled} км за {time} ч, при скорости {self.speed} км/ч")


# Гусеничный робот (CrawlerRobot наследник класса Robot)
class CrawlerRobot(Robot):
    def __init__(self, territory, name, speed):
        super().__init__(name, speed)
        self.territory = territory     # Аттрибут Территория

    # Метод родительского класса можно переопределить
    def movement(self, time):
        traveled = time * self.speed
        return print(f"Робот {self.name} пройдет {traveled} км по {self.territory} за {time} ч,"
                     f" при скорости {self.speed} км/ч")


# Робот на колесах (RobotOnWheels наследник класса Robot)
class RobotOnWheels(Robot):
    def __init__(self, model, name, speed):
        super().__init__(name, speed)
        self.model = model             # Аттрибут Марка автомобиля

    def movement(self, time):
        traveled = time * self.speed
        return print(f"Робот {self.name} марки {self.model} пройдет {traveled} км за {time} ч,"
                     f" при скорости {self.speed} км/ч")


Robot1 = Robot('Chappy', 21)
Robot1.movement(5)

CrawlerRobot1 = CrawlerRobot('Аляска', 'Счастливчик', 20)
CrawlerRobot1.movement(3)

RobotOnWheels1 = RobotOnWheels('Lada', 'Бедолага', 10)
RobotOnWheels1.movement(2)
