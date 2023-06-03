"""
Создать класс "Список домашних дел" с методами "добавить элемент", "удалить
элемент" и "вывести на экран". При каждом добавлении элемента в список сохранять
его в файл и при инициализации класса загружать сохраненный список из файла.
"""


class HouseholdTodoList:

    def __init__(self):
        # Загрузка сохраненного списка из файла при инициализации
        with open('task53.txt', 'r', encoding='utf-8') as file:
            self.lines = file.read()
            file.close()

    # Добавление строки
    def add(self, string):
        with open('task53.txt', 'a', encoding='utf-8') as file:
            file.writelines(string + '\n')
            file.close()
        return

    # Удаление строки
    def delete(self, index):
        with open('task53.txt', 'r') as file:
            lines = file.readlines()
            del lines[index]
            file.close()
        with open('task53.txt', 'w') as file:
            file.writelines(lines)
            file.close()
        return

    # Вывод на экран
    def print(self):
        return print(self.lines)


HouseholdTodoList1 = HouseholdTodoList()
# HouseholdTodoList1.delete(2)
# ouseholdTodoList1.add('Строка 7')
HouseholdTodoList1.print()
