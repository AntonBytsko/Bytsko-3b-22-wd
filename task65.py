"""
Напишите программу, которая создаст двух игровых персонажей, установит им значения
свойств (имя, уровень, здоровье, атака, защита) и запустит 3 боевых раунда, в которых
персонажи будут наносить друг другу урон. По итогу промежуточного раунда и итоговой
оценки сообщит о победившем и проигравшем.
Задача: Создать класс "Игровой персонаж", который будет иметь следующие свойства: имя,
уровень, здоровье, атака и защита.
Также необходимо добавить методы для изменения свойств персонажа:
- метод для применения урона, который будет уменьшать здоровье персонажа на указанное
значение
- метод для повышения уровня персонажа, который будет увеличивать уровень и
увеличивать здоровье и атаку на 10%
"""

import random


class Character:
    def __init__(self, name, level, health, attack, protection):
        self.name = name                                  # Имя персонажа
        self.level = level                                # Уровень персонажа
        self.health = health                              # Здоровье
        self.attack = attack                              # Сила атаки
        self.protection = protection                      # Защита
        self.damaged = self.health

    # Атака
    def hit(self):
        return random.randint(1, self.attack)             # Сила удара от 1 до максимального значения атаки

    # Получение урона
    def damage(self, quantity):
        damage = quantity - (self.protection * 10 / 100)  # Уменьшение уровня здоровья за вычетом 10% от защиты
        self.damaged -= damage
        if self.damaged <= 0:
            print(f'Персонаж {self.name} получает урон {damage}, персонаж убит')
            return True
        else:
            print(f'Персонаж {self.name} получает урон {damage}, осталось здоровья {self.damaged}')
            return False

    # Исцеление (необходимо после каждого раунда)
    def healing(self):
        self.damaged = self.health

    # Повышение уровня персонажа
    def level_up(self):
        self.level += 1
        self.health += round((self.health * 10) / 100)  # Увеличение здоровья на 10%
        self.attack += round((self.attack * 10) / 100)  # Увеличение силы атаки на 10%
        print(f'Уровень персонажа {self.name} повышен до {self.level}. Здоровье увеличено до {self.health},'
              f' атака увеличена до {self.attack}')


Character1 = Character('Char1', 1, 100, 10, 10)
Character2 = Character('Char2', 1, 100, 10, 10)

count1 = 0  # Счетчик побед для первого персонажа
count2 = 0  # Счетчик побед для второго персонажа
for i in range(3):                                                       # Объявление 3-х раундов
    ret = True
    while ret:                                                           # 1 раунд до "смерти" одного из персонажей
        if Character1.damage(Character2.hit()):                          # True возвращается если здоровье <= 0
            print(f'Раунд {i+1}. Победитель {Character2.name}')          # Значит победил другой персонаж
            Character2.level_up()
            count2 += 1
            ret = False
        elif Character2.damage(Character1.hit()):                        # и наоборот
            print(f'Раунд {i+1}. Победитель {Character1.name}')
            Character1.level_up()
            count1 += 1
            ret = False
    Character1.healing()
    Character2.healing()

if count1 > count2:
    print(f'>>> Побеждает {Character1.name}')
else:
    print(f'>>> Побеждает {Character2.name}')

