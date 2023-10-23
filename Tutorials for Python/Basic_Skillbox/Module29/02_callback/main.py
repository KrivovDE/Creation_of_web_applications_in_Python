# TODO здесь писать код

from functools import wraps
from typing import Callable, Any

app = dict()


def CallBack(route: str) -> Callable:
    """ Декоратор функции обратного вызова """

    def out_wrapper(func: Callable) -> Callable:
        app[route] = func

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return func(*args, **kwargs)

        return wrapper

    return out_wrapper


@CallBack('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

# зачтено
