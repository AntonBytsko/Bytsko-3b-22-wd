"""
Напишите программу, которая запрашивает у пользователя имя файла для чтения и
выводит его содержимое на экран. Если файл не найден или возникает ошибка при чтении,
программа должна выводить сообщение "Ошибка" и прекращать работу.
"""

input_file = input("Введите имя файла (с расширением): ")

try:
    file = open(input_file, 'r', encoding='utf-8')
except FileNotFoundError:
    print("Ошибка")
except OSError:
    print("Ошибка")
else:
    text = file.read()
    print(text)
    file.close()
