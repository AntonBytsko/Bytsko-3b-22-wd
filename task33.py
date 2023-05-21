"""
Создайте программу, которая принимает строку в качестве входных данных и выводит
частоту использования каждого символа в строке.
"""


def symbol_count(string):
    res = {}                      # Объявляем словарь типа dict
    for i in string:              # Цикл по каждому символу строки
        count = 0
        for k in string:          # Поиск текущего символа в строке
            if i == k:
                count += 1
            else:
                pass
        res[i] = count
    return res


print(symbol_count("Аааапрввккеннннооо"))
