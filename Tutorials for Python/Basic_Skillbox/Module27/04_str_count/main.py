# TODO здесь писать код

from typing import Callable


def counter(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs):
        count[0] += 1
        print(
            "Функция вызывалась {times} раз(a)".format(
                times=count[0],
            ),
        )
        return func(*args, **kwargs)

    return wrapped_func


count = [0]


@counter
def greeting():
    print("Hello World!")


greeting()
greeting()
greeting()

# зачтено
