# ---------------------------------------------------
# def summ(*elements):
#     #здесь эти элементы автоматически упакуются в кортеж
#     result = 0
#     for element in elements:
#         result += element
#
#     return result
#
#
# print(summ(1, 2, 3))
# #
# print(summ(1, 2, 3, 122, 5000, 10, -1, -5434))

# # ---------------------------------------------------
# def fun(*args):
#
#     print(args[0])
#     print(args)
#
# fun("Python", "C++", "Java", "C#", 55, 898)
# ---------------------------------------------------
# def print_scores(student, *args):
#    print(f'Student Name: {student}')
#
#    for score in args:
#       print(score)
#
# print_scores('DMITRII', 100, 95, 88, 92, 99)

# ---------------------------------------------------
#
# def print_pet_names(owner, **pets):
#     print(f'Имя владельца: {owner}')
#
#     print(pets)
#
#     for pet, name in pets.items():
#         print(f'{pet}: {name}')
#
#
# print_pet_names('ДМИТРИЙ', dog='Рекс', cats=['Васька', 'Белка', 'Машка'], snake='Питон')

# ---------------------------------------------------
# ЗАМЫКАНИЕ

# def outer():  # внешняя функция
#     n = 5  # лексическое окружение - локальная переменная
#
#     def inner():  # локальная функция
#         nonlocal n
#         n += 1  # операции с лексическим окружением
#         print(n)
#
#     return inner
#
# fn = outer()  # fn = inner, так как функция outer возвращает функцию inner
# # вызываем внутреннюю функцию inner
# fn()  # 6
# fn()  # 7
# fn()  # 8
# ---------------------------------------------------
# def multiply(n):
#     def inner(m):
#         return n * m
#     return inner
#
#
# fn = multiply(5)
# print(fn(5))  # 25
# print(fn(6))  # 30
# print(fn(7))  # 35
#
#
# def multiply(n):
#     return lambda m: n * m

#
# fn = multiply(5)
# print(fn(5))  # 25
# print(fn(6))  # 30
# print(fn(7))  # 35

# ---------------------------------------------------
# ПРИМЕР ИСПОЛЬЗОВАНИЯ ЗАМЫКАНИЯ

# def counter(start=0):
#     def step():
#         nonlocal start
#         start += 1
#         return start
#
#     return step
#
#
# c1 = counter(10)
# c2 = counter()
#
# print(c1(), c2())
# print(c1(), c2())
# print(c1(), c2())
#
# # ---------------------------------------------------
# def strip_string(strip_chars=' '):
#     def do_strip(string):
#         return string.strip(strip_chars)
#
#     return do_strip
#
# strip1 = strip_string()
# strip2 = strip_string(" !?,.;")
#
# print(strip1(" hello python!..  "))
# print(strip2(" hello python!..  "))

# ---------------------------------------------------

# Алгоритм Евклида
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print(get_nod(1,5))
# ---------------------------------------------------
import time


def test_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        stop = time.time() - start
        print(f"Время работы: {stop} сек")
    return wrapper

test1 = test_time(get_nod)
test1(1000000000, 2)



# ---------------------------------------------------
# def get_nod(a, b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
#
# print(get_nod(1,5))
# # Быстрый алгоритм Евклида
# def get_fast_nod(a, b):
#     if a < b:
#         a, b = b, a
#     while b:
#         a, b = b, a % b
#     return a
# print(get_fast_nod(1,5))
#
# def test_time(fn, *args):
#     st = time.time()
#     fn(*args)
#     dt = time.time() - st
#     print(f"Время работы: {dt} сек")
#
#
# test1 = test_time(get_nod,100000, 2)
# test2 = test_time(get_fast_nod,100000, 2)
# #
# test1()
# test2()

# ---------------------------------------------------
# import time
#
# def test_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         stop = time.time() - start
#         print(f"Время работы: {stop} сек")
#     return wrapper
# #
# @test_time
# def get_fast_nod(a, b):
#     if a < b:
#         a, b = b, a
#     while b:
#         a, b = b, a % b
#     return a
#
# get_fast_nod(100000000000, 2)
#
# # ---------------------------------------------------
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

# ---------------------------------------------------
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

# ---------------------------------------------------
# На вход программы поступает строка из целых чисел, записанных через пробел. Напишите функцию get_list,
# которая преобразовывает эту строку в список из целых чисел и возвращает его. Определите декоратор для этой функции,
# который сортирует список чисел по возрастанию. Результат сортировки должен возвращаться при вызове декоратора.
# Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst
# s = input()
#
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
# lst = get_list(s)
# print(*lst)
#
# a, b = input(), input()


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



# Пример который можно переделать
# import time

# inp = 'd:\\text.txt'
#
# unique = list()
# remove_index = list()
# hashes = set()
#
# with open(inp, 'r', encoding="utf-8") as fp:
#     data = fp.read()
#
#     start_time = time.time()
#
#     for ln_index, ln in enumerate(data.split('\n', )):
#
#         if ln not in hashes:
#             hashes.add(ln)
#             unique.append(ln)
#         else:
#             remove_index.append(ln_index)
#
#     print("---Выполнено за %s секунд ---" % (time.time() - start_time))
