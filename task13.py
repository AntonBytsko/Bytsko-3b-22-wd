"""Класс BankAccount, описывающий описывающий банковский счет со свойствами
имя владельца, номер счета и баланс, и методами для пополнения и снятия средств со счета"""


class BankAccount:

    def __init__(self, owner, account, balance):
        self.owner = owner
        self.account = account
        self.balance = balance

    def enroll(self, summ):       # Зачислить
        enroll_res = "Зачислено " + str(summ) + ", остаток на счете " + str(self.balance + summ)
        return enroll_res

    def write_off(self, summ):    # Списать
        if self.balance < summ:
            write_off_res = "Недостаточно средств на счете " + self.account
        else:
            write_off_res = "Списано " + str(summ) + ", остаток на счете " + str(self.balance - summ)
        return write_off_res


BankAccount1 = BankAccount("Anton Bytsko", "4886754320070943", 100000)

# Проверка результата
# test_res = BankAccount1.enroll(100)
test_res = BankAccount1.write_off(200000)
print(test_res)
