"""
Создайте класс "Сотрудник". У этого класса должны быть атрибуты "имя", "возраст" и
"зарплата". Напишите метод "представление", который выводит информацию о сотруднике в
консоль. Создайте объект этого класса и вызовите у него метод "представление".
"""

class Employee:
    def __init__(self, name, age, salary):  # Конструктор класса Employee
        self.name = name                    # Свойства класса Employee
        self.age = age
        self.salary = salary

    def presentation(self):                 # Метод output для вывода информации на экран
        print(f"Сотрудник {self.name}, возраст {self.age}, зарплата {self.salary}")


Employee1 = Employee("Anton Bytsko", 32, 260000)

Employee1.presentation()
