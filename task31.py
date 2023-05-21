"""
Создайте модуль `calculator.py`, который содержит функции для сложения, вычитания,
умножения и деления. Импортируйте этот модуль в другом скрипте и используйте его
функции для вычисления арифметических операций.
"""

import calculator

print(calculator.addition(4, 4))        # Сложение
print(calculator.subtraction(4, 4))     # Вычитание
print(calculator.multiplication(4, 4))  # Умножение
print(calculator.division(4, 4))        # Деление
print(calculator.division(4, 0))        # Деление на 0
print(calculator.division(4, "s"))      # Некорректный аргумент
