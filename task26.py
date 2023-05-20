"""
Напишите программу, которая находит наименьший общий множитель двух чисел.
"""

# Получение простых множителей первого числа в массив
number_list1 = []
input_number1 = input("Введите первое число: ")
number1 = int(input_number1)
for i in range(1, number1 + 1):
    if number1 % i == 0:
        number_list1.append(i)

# Получение простых множителей второго числа в массив
number_list2 = []
input_number2 = input("Введите второе число: ")
number2 = int(input_number2)
for i in range(1, number2 + 1):
    if number2 % i == 0:
        number_list2.append(i)

# Поиск общих множителей
common_factors = []
for i in number_list1:
    for k in number_list2:
        if i == k and i != 1:
            common_factors.append(i)
if not common_factors:
    print("У введенных чисел нет общих множителей")
else:
    print(f"Общие множители: {common_factors}")
    print(f"Наименьший множитель двух чисел {min(common_factors)}")
