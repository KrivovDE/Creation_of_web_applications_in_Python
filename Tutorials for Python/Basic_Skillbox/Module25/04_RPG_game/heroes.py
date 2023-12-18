class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нет кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print(
            "\t",
            self.name,
            "Получил удар с силой равной = ",
            round(damage),
            ". Осталось здоровья - ",
            round(self.get_hp()),
        )
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        # Каждый наследник должен выводить информацию о своём состоянии, чтобы вы могли отслеживать ход сражения
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):
    # Целитель:
    # Атрибуты:
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # исцеление) на выбранную им цель

    def __init__(self, name: str):
        super().__init__(name)
        self.magic_power = super().get_power() * 3

    def __str__(self):
        return (
            "Я - {name} ({class_type}), уровень здоровья - {hp}, "
            "уровень сил - {power}".format(
                name=self.name,
                class_type=self.__class__.__name__,
                hp=round(self.get_hp(), 2),
                power=round(self.get_power(), 2),
            )
        )

    def attack(self, target):
        target.take_damage(round(self.get_power() / 2, 2))

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - 1.2 * damage)
        super().take_damage(damage)

    def take_heal(self, heal):
        self.set_hp(self.get_hp() + heal)
        print(
            "\t",
            self.name,
            "Получил лечение равное = ",
            round(heal),
            ". Уровень здоровья - ",
            round(self.get_hp()),
        )

    def healing(self, target):
        target.take_heal(self.magic_power)

    def make_a_move(self, friends: list, enemies: list):
        friend_hp = [friend.get_hp() for friend in friends]
        enemies_hp = [enemy.get_hp() for enemy in enemies]
        if min(friend_hp) > 120:
            target = enemies[enemies_hp.index(min(enemies_hp))]
            self.attack(target)
        else:
            target = friends[friend_hp.index(min(friend_hp))]
            self.healing(target)
        super().make_a_move(friends, enemies)


class Tank(Hero):
    # Танк:
    # Атрибуты:
    # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
    # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    # Методы:
    # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом отнимается от здоровья
    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.
    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # поднять щит/опустить щит) на выбранную им цель

    def __init__(self, name):
        super().__init__(name)
        self.__defense = 1
        self.shield_up = False

    def __str__(self):
        return (
            "Я - {name} ({class_type}), уровень здоровья - {hp}, "
            "уровень сил - {power}, щит поднят {shield}".format(
                name=self.name,
                class_type=self.__class__.__name__,
                hp=round(self.get_hp(), 2),
                power=round(self.get_power(), 2),
                shield=self.shield_up,
            )
        )

    def get_defense(self):
        return self.__defense

    def set_defense(self, new_def):
        self.__defense = new_def

    def attack(self, target):
        target.take_damage(round(self.get_power() / 2, 2))

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - round(damage / self.get_defense(), 2))
        super().take_damage(damage)

    def raise_shield(self):
        if self.shield_up == False:
            self.set_defense(self.get_defense() * 2)
            self.set_power(round(self.get_power() / 2, 2))
            self.shield_up = True

    def lower_shield(self):
        if self.shield_up == True:
            self.set_defense(round(self.get_defense() / 2, 2))
            self.set_power(self.get_power() * 2)
            self.shield_up = False

    def take_heal(self, heal):
        self.set_hp(self.get_hp() + heal)
        print(
            "\t",
            self.name,
            "Получил лечение равное = ",
            round(heal),
            ". Уровень здоровья - ",
            round(self.get_hp()),
        )

    def make_a_move(self, friends: list, enemies: list):
        enemies_hp = [enemy.get_hp() for enemy in enemies]

        if self.get_hp() > 100 and self.shield_up:
            self.lower_shield()
            print("Опускаю Щит")
        elif self.get_hp() < 70 and not (self.shield_up):
            self.raise_shield()
            print("Поднимаю Щит")
        else:
            target = enemies[enemies_hp.index(min(enemies_hp))]
            self.attack(target)
        super().make_a_move(friends, enemies)


class Attacker(Hero):
    # Убийца:
    # Атрибуты:
    # - коэффициент усиления урона (входящего и исходящего)
    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона (self.power_multiply)
    # после нанесения урона - вызывается метод ослабления power_down.
    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона - damage * (
    # self.power_multiply / 2)
    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # усиление, ослабление) на выбранную им цель

    def __init__(self, name):
        super().__init__(name)
        self.__power_multiply = 1

    def __str__(self):
        return (
            "Я - {name} ({class_type}), уровень здоровья - {hp}, "
            "уровень сил - {power}".format(
                name=self.name,
                class_type=self.__class__.__name__,
                hp=round(self.get_hp(), 2),
                power=round(self.get_power(), 2),
            )
        )

    def get_multiply(self):
        return self.__power_multiply

    def set_multiply(self, new_multy):
        self.__power_multiply = new_multy

    def attack(self, target):
        target.take_damage(self.get_power() * self.get_multiply())
        self.power_down()

    def power_up(self):
        self.set_multiply(self.get_multiply() * 2)
        print(
            "\tКоэффициент усиления увеличен вдвое = {}".format(
                self.get_multiply(),
            ),
        )

    def power_down(self):
        self.set_multiply(round(self.get_multiply() / 2, 2))
        print(
            "\tКоэффициент усиления уменьшен вдвое = {}".format(
                self.get_multiply(),
            ),
        )

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage * (round(self.__power_multiply / 2, 2)))
        super().take_damage(damage)

    def take_heal(self, heal):
        self.set_hp(self.get_hp() + heal)
        print(
            "\t",
            self.name,
            "Получил лечение равное = ",
            round(heal),
            ". Уровень здоровья - ",
            round(self.get_hp()),
        )

    def make_a_move(self, friends: list, enemies: list):
        enemies_hp = [enemy.get_hp() for enemy in enemies]
        if self.get_hp() > 100 and self.get_multiply() < 2:
            self.power_up()
        elif self.get_multiply() >= 4:
            target = enemies[enemies_hp.index(max(enemies_hp))]
            self.attack(target)
        elif self.get_hp() < 50 and self.get_multiply() >= 1:
            self.power_down()
        else:
            target = enemies[enemies_hp.index(min(enemies_hp))]
            self.attack(target)
        super().make_a_move(friends, enemies)


# tank = Tank("Танк Пётр")
# attacker = Attacker("Убийца Ольга")
# second_attacker = Attacker("Убийца Траур")
# healer = Healer("Монах Игнат")
# second_healer = Healer("Монах Ирэна")
# good_team = [tank, attacker, second_attacker, second_healer, healer]
#
# friend_hp = [friend.get_hp() for friend in good_team]
# print(friend_hp)
