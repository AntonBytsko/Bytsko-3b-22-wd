"""
Дан список кортежей с координатами точек (1, 2), (3, 4), (-1, 5), (6, -3).
Отсортировать его по расстоянию от начала координат.
"""
import pandas as pd
import math

# Реализация через itemgetter
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
"""

# Реализация через DataFrame

arr = [(1, 2), (3, 4), (-1, 5), (6, -3)]
arr_dict = {"coordinates": [], "distance": []}
# Заполнение ассоциативного массива с расчетом расстояний
for i in arr:
    dist = math.dist((0, 0), i)
    arr_dict['coordinates'].append(i)
    arr_dict['distance'].append(dist)

"""
print(arr_dict)
{'coordinates': [(1, 2), (3, 4), (-1, 5), (6, -3)], 'distance': [2.23606797749979, 5.0,
                                                                 5.0990195135927845, 6.708203932499369]}
"""

df = pd.DataFrame(arr_dict)                    # Преобразование ассоциативного массива в DataFrame
sorted_df = df.sort_values(by='distance')      # Сортировка внутри DataFrame
np = sorted_df['coordinates'].to_numpy()       # Преобразование DataFrame в NumPy массив
# print(sorted_df)  # для отладки
print(np)

# Реализация через подстановку функции в параметр sorted

"""
arr = [(1, 2), (3, 4), (-1, 5), (6, -3)]


def sort_by_dist(element):
    return math.dist((0, 0), element)


sortedList = sorted(arr, key=sort_by_dist)
print(sortedList)
"""