"""
Создайте функцию, которая принимает на вход строку и возвращает ее в обратном
порядке.
"""


def reverse_string(string):
    res = ""                    # Объявляем пустую результирующую строку
    for i in reversed(string):  # Цикл по перевернутой строке с заполнением результирующей строки
        res += i
    return res


reverse_string1 = reverse_string("Строка")

print(reverse_string1)
