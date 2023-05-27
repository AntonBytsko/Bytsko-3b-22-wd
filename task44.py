"""
Напишите программу, которая открывает файл "test.txt" и выводит его содержимое на
экран. Если файл не найден, программа должна выводить сообщение "Файл не найден" и
прекращать работу.
"""

try:
    file = open('text.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print("Файл не найден")
else:
    text = file.read()
    print(text)
    file.close()
