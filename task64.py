"""
Создать класс "Банк", который хранит информацию о клиентах, счетах и транзакциях.
Реализовать методы для создания клиента и открытия счета, а также для совершения
перевода с одного счета на другой с проверкой на наличие достаточной суммы на
счете.
"""
import pandas as pd


class Bank:
    def __init__(self, column1, column2, column3):
        self.column1 = column1  # Client
        self.column2 = column2  # Account
        self.column3 = column3  # Balance
        self.df = pd.DataFrame({self.column1: [], self.column2: [], self.column3: []})  # Инициализируем DataFrame

    # Создание клиента
    def create_client(self, name):
        self.df.loc[len(self.df.index)] = [name, '', 0]          # Добавление клиента в DataFrame с пустыми значениями

    # Создание счета
    def create_account(self, index, account_number):
        self.df.at[index, self.column2] = account_number         # Создание счета по "ID клиента"

    # Зачисление денежных средств на счет
    def add_money(self, account, amount):
        acc_to = self.df[self.column2] == account                # Поиск нужной записи с указанным счетом
        self.df.loc[acc_to, self.column3] += amount              # Обновление столбца Balance у записи с данным счетом

    # Перевод со счета на счет
    def transaction(self, account1, account2, amount):
        acc_from = self.df[self.column2] == account1             # Поиск нужной записи с указанным счетом
        if self.df.loc[acc_from, self.column3][1] < amount:      # Если значение столбца Balance меньше введенной суммы
            print(f'Недостаточно средств на счете {account1}')   # Показать ошибку и выйти из метода
            return
        else:
            self.df.loc[acc_from, self.column3] -= amount        # Иначе вычесть сумму из значения столбца Balance

        acc_to = self.df[self.column2] == account2               # Поиск нужной записи с указанным счетом 2
        self.df.loc[acc_to, self.column3] += amount              # Обновление столбца Balance у записи с данным счетом 2

    def display(self):
        return print(self.df)


Bank1 = Bank('Client', 'Account', 'Balance')
Bank1.create_client('Client1')
Bank1.create_account(0, '40817810099910004312')
Bank1.create_client('Client2')
Bank1.create_account(1, '40817810099910001234')
Bank1.add_money('40817810099910001234', 5000)
Bank1.transaction('40817810099910001234', '40817810099910004312', 2000)
Bank1.display()
