"""
Напишите программу для поиска всех файлов с заданным расширением в заданной
директории и всех ее поддиректориях. Если директория не найдена, программа должна
вызывать исключение.
"""

import glob
import os


def dir_find(path, extension):
    # Проверка каталога
    if not os.path.exists(path):
        return print('Каталог не найден')

    files = glob.glob(path + '**/*.' + extension, recursive=True)  # Поиск файлов в указанном каталоге с указанным
    return print(files)                                            # расширением


path1 = input('Введите путь до каталога (например C:/../): ')
extension1 = input('Введите расширение файла (например txt): ')
dir_find(path1, extension1)
