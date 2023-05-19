"""Класс Rectangle, представляющий прямоугольник по длине и ширине, и
метод для вычисления его площади"""


class Rectangle:
    def __init__(self, length, height):  # Конструктор класса Rectangle
        self.length = length             # Свойства класса Rectangle
        self.height = height

    def calc_square(self):               # Метод calc_square для вычисления площади
        calc_res = self.length * self.height
        return calc_res


Rectangle1 = Rectangle(10, 5)            # Создание объекта Rectangle1 на основе класса Rectangle

# Проверка результата
test_res = Rectangle1.calc_square()
print(test_res)
