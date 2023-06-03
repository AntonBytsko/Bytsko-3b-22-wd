"""
Дан список кортежей с координатами точек (1, 2), (3, 4), (-1, 5), (6, -3).
Отсортировать его по расстоянию от начала координат.
"""
import math
from operator import itemgetter

arr = [(1, 2), (3, 4), (-1, 5), (6, -3)]
tup = tuple(arr)
dist_dict = {}
for i in tup:
    dist = math.dist((0, 0), i)                                        # Рассчет расстояния от 0 координат до значения
    dist_dict.update({i: dist})                                        # Запись в словарь {координаты:расстояние}
sorted_dist_dict = dict(sorted(dist_dict.items(), key=itemgetter(1)))  # Сортировка словаря по значениям ключей
print(list(sorted_dist_dict))                                          # Вывод на экран с преобразованием в массив
