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



#---------------------------------------------------




#---------------------------------------------------





