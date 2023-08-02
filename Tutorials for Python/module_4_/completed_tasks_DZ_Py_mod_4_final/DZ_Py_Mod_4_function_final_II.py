# 1РАЗ необязательные и именованные аргументы
# Напишите функцию matrix(), которая создает, заполняет и возвращает
# матрицу заданного размера. При этом (в зависимости от переданных аргументов)
# она должна вести себя так:
# def matrix(n=1, m=1, value=9):
#     return [[value for i in range(m)] for i in range(n)]
#
#
# print(matrix(3, 4, 9))

# 2РАЗ функции с переменным количеством аргументов
# Напишите функцию count_args(), которая принимает произвольное количество
# аргументов и возвращает количество переданных в нее аргументов.


# def count_args(*args):
#     return len(args)
#
#
# print(count_args([], (''), 'a', 12, False))
# print(count_args())

# 3РАЗфункции с переменным количеством аргументов
# Напишите функцию sq_sum(), которая принимает произвольное количество
# числовых аргументов и возвращает сумму их квадратов.
# Примечание 1. Обратите внимание, что функция должна принимать не список,
# а именно произвольное количество аргументов.

# def sq_sum(*args):
#     return sum(list(map(lambda x: x**2, args)))
#     # Пробовал через reduce, не получается
#
#
# print(sq_sum())
# print(sq_sum(1, 2, 3))
# print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# 4РАЗ функции с переменным количеством аргументов
# Напишите функцию greet(), которая принимает произвольное количество
# аргументов строк имен (как минимум одно) и возвращает приветствие
# в соответствии с образцом.

# def greet(name, *args):
#     return f'Hello, {name} {" and ".join(args)}!'
#
#
# print(greet('Timur', 'Roman', 'Ruslan'))

# 5РАЗ функции с переменным количеством аргументов
# Напишите функцию info_kwargs(), которая принимает произвольное количество
# именованных аргументов и печатает именованные аргументы в соответствии с
# образцом: <имя аргумента>: <значение аргумента>, при этом имена аргументов
# следуют в алфавитном порядке (по возрастанию).


# def info_kwargs(**kwargs):
#     return '\n'.join(map(lambda x: f'{x[0]}: {x[1]}', sorted(kwargs.items())))
#
#
# print(info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher'))


# 6РАЗ функции как объекты
# Список athletes содержит сведения о спортсменах в виде кортежей:
# (имя, возраст, рост, вес).
# Напишите программу сортировки списка спортсменов по указанному полю:
# 11: по имени;
# 22: по возрасту;
# 33: по росту;
# 44: по весу.

# def func_sort(num, lst):
#     lst.sort(key=lambda x: x[num-1])
#     return '\n'.join(list(map(lambda x: ' '.join(x), [map(str, j) for j in lst])))
#
#
# athletes = [['Дима', 10, 130, 35], ['Тимур', 11, 135, 39],
#             ['Руслан', 9, 140, 33], ['Рустам', 10, 128, 30],
#             ['Амир', 16, 170, 70], ['Рома', 16, 188, 100],
#             ['Матвей', 17, 168, 68], ['Петя', 15, 190, 90]]
# print(func_sort(int(input()), athletes))


# 7РАЗ функции высшего порядка
# Напишите программу, которая с помощью функций filter() и map() отбирает из
# заданного списка numbers трёхзначные числа, дающие при делении на 55 остаток
# 22, и выводит их кубы, каждый в отдельной строке.


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696,
#            1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225,
#            912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027,
#            257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394,
#            560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898,
#            669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207,
#            1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186,
#            273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120,
#            340, 963, 832, 1127]
#
# func1 = lambda x: 99 < x < 999 and x % 5 == 2
# func2 = lambda x: x**2
#
# srt = list(filter(func1, numbers))
# print(*map(func2, srt), sep='\n')

# 8РАЗ анонимные функции
# Требовалось написать программу, которая:
# преобразует список floats в список чисел, возведенных в квадрат и
# округленных с точностью до одного десятичного знака;
# фильтрует список words  и оставляет только палиндромы длиной более 44 символов;
# находит произведение чисел из списка numbers.
# Программист торопился и написал программу неправильно. Доработайте его программу.
# from functools
# # Исправьте этот код
# map_result = list(map(lambda num: num, floats))
# filter_result = list(filter(lambda name: name, words))
# reduce_result = reduce(lambda num1, num2: num1 + num2, numbers, 0)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)

#############################################################################
# ИСПРАВЛЕНИЕ КОДА

# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67,
#           2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic',
#          'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]

# map_result = list(map(lambda num: round(num**2, 1), floats))
# filter_result = list(filter(lambda name: name == name[::-1] and len(name) > 4, words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)

# 9 РАЗ Анонимные функции
# Напишите программу, которая с помощью встроенных функций filter(), map(),
# sorted() и reduce() выводит в алфавитном порядке список primary городов с
# населением более 1000000010000000 человек, в формате:
# Cities: Beijing, Buenos Aires, ...

# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
# filt = sorted(list(filter(lambda x: 'primary' in x and x[1] > 1e7, data)))
# inp = ' ,'.join(list(map(lambda x: x[0], filt)))
# print(inp)


# 10РАЗ
# Напишите функцию is_non_negative_num, используя синтаксис анонимных функций,
# которая принимает строковый аргумент и возвращает значение True, если
# переданный аргумент является неотрицательным числом (целым или вещественным)
# и False в противном случае.
# Примечание 1. Следующий программный код:
# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))
# должен выводить:
# False
# True
# False
# False
# True
# False
# False
# True
# Примечание 2.
# Неотрицательные числа — это положительные числа и число нуль.

# is_non_negative_num = lambda x: x.replace('.', '', 1).isdigit()
# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))

# 11 РАЗ Встроенные функции
#
# Используя параллельную итерацию сразу по трем спискам countries, capitals
# и population выведите информацию о стране в формате:
# <capital> is the capital of <country>, population equal <population> people.
# Moscow is the capital of Russia, population equal 145934462 people.
# Washington is the capital of USA, population equal 331002651 people.
# Для каждой страны информацию выводить на отдельной строке.

# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511,
#               1_380_004_385]
#
# iters = zip(countries, capitals, population)
# info = '\n'.join(list(map(lambda x: f'{x[0]} is the capital of {x[1]} popu'
#                                     f'lation equal {x[2]} people.', iters)))
# print(info)
