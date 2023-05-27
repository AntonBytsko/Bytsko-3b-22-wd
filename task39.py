"""
Напишите программу, которая создает новый файл "new_file.txt" и записывает туда
сообщение "Hello, world!".
"""

with open('new_file.txt', 'w') as file:
    file.write('Hello, world!')