"""
Пример выполнения программы

Персонаж Char1 получает урон 3.0, осталось здоровья 97.0
Персонаж Char2 получает урон 2.0, осталось здоровья 98.0
Персонаж Char1 получает урон 1.0, осталось здоровья 96.0
Персонаж Char2 получает урон 8.0, осталось здоровья 90.0
Персонаж Char1 получает урон 1.0, осталось здоровья 95.0
Персонаж Char2 получает урон 1.0, осталось здоровья 89.0
Персонаж Char1 получает урон 8.0, осталось здоровья 87.0
Персонаж Char2 получает урон 4.0, осталось здоровья 85.0
Персонаж Char1 получает урон 0.0, осталось здоровья 87.0
Персонаж Char2 получает урон 3.0, осталось здоровья 82.0
Персонаж Char1 получает урон 2.0, осталось здоровья 85.0
Персонаж Char2 получает урон 9.0, осталось здоровья 73.0
Персонаж Char1 получает урон 8.0, осталось здоровья 77.0
Персонаж Char2 получает урон 6.0, осталось здоровья 67.0
Персонаж Char1 получает урон 2.0, осталось здоровья 75.0
Персонаж Char2 получает урон 8.0, осталось здоровья 59.0
Персонаж Char1 получает урон 8.0, осталось здоровья 67.0
Персонаж Char2 получает урон 3.0, осталось здоровья 56.0
Персонаж Char1 получает урон 4.0, осталось здоровья 63.0
Персонаж Char2 получает урон 9.0, осталось здоровья 47.0
Персонаж Char1 получает урон 6.0, осталось здоровья 57.0
Персонаж Char2 получает урон 4.0, осталось здоровья 43.0
Персонаж Char1 получает урон 4.0, осталось здоровья 53.0
Персонаж Char2 получает урон 1.0, осталось здоровья 42.0
Персонаж Char1 получает урон 0.0, осталось здоровья 53.0
Персонаж Char2 получает урон 6.0, осталось здоровья 36.0
Персонаж Char1 получает урон 0.0, осталось здоровья 53.0
Персонаж Char2 получает урон 5.0, осталось здоровья 31.0
Персонаж Char1 получает урон 9.0, осталось здоровья 44.0
Персонаж Char2 получает урон 1.0, осталось здоровья 30.0
Персонаж Char1 получает урон 6.0, осталось здоровья 38.0
Персонаж Char2 получает урон 1.0, осталось здоровья 29.0
Персонаж Char1 получает урон 5.0, осталось здоровья 33.0
Персонаж Char2 получает урон 0.0, осталось здоровья 29.0
Персонаж Char1 получает урон 8.0, осталось здоровья 25.0
Персонаж Char2 получает урон 5.0, осталось здоровья 24.0
Персонаж Char1 получает урон 9.0, осталось здоровья 16.0
Персонаж Char2 получает урон 1.0, осталось здоровья 23.0
Персонаж Char1 получает урон 1.0, осталось здоровья 15.0
Персонаж Char2 получает урон 0.0, осталось здоровья 23.0
Персонаж Char1 получает урон 1.0, осталось здоровья 14.0
Персонаж Char2 получает урон 8.0, осталось здоровья 15.0
Персонаж Char1 получает урон 3.0, осталось здоровья 11.0
Персонаж Char2 получает урон 0.0, осталось здоровья 15.0
Персонаж Char1 получает урон 7.0, осталось здоровья 4.0
Персонаж Char2 получает урон 1.0, осталось здоровья 14.0
Персонаж Char1 получает урон 1.0, осталось здоровья 3.0
Персонаж Char2 получает урон 0.0, осталось здоровья 14.0
Персонаж Char1 получает урон 4.0, персонаж убит
Раунд 1. Победитель Char2
Уровень персонажа Char2 повышен до 2. Здоровье увеличено до 110, атака увеличена до 11
Персонаж Char1 получает урон 4.0, осталось здоровья 96.0
Персонаж Char2 получает урон 3.0, осталось здоровья 107.0
Персонаж Char1 получает урон 0.0, осталось здоровья 96.0
Персонаж Char2 получает урон 8.0, осталось здоровья 99.0
Персонаж Char1 получает урон 3.0, осталось здоровья 93.0
Персонаж Char2 получает урон 5.0, осталось здоровья 94.0
Персонаж Char1 получает урон 6.0, осталось здоровья 87.0
Персонаж Char2 получает урон 8.0, осталось здоровья 86.0
Персонаж Char1 получает урон 8.0, осталось здоровья 79.0
Персонаж Char2 получает урон 8.0, осталось здоровья 78.0
Персонаж Char1 получает урон 4.0, осталось здоровья 75.0
Персонаж Char2 получает урон 2.0, осталось здоровья 76.0
Персонаж Char1 получает урон 10.0, осталось здоровья 65.0
Персонаж Char2 получает урон 4.0, осталось здоровья 72.0
Персонаж Char1 получает урон 5.0, осталось здоровья 60.0
Персонаж Char2 получает урон 6.0, осталось здоровья 66.0
Персонаж Char1 получает урон 4.0, осталось здоровья 56.0
Персонаж Char2 получает урон 7.0, осталось здоровья 59.0
Персонаж Char1 получает урон 4.0, осталось здоровья 52.0
Персонаж Char2 получает урон 7.0, осталось здоровья 52.0
Персонаж Char1 получает урон 1.0, осталось здоровья 51.0
Персонаж Char2 получает урон 0.0, осталось здоровья 52.0
Персонаж Char1 получает урон 0.0, осталось здоровья 51.0
Персонаж Char2 получает урон 5.0, осталось здоровья 47.0
Персонаж Char1 получает урон 7.0, осталось здоровья 44.0
Персонаж Char2 получает урон 7.0, осталось здоровья 40.0
Персонаж Char1 получает урон 4.0, осталось здоровья 40.0
Персонаж Char2 получает урон 2.0, осталось здоровья 38.0
Персонаж Char1 получает урон 1.0, осталось здоровья 39.0
Персонаж Char2 получает урон 6.0, осталось здоровья 32.0
Персонаж Char1 получает урон 8.0, осталось здоровья 31.0
Персонаж Char2 получает урон 9.0, осталось здоровья 23.0
Персонаж Char1 получает урон 1.0, осталось здоровья 30.0
Персонаж Char2 получает урон 9.0, осталось здоровья 14.0
Персонаж Char1 получает урон 0.0, осталось здоровья 30.0
Персонаж Char2 получает урон 5.0, осталось здоровья 9.0
Персонаж Char1 получает урон 9.0, осталось здоровья 21.0
Персонаж Char2 получает урон 7.0, осталось здоровья 2.0
Персонаж Char1 получает урон 7.0, осталось здоровья 14.0
Персонаж Char2 получает урон 3.0, персонаж убит
Раунд 2. Победитель Char1
Уровень персонажа Char1 повышен до 2. Здоровье увеличено до 110, атака увеличена до 11
Персонаж Char1 получает урон 8.0, осталось здоровья 102.0
Персонаж Char2 получает урон 3.0, осталось здоровья 107.0
Персонаж Char1 получает урон 0.0, осталось здоровья 102.0
Персонаж Char2 получает урон 10.0, осталось здоровья 97.0
Персонаж Char1 получает урон 7.0, осталось здоровья 95.0
Персонаж Char2 получает урон 3.0, осталось здоровья 94.0
Персонаж Char1 получает урон 1.0, осталось здоровья 94.0
Персонаж Char2 получает урон 1.0, осталось здоровья 93.0
Персонаж Char1 получает урон 2.0, осталось здоровья 92.0
Персонаж Char2 получает урон 4.0, осталось здоровья 89.0
Персонаж Char1 получает урон 7.0, осталось здоровья 85.0
Персонаж Char2 получает урон 7.0, осталось здоровья 82.0
Персонаж Char1 получает урон 3.0, осталось здоровья 82.0
Персонаж Char2 получает урон 8.0, осталось здоровья 74.0
Персонаж Char1 получает урон 0.0, осталось здоровья 82.0
Персонаж Char2 получает урон 6.0, осталось здоровья 68.0
Персонаж Char1 получает урон 2.0, осталось здоровья 80.0
Персонаж Char2 получает урон 5.0, осталось здоровья 63.0
Персонаж Char1 получает урон 2.0, осталось здоровья 78.0
Персонаж Char2 получает урон 7.0, осталось здоровья 56.0
Персонаж Char1 получает урон 7.0, осталось здоровья 71.0
Персонаж Char2 получает урон 1.0, осталось здоровья 55.0
Персонаж Char1 получает урон 3.0, осталось здоровья 68.0
Персонаж Char2 получает урон 4.0, осталось здоровья 51.0
Персонаж Char1 получает урон 3.0, осталось здоровья 65.0
Персонаж Char2 получает урон 4.0, осталось здоровья 47.0
Персонаж Char1 получает урон 10.0, осталось здоровья 55.0
Персонаж Char2 получает урон 10.0, осталось здоровья 37.0
Персонаж Char1 получает урон 2.0, осталось здоровья 53.0
Персонаж Char2 получает урон 1.0, осталось здоровья 36.0
Персонаж Char1 получает урон 1.0, осталось здоровья 52.0
Персонаж Char2 получает урон 9.0, осталось здоровья 27.0
Персонаж Char1 получает урон 8.0, осталось здоровья 44.0
Персонаж Char2 получает урон 9.0, осталось здоровья 18.0
Персонаж Char1 получает урон 4.0, осталось здоровья 40.0
Персонаж Char2 получает урон 4.0, осталось здоровья 14.0
Персонаж Char1 получает урон 5.0, осталось здоровья 35.0
Персонаж Char2 получает урон 0.0, осталось здоровья 14.0
Персонаж Char1 получает урон 8.0, осталось здоровья 27.0
Персонаж Char2 получает урон 7.0, осталось здоровья 7.0
Персонаж Char1 получает урон 8.0, осталось здоровья 19.0
Персонаж Char2 получает урон 10.0, персонаж убит
Раунд 3. Победитель Char1
Уровень персонажа Char1 повышен до 3. Здоровье увеличено до 121, атака увеличена до 12
>>> Побеждает Char1
"""