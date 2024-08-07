# TODO здесь писать код


# def log_methods(format: str) -> Callable:
#     def out_wrapper(orig_func: Callable) -> Callable:
#         @wraps(orig_func)
#         def wrapper(*args, **kwargs) -> None:
#
#             return
#         return out_wrapper
#     return out_wrapper

# def for_all_methods(decorator: Callable) -> Callable:
#     @wraps(decorator)
#     def decorate(cls):
#         for i_method_name in dir(cls):
#             if i_method_name.startswith('__') is False:
#                 cur_method = getattr(cls, i_method_name)
#                 decorated_method = decorator(cur_method)
#                 setattr(cls, i_method_name, decorated_method)
#         return cls
#     return decorate

import time
from datetime import datetime


def timer(cls, func, date_format):
    def wrapped(*args, **kwargs):
        format = date_format
        for sign in format:
            if sign.isalpha():
                format = format.replace(sign, "%" + sign)

        print(
            f"Запускается '{cls.__name__}.{func.__name__}'. "
            f"Дата и время запуска: {datetime.now().strftime(format)}",
        )
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(
            f"Завершение '{cls.__name__}.{func.__name__}', "
            f"время работы = {round(end - start, 3)} сек.",
        )
        return result

    return wrapped


def log_methods(date_format):
    def decorate(cls):
        for method in dir(cls):
            if not method.startswith("__"):
                current_method = getattr(cls, method)
                decorated_method = timer(cls, current_method, date_format)
                setattr(cls, method, decorated_method)
        return cls

    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print("test sum 1")
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num**2 for i_num in range(10000)])
        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num**2 for i_num in range(10000)])
        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

# зачтено
