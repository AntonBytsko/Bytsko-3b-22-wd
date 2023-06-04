"""
Дан список строк "apple", "orange", "banana", "pineapple", "grape". Отсортировать
его в порядке убывания длины строк.
"""
"""
from operator import itemgetter

arr = ["apple", "orange", "banana", "pineapple", "grape"]
arr_cnt = {}
# Составление словаря со словами из массива и количеством символов в каждом слове
for i in arr:
    count = 0
    for k in i:
        count += 1
    arr_cnt.update({i: count})
sorted_arr_cnt = dict(sorted(arr_cnt.items(), key=itemgetter(1)))  # Сортировка словаря по значениям ключей
reversed_arr_cnt = dict(reversed(sorted_arr_cnt.items()))          # Переворот словаря
print(list(reversed_arr_cnt))                                      # Вывод на экран с преобразованием в массив
"""

arr = ["apple", "orange", "banana", "pineapple", "grape"]
print(sorted(arr, key=len, reverse=True))
