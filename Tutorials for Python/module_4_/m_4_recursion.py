# def func_rec(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * func_rec(x, n-1)
#
#
# print(func_rec(2, 3))
#---------------------------------------------------

# N = int(input())
#
#
# def get_rec_N(N):
#     if N > 1:
#         get_rec_N(N-1)
#     print(N)
#
# get_rec_N(N)
#---------------------------------------------------


# def show_elements(lst, func):
#     for x in lst:
#         if func(x):
#             print(x)
#
#
# def _odd(x):
#     return True if x % 2 != 0 else False
#
#
# a = [1, 2, 3, 4, 5, 6, 7]
# show_elements(a, _odd)
#
# show_elements(a, lambda x: True if x % 2 == 0 else False)

#---------------------------------------------------
# Подвиг 1.

# n = int(input())
#
#
# def fact_rec(n):
#     if n > 1:
#         return n * fact_rec(n-1)
#     return 1
#
#
# print(fact_rec(n))
#
#
#
# def fact_rec_2(n):
#     return n * fact_rec_2(n-1) if n else 1
#
#
# print(f' -------{fact_rec_2(n)}')
#---------------------------------------------------
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
#
# lst = list(map(int, input().split()))
# print(get_rec_sum(lst))
#---------------------------------------------------

# get_sq = lambda x: x ** 2
# get_div = lambda x, y: None if y == 0 else x / y
# a = lambda x: abs(x)
#---------------------------------------------------
# def my_func(b):
#     for x in range(b):
#         n = x + 1
#         print(n, end=" ")
#
#
# my_func(6)
#---------------------------------------------------
# name = "Tom"
#
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
#---------------------------------------------------
# x = 0
#
#
# def outer():
#     x = 1
#
#     def inner():
#         x = 2
#         print("inner:", x)
#
#     inner()
#     print("outer:", x)
#
#
# outer()
# print("global:", x)


