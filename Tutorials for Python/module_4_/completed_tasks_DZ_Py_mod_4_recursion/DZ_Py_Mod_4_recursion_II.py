# Задание 1
# Написать рекурсивную функцию нахождения степени числа.

# def func_rec(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * func_rec(x, n - 1)
#
#
# print(func_rec(int(input('Enter number: ')), int(input('Enter degree: '))))

# Задание 2
# Написать рекурсивную функцию, которая вычисляет сумму всех чисел в диапазоне от a до b. Пользователь вводит a и b.
# Проиллюстрируйте работу функции примером.

# def sum_rec(a, b):
#     if a > b:
#         a, b = b, a
#
#     return b if a == b else a + sum_rec(a + 1, b)
#
#
# print(sum_rec(int(input('Enter number 1: ')), int(input('Enter number 2: '))))

# Задание 3
# Написать рекурсивную функцию, которая выводит N звезд в ряд, число N задает пользователь.
# Проиллюстрируйте работу функции примером.

# def func_rec(n):
#     if n == 0:
#         return
#     else:
#         print('*', end='')
#         func_rec(n-1)
#
#
# func_rec(int(input('Enter N: ')))

# Задание 4*
# Напишите рекурсивную функцию, которая принимает список из 100 целых чисел, полученных случайным образом,
# и находит позицию, с которой начинается последовательность из 10 чисел, сумма которых минимальна.

# Для упрощения проверки изменил длину списка на 20, а последовательности на 3. Числа от 0 до 10.

# import random
#
#
# def func_rec(lst, start_pos=0):
#     if len(lst) == 3:
#         min_pos = 17
#         return min_pos, sum(lst)
#
#     sum1 = sum(lst[start_pos:3])
#     min_pos, sum2 = func_rec(lst[start_pos + 1:])
#
#     if sum1 <= sum2:
#         min_pos = 20 - len(lst[start_pos:])
#         return min_pos, sum1
#     else:
#         return min_pos, sum2
#
#
# lst1 = [random.randint(0, 10) for x in range(20)]
# print(f'Список случайных чисел: {lst1}',
#       f'Наименьшая сумма 3 чисел подряд: {func_rec(lst1)[1]}',
#       f'Индекс начала последовательности: {func_rec(lst1)[0]}', sep='\n')

# Задание 5**
# Написать функцию, которая принимает две даты (т.е. функция принимает шесть параметров) и вычисляет разность
# в днях между этими датами. Для решения этой задачи необходимо также написать функцию, которая определяет,
# является ли год високосным.

# date1 = list(map(int, input("Введите первую дату (более раннюю) в формате дд.мм.гг: ").split('.')))
# date2 = list(map(int, input("Введите вторую дату (более позднюю) в формате дд.мм.гг: ").split('.')))
# day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#
# # високосный или нет год
# def leap_year(y):
#     if y % 400 == 0:
#         return True
#     elif y % 4 == 0 and y % 100 != 0:
#         return True
#     else:
#         return False
#
#
# # считает дни прошедшие с начала года
# def day_gone_by(d, m, y):
#     count = d
#     count += sum(day_in_month[:m - 1])
#     if leap_year(y) and m > 2:
#         count += 1
#     return count
#
#
# def count_days(dd1, mm1, yy1, dd2, mm2, yy2):
#     dif = 0
#     # считаем дни в целых годах между датами
#     if yy2 - yy1 > 1:
#         for i in range(yy1 + 1, yy2):
#             dif += 366 if leap_year(i) else 365
#     # считаем разницы между днями без учета полных лет между ними
#     if yy2 - yy1 == 1:
#         dif += 365 - day_gone_by(dd1, mm1, yy1) + day_gone_by(dd2, mm2, yy2)
#     elif yy2 == yy1:
#         dif += day_gone_by(dd2, mm2, yy2) - day_gone_by(dd1, mm1, yy1)
#     return dif
#
#
# print(count_days(date1[0], date1[1], date1[2], date2[0], date2[1], date2[2]))
