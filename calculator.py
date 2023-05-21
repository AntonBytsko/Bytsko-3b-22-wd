"""Функции для вычисления арифметических операций."""


# Сложение
def addition(arg1, arg2):
    check_number = True
    # Проверка аргументов
    try:                       # Преобразование введенного значения в число с проверкой
        arg1 = int(arg1)
        arg2 = int(arg2)
    except ValueError:         # Если произошла ошибка при преобразовании в число, поднять флаг check_number = False
        check_number = False

    # Вычисление
    if check_number:           # Если проверка пройдена
        res = arg1 + arg2      # выполняем математическую операцию
    else:
        res = "Некорректный тип аргументов"
    return res


# Вычитание
def subtraction(arg1, arg2):
    check_number = True
    try:
        arg1 = int(arg1)
        arg2 = int(arg2)
    except ValueError:
        check_number = False
    if check_number:
        res = arg1 - arg2
    else:
        res = "Некорректный тип аргументов"
    return res


# Умножение
def multiplication(arg1, arg2):
    check_number = True
    try:
        arg1 = int(arg1)
        arg2 = int(arg2)
    except ValueError:
        check_number = False
    if check_number:
        res = arg1 * arg2
    else:
        res = "Некорректный тип аргументов"
    return res


# Деление
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
