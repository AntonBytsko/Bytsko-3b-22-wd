"""
Даны массивы: 24, 36, 48, 60; 12, 18, 24, 36, 72. Найти наибольший общий делитель
двух массивов чисел.
"""


def comm_div(arr):  # Поиск общих делителей каждого элемента массива
    arr_length = len(arr)
    
    all_divisor = []     # Массив всех делителей каждого элемент массива
    common_divisor = []  # Массив общих делителей каждого элемента массива

    # Поиск всех делителей каждого элемента массива
    for i in arr:
        for k in range(1, i + 1):
            if i % k == 0:
                all_divisor.append(k)
    # print(all_divisor)  # для отладки
    
    # Поиск общих делителей каждого элемента массива
    for i in all_divisor:
        count = 0
        for k in all_divisor:
            if i == k:
                count += 1
            if count == arr_length:
                if common_divisor.count(k) == 0:
                    common_divisor.append(k)
                break
    # print(common_divisor)  # для отладки
    return common_divisor


res1 = comm_div([24, 36, 48, 60])      # Поиск общих делителей каждого элемента первого массива
res2 = comm_div([12, 18, 24, 36, 72])  # Поиск общих делителей каждого элемента второго массива

# Поиск общих делителей для двух массивов
res3 = []
for i in res1:
    if res2.count(i):
        res3.append(i)
# print(res1)  # для отладки
# print(res2)  # для отладки
# print(res3)  # для отладки

# Поиск наибольшего общего делителя для двух массивов
res = res3[0]
for k in res3:
    if k >= res:
        res = k

print(res)
