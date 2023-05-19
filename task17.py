"""Класс Book, который имеет свойства название, автор, год издания и жанр. Метод,
который выводит информацию о книге в формате 'Название, автор (год издания), жанр'"""


class Book:
    def __init__(self, name, author, published, genre):  # Конструктор класса Book
        self.name = name                                 # Свойства класса Book
        self.author = author
        self.published = published
        self.genre = genre

    def output(self):                                    # Метод output для вывода информации на экран
        print(f"{self.name}, {self.author} ({self.published}), {self.genre}")


Book1 = Book("Властелин Колец", "Толкиен", "2003", "Приключения")

Book1.output()
