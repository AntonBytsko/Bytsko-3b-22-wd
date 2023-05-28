"""
Напишите программу, которая открывает файл "test.txt" и записывает в него сообщение
"Hello, world!" Если возникает ошибка при записи, программа должна выводить сообщение
"Ошибка" и прекращать работу.
"""

try:
    file = open('test.txt', 'w')
    file.write('Hello, world!\n')
    file.close()
except FileNotFoundError:
    print("Ошибка")
except OSError:
    print("Ошибка")
