# TODO здесь писать код

class House:

    def __init__(self, food: int = 50, money: int = 0):
        self.refrigerator = food
        self.nightstand = money

    def info(self):
        print('Дом, адрес - не указан, холодильник полон на {food}, '
              'уровень денег - {money}'.format(
            food = self.refrigerator, money = self.nightstand))

class Human:

    def __init__(self, name: str, home: House, satiety: int = 50):
        self.name = name
        self.satiety = satiety
        self.home = home

    def info(self):
        print('Меня зовут {h_name}, сыт(а) я на {h_satiety}, '
              'живу в {house}'.format(
            h_name = self.name, h_satiety = self.satiety, house = self.home))
    def eat(self):
        # print('Можно и поесть')
        if self.home.refrigerator >= 5:
            self.home.refrigerator -= 5
            self.satiety += 5
        # else:
        #     print('Есть нечего')

    def work(self):
        # print('На любимую работу')
        self.satiety -= 10
        if self.satiety <= 0:
            raise BaseException('Сытость упала до 0 - человек умер :(')
        self.home.nightstand += 10

    def play(self):
        # print('Меня нет, я играть, буду когда вернусь')
        self.satiety -= 10
        if self.satiety <= 0:
            raise BaseException('Сытость упала до 0 - человек умер :(')

    def restock(self):
        # print('Опят/ь в Шестёрочку переться.')
        if self.home.nightstand >= 5:
            self.home.nightstand -= 5
            print(self.home.nightstand)
            self.home.refrigerator += 5
            print(self.home.refrigerator)
        else:
            print('Денег недостаточно :(')

from random import randint


house = House()
man_1 = Human('Василий', house)
woman_1 = Human('Лера', house)

house.info()
man_1.info()
woman_1.info()

for _ in range(1000):

    rand_num = randint(1, 6)

    if man_1.satiety < 20:
        man_1.eat()
    elif house.refrigerator < 10:
        man_1.restock()
    elif house.nightstand < 50:
        man_1.work()
    elif rand_num == 1:
        man_1.work()
    elif rand_num == 2:
        man_1.eat()
    else:
        man_1.play()

    if woman_1.satiety < 20:
        woman_1.eat()
    elif house.refrigerator < 10:
        woman_1.restock()
    elif house.nightstand < 50:
        woman_1.work()
    elif rand_num == 1:
        woman_1.work()
    elif rand_num == 2:
        woman_1.eat()
    else:
        woman_1.play()

else:
    print('\nПрошёл год\n')
    house.info()
    man_1.info()
    woman_1.info()
