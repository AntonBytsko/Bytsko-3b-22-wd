"""Класс Car, который имеет свойства марка, модель, год выпуска и цена. Метод,
который выводит информацию об автомобиле в формате 'Марка - модель, год выпуска, цена'"""


class Car:
    def __init__(self, brand, model, produced, price):  # Конструктор класса Car
        self.brand = brand                              # Свойства класса Car
        self.model = model
        self.produced = produced
        self.price = price

    def output(self):                                   # Метод output для вывода информации на экран
        print(f"{self.brand} - {self.model}, produced in {self.produced}, {self.price} RUB")


Car1 = Car("BMW", "X6", 2023, 9300000)

Car1.output()
