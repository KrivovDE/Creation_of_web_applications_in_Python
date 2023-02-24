# Алгоритм Евклида
# def get_nod(a, b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
#
# print(get_nod(1,5))
#---------------------------------------------------
# import time
#
#
# def test_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         stop = time.time() - start
#         print(f"Время работы: {stop} сек")
#     return wrapper


# test1 = test_time(get_nod)
# test1(100000, 2)

#---------------------------------------------------
# def test_time(fn, *args):
#     st = time.time()
#     fn(*args)
#     dt = time.time() - st
#     print(f"Время работы: {dt} сек")
#
#
# test_time(get_nod, 100000, 2)

#---------------------------------------------------
# Быстрый алгоритм Евклида
# def get_fast_nod(a, b):
#     if a < b:
#         a, b = b, a
#     while b:
#         a, b = b, a % b
#     return a
#
#
# test1 = test_time(get_nod)
# test2 = test_time(get_fast_nod)
#
# test1(100000, 2)
# test2(100000, 2)

#---------------------------------------------------
# import time
# def test_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         stop = time.time() - start
#         print(f"Время работы: {stop} сек")
#     return wrapper
#
# @test_time
# def get_fast_nod(a, b):
#     if a < b:
#         a, b = b, a
#     while b:
#         a, b = b, a % b
#     return a
#
# get_fast_nod(1000, 2)

#---------------------------------------------------
# def test_time(fn):
#     def wrapper(*args, **kwargs):
#         st = time.time()
#         res = fn(*args, **kwargs)
#         dt = time.time() - st
#         print(f"Время работы: {dt} сек")
#         return res
#     return wrapper
#
# res = get_fast_nod(100000,2)
# print( res )

#---------------------------------------------------
# Объявите функцию с именем get_sq, которая вычисляет площадь прямоугольника по двум параметрам:
# width и height - ширина и высота прямоугольника. И возвращает результат.
# Определите декоратор func_show для этой функции, который отображает результат на экране в виде строки (без кавычек):

# def func_show(func):
#     def show_text(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(f"Площадь прямоугольника: {res}")
#     return show_text
#
#
# def get_sq(width, height):
#     sq = width * height
#     return sq
#
# z = func_show(get_sq)
# z(8, 11)

#---------------------------------------------------
# На вход программы поступает строка из целых чисел, записанных через пробел. Напишите функцию get_list,
# которая преобразовывает эту строку в список из целых чисел и возвращает его. Определите декоратор для этой функции,
# который сортирует список чисел по возрастанию. Результат сортировки должен возвращаться при вызове декоратора.
# Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst
# s = input()

# def get_sort(func):
#     def wrapper(s):
#         res = sorted(func(s))
#         return res
#     return wrapper
#
#
# @get_sort
# def get_list(s):
#     s = list(map(int, s.split()))
#     return s
#
#
# lst = get_list(s)
# print(*lst)

# a, b = input(), input()
#
#
# def get_decor(func):
#     def get_dict(a, b):
#         c = list(zip(*func(a, b)))
#         return c
#
#     return get_dict
#
#
# @get_decor
# def get_list(a, b):
#     return a.split(), b.split()
#
#
# d = get_list(a, b)
# print(d)




