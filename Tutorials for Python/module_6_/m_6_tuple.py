from typing import Tuple

# # Вариант 1. Если нужны индексы элементов:

#
# numbers_1: Tuple[int, ...] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# for i in range(len(numbers_1)):
#     print(numbers_1[i])
# # ---------------------------------------------------------------------
#
# # Вариант 2. Если индексы не нужны:
# numbers_2: Tuple[int, ...] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# for num in numbers_2:
#     print(num)
# # ---------------------------------------------------------------------
# numbers_3: Tuple[int, ...] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# languages: Tuple[str, ...] = ('Python', 'C++', 'Java')
#
# print(*numbers_3)
# print(*languages, sep='\n')
# ---------------------------------------------------------------------
# print((1, 8) == (1, 8))
# print((1, 8) != (1, 10))
# print((1, 9) < (1, 2))
# print((2, 5) < (6,))
# print(('a', 'bc') > ('a', 'de'))
# # print((7, 5) < ('java', 'python'))     #TypeError: '<' not supported between instances of 'int' and 'str'

# # ---------------------------------------------------------------------
# not_sorted_tuple: Tuple[int, ...] = (34, 1, 8, 67, 5, 9, 0, 23)
# print(not_sorted_tuple)
#
# sorted_tuple = tuple(sorted(not_sorted_tuple))
# print(sorted_tuple)

# ---------------------------------------------------------------------
# notes: Tuple[str, ...] = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
# string1: str = ''.join(notes)
# string2: str = '.'.join(notes)
#
# print(string1)
# print(string2)


# ---------------------------------------------------------------------
# letters: str = 'abcdefghijkl'
# tpl: tuple = tuple(letters)
# print(tpl)


# number = 12345
# tpl = tuple(number)
# print(tpl)    #TypeError: 'int' object is not iterable

# ---------------------------------------------------------------------

# Подвиг 1.
# Вводятся названия городов в одну строку через пробел. На их основе формируется кортеж.
# Если в этом кортеже нет города "Москва", то следует его добавить в конец кортежа.
# Результат вывести на экран в виде строки с названиями городов через пробел.

# city: Tuple[str, ...] = tuple(input().split())
# for i in city:
#     if 'Москва' not in city:
#         city += ('Москва',)
# print(*city)
#
# t: Tuple[str, ...] = tuple(input().split())
# t: Tuple[str, ...] = t + ('Москва',) if 'Москва' not in t else t
# print(*t)
# ---------------------------------------------------------------------

# Подвиг 2.
# Вводятся целые числа в одну строку через пробел. На их основе формируется кортеж.
# Необходимо создать еще один кортеж с уникальными (не повторяющимися) значениями из первого кортежа.
# Результат отобразите в виде списка чисел через пробел.

# n: map = map(int, input().split())
# x: Tuple[int, ...] = tuple()
#
# for i in n:
#     if i not in x:
#         x += (i,)
#     else:
#         continue
# print(*x)
#
# print(*tuple(k for d in [{x: x for x in tuple(map(int, input().split()))}] for k in d.keys()))

# ---------------------------------------------------------------------
# Подвиг 3. Имеется двумерный кортеж, размером 5 x 5 элементов:
# Вводится натуральное число N (N < 5). Необходимо на основе кортежа t сформировать новый аналогичный кортеж t2
# размером N x N элементов. Результат вывести на экран в виде таблицы чисел.

# t: Tuple[tuple, ...] = ((1, 0, 0, 0, 0),
#                         (0, 1, 0, 0, 0),
#                         (0, 0, 1, 0, 0),
#                         (0, 0, 0, 1, 0),
#                         (0, 0, 0, 0, 1))
#
# t2: Tuple[tuple, ...] = ()
# n: int = int(input())

# for i in t[:n]:
#     t2 += (i[:n],)
#
# for i in t2:
#     print(*i)
# -----
# for i in t[:n]:
#     print(*i[:n])