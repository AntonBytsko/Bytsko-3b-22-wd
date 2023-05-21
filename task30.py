"""
Напишите программу для подсчета количества гласных и согласных букв в введенной
пользователем строке.
"""


def letter_count(string):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"  # Строка с гласными буквами в верхнем и нижнем регистре
    vow_count = 0
    con_count = 0
    res = []
    for i in string:                 # Перебираем все символы строки
        if i in vowels:              # Если символ найден в строке с гласными буквами, считаем гласной буквой
            vow_count += 1
        else:                        # иначе согласной буквой
            con_count += 1

    # Записываем результат в массив для возврата значений из функции
    res.append(vow_count)
    res.append(con_count)
    return res


letter_count1 = letter_count("СтрокА")
print(f"Гласных букв {letter_count1[0]}, согласных букв {letter_count1[1]}")
