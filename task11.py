"""Класс Dog, описывающий собаку со свойствами имя, порода и возраст,
и метод для печати этой информации"""


class Dog:
    def __init__(self, name, breed, age):  # Конструктор класса Dog
        self.name = name                   # Свойства класса Dog
        self.breed = breed
        self.age = age

    def output(self):                      # Метод output для вывода информации на экран
        print(self.name, self.breed, self.age)


Dog1 = Dog("Marsel", "Korgi", 2)

Dog1.output()
