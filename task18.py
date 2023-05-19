"""Класс GeometricFigure, который имеет свойства площадь и периметр. Метод,
который выводит информацию о фигуре в формате 'площадь - Площадь, периметр - Периметр'"""


class GeometricFigure:
    def __init__(self, square, perimeter):  # Конструктор класса GeometricFigure
        self.square = square                # Свойства класса GeometricFigure
        self.perimeter = perimeter

    def output(self):                       # Метод output для вывода информации на экран
        print(f"Площадь - {self.square}, периметр - {self.perimeter}")


GeometricFigure1 = GeometricFigure(20, 10)

GeometricFigure1.output()
