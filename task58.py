"""
Дан список целых чисел 5, 1, 10, 3, 7. Отсортировать его в порядке возрастания и
вернуть в виде кортежа.
"""

arr = [5, 1, 10, 3, 7]
arr.sort()                  # Сортировка массива в порядке возрастания
tuple_keys = tuple(arr)     # Преобразование массива в кортеж
print(tuple_keys)
