import time
import timeit
from copy import deepcopy, copy
from timeit import Timer
from functools import partial


# def decor_times(fuu):
#     def wrap(*args, **kwargs):
#         start = time.time()
#         res = fuu(*args, **kwargs)
#         dt = time.time() - start
#         print (f"Время работы: {dt} сек")
#         return res
#     return wrap
#
# @decor_times
# def two_sum(one_number: int, two_number: int):
#     try:
#         print(one_number + two_number)
#     except TypeError:
#         print("Ghjdthnt nbfs lfyys[")
#

# two_sum = decor_times(two_sum)

# two_sum(9, 4)

# timed_run = Timer(partial(two_sum(9, 4))).timeit(number=10000)
# print(timed_run)


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(f"Привет меня зовут {self.name} мне {self.age} лет.")
#
#
# cat1 = Cat("Васька", 6)
#
# d = {}
# d[cat1] = "sidc"
# print(d)


# def foo(dict_num):
#     sorted_k = sorted(dict_num.items(), key=lambda item: item[1])
#     print(sorted_k[0][0], sorted_k[1][0])
#
#
# people = {"Вася": 25, "Петя": 30, "Маша": 20}
#
# foo(people)


