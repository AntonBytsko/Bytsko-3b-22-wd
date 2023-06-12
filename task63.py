"""
Создать класс "Карточка товара". Реализовать атрибуты "название", "стоимость",
"количество" и методы "уменьшение количества" и "изменение стоимости" с защитой от
отрицательного количества и отрицательной стоимости товара.
"""

import pandas as pd


class Cart:
    def __init__(self, column1, column2, column3):
        self.column1 = column1  # Product name
        self.column2 = column2  # Price
        self.column3 = column3  # Count
        self.df = pd.DataFrame({self.column1: [], self.column2: [], self.column3: []})  # Инициализируем DataFrame

    # Добавление товара в Корзину
    def add(self, product_name, price, cnt):
        self.df.loc[len(self.df.index)] = [product_name, price, cnt]

    # Увеличение количества
    def increase(self, index):
        self.df.at[index, self.column3] += 1

    # Уменьшение количества
    def decrease(self, index):
        self.df.at[index, self.column3] -= 1
        if self.df.at[index, self.column3] <= 0:
            print('Ошибка. Отрицательное количество')
            self.df.at[index, self.column3] = 1

    # Изменение цены
    def change_price(self, index, new_price):
        self.df.at[index, self.column2] = new_price
        if self.df.at[index, self.column2] < 0:
            print('Ошибка. Стоимость не может быть ниже 0')
            self.df.at[index, self.column2] = 0

    def display(self):
        return print(self.df)


Cart1 = Cart('Product name', 'Price', 'Count')
Cart1.add('Product1', 2100, 1)
Cart1.add('Product2', 3200, 2)
Cart1.add('Product3', 3200, 0)
Cart1.increase(1)
Cart1.decrease(0)
Cart1.decrease(2)
Cart1.change_price(2, 1600)
Cart1.change_price(1, -1000)
Cart1.display()
