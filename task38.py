"""
Напишите программу, которая открывает файл "text.txt" и выводит его содержимое на
экран.
"""

file = open('text.txt', 'r', encoding='utf-8')  # Открытие файла
text = file.read()                              # Чтение файла
print(text)
file.close()                                    # Закрытие файла (обязательно всегда)