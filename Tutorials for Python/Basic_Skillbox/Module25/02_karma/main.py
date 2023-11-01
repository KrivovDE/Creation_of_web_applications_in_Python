# TODO здесь писать код

from random import randint


class KillError(Exception):
    """ Класс нового исключения. Родитель: Exception """
    pass


class DrunkError(Exception):
    """ Класс нового исключения. Родитель: Exception """
    pass


class CarCrashError(Exception):
    """ Класс нового исключения. Родитель: Exception """
    pass


class GluttonyError(Exception):
    """ Класс нового исключения. Родитель: Exception """
    pass


class DepressionError(Exception):
    """ Класс нового исключения. Родитель: Exception """
    pass


class SimLive:
    """
    Базовый класс симуляции жизни.

    __enlightenment_cost (int): кол-во очков необходимых для просветления
    __exception_dict (dict): словарь с ошибками

    Args:
        karma (int): передаётся начальный уровень кармы


    """

    __enlightenment_cost = 500
    __exception_dict = {
        1: KillError(),
        2: DrunkError(),
        3: CarCrashError(),
        4: GluttonyError(),
        5: DepressionError()
    }

    def __init__(self, karma: int = 0):
        self.__karma = karma

    def enlightenment_check(self):
        """
        Проверка на наличие очков кармы для достижения просветления

        :rtype: bool
        """
        return True if self.__karma <= self.__enlightenment_cost else False

    def one_day(self):
        """
        Имитация прожитого дня.
        Увеличивает уровень кармы на случайное кол-во очков от 1 до 7.

        :raise Exception: с вероятностью 1 к 10 вызывает случайную ошибку из
        словаря
        """
        self.__karma += randint(1, 7)
        chance = randint(1, 50)
        if chance <= 5:
            raise self.__exception_dict[chance]

    def show_karma(self):
        """
        Выводит на экран текущий уровень кармы.
        """
        print('Текущий уровень кармы {}'.format(self.__karma))


sim_1 = SimLive()

with open('karma.log', 'w', encoding='utf-8') as log_file:
    while sim_1.enlightenment_check():
        try:
            sim_1.one_day()
        except KillError:
            log_file.write('KillError\n')
        except DrunkError:
            log_file.write('DrunkError\n')
        except CarCrashError:
            log_file.write('CarCrashError\n')
        except GluttonyError:
            log_file.write('GluttonyError\n')
        except DepressionError:
            log_file.write('DepressionError\n')
    else:
        sim_1.show_karma()
        print('Вы достигли просветления!')

# зачтено
