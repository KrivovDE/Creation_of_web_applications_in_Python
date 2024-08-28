# TODO здесь писать код

from datetime import datetime
from functools import wraps
from typing import Callable


def logging(func: Callable) -> Callable:
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            with open("function_errors.log", "a", encoding="utf-8") as log_file:
                log_file.write(
                    "{time}: Функция - {func_name}, "
                    "завершилось ошибкой - {error} \n\t"
                    "Документация: {doc}\n".format(
                        func_name=func.__name__,
                        time=datetime.now(),
                        error=TypeError,
                        doc=func.__doc__,
                    ),
                )

    return wrapped_func


@logging
def say_hi_1(name: str) -> None:
    """Функция приветствует пользователя"""
    print(f"Привет, {name}")


@logging
def say_hi_2(name: str) -> None:
    """Функция приветствует пользователя и делит стоку на число"""
    print(f"Привет, {name}")
    "b0" / 2


@logging
def say_hi_3(name: str) -> None:
    """Функция приветствует пользователя и округляет строку"""
    round("b0", 2)
    print(f"Привет, {name}")


say_hi_1("Valyera")
say_hi_2("Ivan")
say_hi_3("Kostya")

# зачтено
