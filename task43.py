"""
Напишите программу, которая запрашивает у пользователя два числа и выводит
результат их деления. Если пользователь вводит некорректные данные (например, символы
вместо чисел или деление на ноль), программа должна выводить сообщение "Ошибка" и
прекращать работу.
"""


def division(arg1, arg2):
    check_number = True
    try:
        arg1 = int(arg1)
        arg2 = int(arg2)
    except ValueError:
        check_number = False
    if check_number:
        if arg2 == 0:
            res = "Деление на 0!"
        else:
            res = arg1 / arg2
    else:
        res = "Некорректный тип аргументов"
    return res


print(division("g", 4))
