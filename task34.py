"""
Напишите программу, которая выводит таблицу умножения от 1 до 10.
"""


def multiplication_table(limit):
    count = 0
    for i in range(2, 10):                     # Первый множитель от 2 до 9
        for k in range(2, 10):                 # Второй множитель от 2 до 9
            print(f"{i} * {k} = {i * k}")
            count += 1
            if count == limit:
                return
            else:
                pass


multiplication_table(10)
