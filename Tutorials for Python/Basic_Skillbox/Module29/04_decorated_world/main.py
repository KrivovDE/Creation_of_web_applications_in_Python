# TODO здесь писать код

from functools import wraps
from typing import Callable


def decorator_with_args_for_any_decorator(basic_dec: Callable) -> Callable:
    def dec_height(*args, **kwargs) -> Callable:
        def dec_wrapper(func: Callable) -> Callable:
            return basic_dec(func, *args, **kwargs)

        return dec_wrapper

    return dec_height


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        print('Переданные Args и Kwargs:', dec_args, dec_kwargs)
        return func(*args, **kwargs)

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)

# зачтено
