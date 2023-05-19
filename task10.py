"""Класс Person, описывающий человека со свойствами имя и возраст,
и метод для печати этой информации"""


class Person:
    def __init__(self, name, age):  # Конструктор класса Person
        self.name = name            # Свойства класса Person
        self.age = age

    def output(self):               # Метод output для вывода информации на экран
        print(self.name, self.age)


Person1 = Person("Anton", 32)

Person1.output()
