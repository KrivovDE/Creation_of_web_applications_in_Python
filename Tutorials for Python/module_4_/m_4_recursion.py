# import time
#
# def test_time(fn):
#     def wrapper(*args, **kwargs):
#         st = time.time()
#         fn(*args, **kwargs)
#         dt = time.time() - st
#         print(f"Время работы рекурсии: {dt} сек")
#     return wrapper
#
#
# # @test_time
# def func_2(a, b):
#     return a ** b
#
# # func_2(2, 100)
#
#
# def func_rec(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * func_rec(x, n-1)
#
#
# st = time.time()
# func_rec(2, 997)
# dt = time.time() - st
# print(f"Время работы второй: {dt} сек")

#

# def func_rec(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * func_rec(x, n-1)
#
#
# print(func_rec(2, 3))
# ---------------------------------------------------


N = int(input())


def get_rec_N(N: int):
    if N > 1:
        get_rec_N(N - 1)
    print(N)


get_rec_N(N)
# ---------------------------------------------------


# def show_elements(lst, func):
#     for x in lst:
#         if func(x):
#             print(x)
# #
# #
# def _odd(x):
#     return True if x % 2 != 0 else False
# #
# #
# a = [1, 2, 3, 4, 5, 6, 7]
# show_elements(a, _odd)
# #
# show_elements(a, lambda x: True if x % 2 == 0 else False)

# ---------------------------------------------------
# Подвиг 1.
#
# n = int(input())


# def fact_rec(n):
#     if n > 1:
#         return n * fact_rec(n - 1)
#     return 1
#
#
# print(fact_rec(n))
#
#
# def fact_rec_2(n):
#     return n * fact_rec_2(n - 1) if n else 1
#
#
# print(f" -------{fact_rec_2(n)}")
# ---------------------------------------------------
# Подвиг 2.

# def get_rec_sum(lst):
#     if len(lst) > 0:
#         return lst.pop() + get_rec_sum(lst)
#     return 0
#
#
# lst = list(map(int, input().split()))
# print(get_rec_sum(lst))
#
#
# def get_rec_sum(lst):
#     if len(lst):
#         return lst[0] + get_rec_sum(lst[1:])
#     return 0
#
# #
# lst = list(map(int, input().split()))
# print(get_rec_sum(lst))
# #---------------------------------------------------
# def show_elements(lst, func):
#     for x in lst:
#         if func(x):
#             print(x)


# def __odd(x):
#     return True if x % 2 != 0 else False

# l_1 = lambda x: x % 2 == 0
# l_2 = lambda x: x % 2 != 0
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# show_elements(a, l_1)
# print('----------')
# show_elements(a, l_2)


# show_elements(a, __odd)

# #
# r = lambda a, b: a+b
# print('lambda', r(1, 2))

# show_elements(a, lambda x: x % 2 == 0)

# get_sq = lambda x: x ** 2
# get_div = lambda x, y: None if y == 0 else x / y
# a = lambda x: abs(x)
# ---------------------------------------------------


# def my_func(b):
#     for x in range(b):
#         n = x + 1
#         print(n, end=" ")
#
#
# my_func(6)

# ---------------------------------------------------
# name = "Tom"
# #
#
# def say_hi():
#     print("Hello", name)
#
#
# def say_bye():
#     name = "Bob"
#     print("Good bye", name)
#
#
# say_hi()
# say_bye()
# print(name)
# ---------------------------------------------------
# x = 0
# def outer():
#     global x
#     x = 1
#     def inner():
#         nonlocal x
#         x = 2
#         print("inner:", x)
#     inner()
#     print("outer:", x)
# outer()
# print("global:", x)

# def func_rec(x, n):
#     if n == 0:
#         return 1
#     else:
#         print( x * func_rec(x, n-1))


# func_rec(2, 3)


# def func_num(num):
#
#     if num == 1:
#         print(1)
#     else:
#         print(num)
#         num -= 1
#         func_num(num)
#
#
# func_num(10)
#


# def set_solving(sp_1, sp_2, sp_3):
#
#     x = set(sp_1).intersection(sp_2, sp_3)
#     y = set(sp_1) - set(sp_2).union(sp_3)
#
#     return x, y
#
#     # return (set(sp_1).intersection(sp_2, sp_3), set(sp_1) - set(sp_2).union(sp_3))
#
#
# # def no_set(sp_1, sp_2, sp_3):
# #     dict_len_sp = ({len(sp_1): sp_1, len(sp_2): sp_2, len(sp_3): sp_3})
# #     sp_2_3 = sp_2 + sp_3
# #     result_sp_1 = [num for num in dict_len_sp[min(dict_len_sp)] if num in sp_2 and num in sp_3]
# #     result_sp_2 = [num for num in sp_1 if num not in sp_2_3]
# #     return result_sp_1, result_sp_2
# #
# array_1 = [1, 2, 3, 4]
# array_2 = [2, 4]
# array_3 = [2, 3]
#
# print(set_solving(array_1, array_2, array_3))

#
# for num in range(2):
#     print(f'Задача {num + 1}:')
#     print('Решение без множеств:', *(no_set(array_1, array_2, array_3)[num]))
#     print('Решение с множествами:', *(set_solving(array_1, array_2, array_3)[num]))
#
# def sum_of_values(a, b, c):
#     return a + b + c
#
# values = [1, 2, 3]
# result = sum_of_values(*values)
# print(result)

# def sum_of_values2(*args):
#     return sum(args)
#
# values2 = [1, 2, 3, 5]
# result = sum_of_values2(*values2)
# print(result)

# def print_details(name, age):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#
# details = {"name": "John", "age": 30}
# print_details(**details)
