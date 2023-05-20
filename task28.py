"""
Напишите программу для калькулятора, который принимает два числа и операцию
(сложение, вычитание, умножение, деление) и выводит результат на экран.
"""

check_number = True

# Ввод первого числа с проверкой
number1 = input("Введите первое число: ")
try:
    number1 = int(number1)
except ValueError:
    check_number = False

# Ввод второго числа с проверкой
number2 = input("Введите второе число: ")
try:
    number2 = int(number2)
except ValueError:
    check_number = False

if check_number:
    command = input("Введите операцию (+,-,*,/): ")
    match command.split():
        case ["+"]:
            res = number1 + number2
            print(res)
        case ["-"]:
            res = number1 - number2
            print(res)
        case ["*"]:
            res = number1 * number2
            print(res)
        case ["/"]:
            if number2 == 0:
                print("Деление на 0, введите другое число")
            else:
                print(number1 / number2)
        case _:  # Аналогично default в других языках
            print(f"Введена некорректная операция {command!r}")
else:
    print("Введено некорректное значение, повторите ввод")
