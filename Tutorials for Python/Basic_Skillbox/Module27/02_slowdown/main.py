# TODO здесь писать код

from functools import wraps
from time import sleep
from typing import Callable


def delay(func: Callable) -> Callable:
    """
    Декоратор. Задерживает выполнение функции на 5 сек после вызова.
    :param func: Любая функция
    :return: Модифицированная функция
    """

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        print('ща ща ща')
        sleep(5)
        return func(*args, **kwargs)

    return wrapped_func


@delay
def say_hi(name: str):
    print('Привет {name}!'.format(name=name))


say_hi('Иван')

# зачтено
