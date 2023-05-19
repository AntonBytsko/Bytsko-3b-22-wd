"""Класс Student, который имеет свойства имя, фамилия, возраст и специальность. Метод,
который выводит информацию о студенте в формате 'Имя - Фамилия, возраст лет, специальность'"""


class Student:
    def __init__(self, name, surname, age, speciality):  # Конструктор класса Student
        self.name = name                                 # Свойства класса Student
        self.surname = surname
        self.age = age
        self.speciality = speciality

    def output(self):                                    # Метод output для вывода информации на экран
        print(f"{self.name} - {self.surname}, age {self.age}, {self.speciality} RUB")


Student1 = Student("Anton", "Bytsko", 32, "programmer")

Student1.output()
