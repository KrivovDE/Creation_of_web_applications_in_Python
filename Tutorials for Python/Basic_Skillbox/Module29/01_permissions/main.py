# TODO здесь писать код

from functools import wraps
from typing import Callable, Any

user_permissions = ['admin']


def check_permission(user: str) -> Callable:
    """ Декоратор с одним обязательным аргументом"""

    def out_wrapper(orig_func: Callable) -> Callable:
        @wraps(orig_func)
        def wrapper(*args, **kwargs) -> Any:
            if user in user_permissions:
                return orig_func(*args, **kwargs)
            else:
                raise PermissionError('У пользователя недостаточно прав, '
                                      'чтобы выполнить функцию {name}'.format(
                    name=orig_func.__name__))

        return wrapper

    return out_wrapper


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()

# зачтено
