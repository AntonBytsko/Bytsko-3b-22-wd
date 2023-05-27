"""
Напишите программу, которая открывает файл "text.txt" и выводит его содержимое на
экран.
"""

file = open('text.txt', 'r', encoding='utf-8')
text = file.read()
print(text)
file.close()
