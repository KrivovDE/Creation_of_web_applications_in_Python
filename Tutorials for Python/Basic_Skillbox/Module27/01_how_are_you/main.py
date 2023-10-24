# TODO здесь писать код

from functools import wraps
from typing import Callable


def how_are_you(func: Callable) -> Callable:
    """
    Надоедливый декоратор нытик, задаёт вопросы из вежливости,
    но вне зависимости от ответа будет ныть от своей тяжёлой декораторской доле

    :param func: любая функция
    :return:
    """

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return func(*args, **kwargs)

    return wrapped_func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()

# зачтено
