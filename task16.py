"""Класс Cat, который имеет свойства имя, возраст и цвет. Метод,
который выводит информацию о кошке в формате 'Кошка по имени Имя, Возраст лет, цвет Цвет'"""


class Cat:
    def __init__(self, nickname, age, color):  # Конструктор класса Cat
        self.nickname = nickname               # Свойства класса Cat
        self.age = age
        self.color = color

    def output(self):                          # Метод output для вывода информации на экран
        print(f"Кошка по имени {self.nickname}, {self.age} лет, цвет {self.color}")


Cat1 = Cat("Чевапчич", 3, "серобуромалиновый")

Cat1.output()
