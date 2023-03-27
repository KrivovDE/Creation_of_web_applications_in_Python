# Задание 1
# Написать рекурсивную функцию нахождения степени числа.

# def number_degree_rec(num: int, deg: int) -> int:
#     return 1 if deg == 0 else num * number_degree_rec(num, deg - 1)
#
#
# print(number_degree_rec(2, 3))

# Задание 2
# Написать рекурсивную функцию, которая вычисляет сумму всех чисел в
# диапазоне от a до b. Пользователь вводит a и b.
# Проиллюстрируйте работу функции примером.

# def sum_range_rec(frst: int, scd: int) -> int:
#     if frst > scd:
#         frst, scd = scd, frst
#     return scd if frst == scd else frst + sum_range_rec(frst + 1, scd)
#
#
# print(sum_range_rec(5, 10))

# Задание 3
# Написать рекурсивную функцию, которая выводит N звезд в ряд, число N
# задает пользователь. Проиллюстрируйте работу функции примером.

# def row_rec(n: int) -> str:
#     if n == 1:
#         return '*'
#     else:
#         print('*', end='')
#         return row_rec(n - 1)
#
# print(row_rec(5))

# Задание 4*
# Напишите рекурсивную функцию, которая принимает список из 100 целых чисел,
# полученных случайным образом, и находит позицию, с которой начинается
# последовательность из 10 чисел, сумма которых минимальна.
# import random
# #
# #
# def find_index_rec(lst: list, x=1):
#     if len(lst) == 10:                                     # условие остановки
#         return lst
#     else:
#         rec_lst = find_index_rec(lst[1:])                  # рекурсия по срезам
#         range_sum = lst[:10]                 # первые 10 знач. основного списка
#         rec_lst = rec_lst if sum(rec_lst) < sum(range_sum) else range_sum     # ищет минимальную сумму
#         if len(lst) < 100:
#             return rec_lst                                # возврат из рекурсий
#         else:                             # последний шаг рекурсии, ищем индекс
#             while lst[0:10] != rec_lst:               # режем основной список пока не находим равенство
#                 del lst[0]
#                 x += 1                                      # считаем позицию
#             return f'Позиция - {x}, Список чисел с наименьшей суммой - ' \
#                    f'{rec_lst}, Их сумма - {sum(rec_lst)}'
#
#
# frst_lst = [random.randint(1, 30) for i in range(100)]
# print(frst_lst)
# print(find_index_rec(frst_lst))


# Задание 5**
# Написать функцию, которая принимает две даты (т.е. функция принимает
# шесть параметров) и вычисляет разность в днях между этими датами. Для
# решения этой задачи необходимо также написать функцию, которая определяет,
# является ли год високосным.

###############################################################################
# ВЕРСИЯ С ОГРАНИЧЕНИЕМ МЕЖДУ ДАТАМИ В 999 ДНЕЙ(из за вложенности рекурсии) ###
###############################################################################
# def leap_year(yr: int) -> int:
#     return yr % 4 == 0
#
#
# def cnt_day_rec(day1, mth1, yr1, day2, mth2, yr2):
#     if day1 == day2 and mth1 == mth2 and yr1 == yr2:  # условие остановки
#         return 0
#     else:
#         if mth1 == 12 and day1 == 31:                   # проверяем год
#             day1, mth1 = 1, 1
#             return cnt_day_rec(day1, mth1, yr1 + 1, day2, mth2, yr2) + 1
#         elif (mth1 in [4, 5, 9, 11] and day1 != 30) or \
#                 (mth1 in [1, 3, 6, 7, 8, 10, 12] and day1 != 31) or \
#                 (leap_year(yr1) and mth1 == 2 and day1 != 29) or \
#                 ((not leap_year(yr1)) and mth1 == 2 and day1 != 28):    # проверяем день в зависимости от месяца
#             return cnt_day_rec(day1 + 1, mth1, yr1, day2, mth2, yr2) + 1
#         else:
#             day1 = 1                                # проверяем месяц
#             return cnt_day_rec(day1, mth1 + 1, yr1, day2, mth2, yr2) + 1
#
#
# #ВВОД И ПРОВЕРКА ДАТ
# try:
#     print('Введите дату через пробел (dd mm yy)')
#     d1, m1, y1 = [int(i) for i in input("Дата №1: ").split(' ')]  # Дата1
#     d2, m2, y2 = [int(i) for i in input("Дата №2: ").split(' ')]  # Дата2
#     # НОРМАЛИЗАЦИЯ ДАТ
#     if (y1 > y2) or (m1 > m2 and y1 == y2) or (
#             d1 > d2 and m1 == m2 and y1 == y2):
#         d1, m1, y1, d2, m2, y2 = d2, m2, y2, d1, m1, y1
#     if (d1 or d2) > 31 or (m1 or m2) > 12 or (0 > (y1 or y2)):
#         raise ValueError('Дата введена неверно')
#     print('Разность в днях:', cnt_day_rec(d1, m1, y1, d2, m2, y2))
# except ValueError as err:
#     print(err)
# except RecursionError:
#     print('Дата введена неверно')

##############################################################################
#################### ВЕРСИЯ БЕЗ ОГРАНИЧЕНИЙ МЕЖДУ ДАТАМИ #####################
############ НО КОД ПОЛУЧИЛСЯ БОЛЬШИМ И НАВРЯДЛИ НОРМАЛЬНО ЧИТАЕМЫЕЙ##########

def leap_year(yr: int) -> int:
    return yr % 4 == 0


def cnt_day_rec(day1, mth1, yr1, day2, mth2, yr2):
    thirty, thirty_one = [4, 5, 9, 11], [1, 3, 6, 7, 8, 10, 2]  # месяца с 30 и 31 днями
    # СЧИТАЕМ ГОДЫ
    if yr1 != yr2 and 12 - mth1 >= 12 - mth2:
        dy_yr = yr2 - yr1
        if dy_yr >= 4:  # Если между датами больше 4 лет
            yr1 = yr1 + dy_yr - dy_yr % 4
            cnt_yr = 365 * (dy_yr - dy_yr % 4) + (dy_yr // 4) + 1
        elif leap_year(yr1) and mth1 < 3:  # Високосный год
            cnt_yr, yr1 = 366, yr1 + 1
        else:                               # Не високосный
            cnt_yr, yr1 = 365, yr1 + 1
        return cnt_day_rec(day1, mth1, yr1, day2, mth2, yr2) + cnt_yr
    # СЧИТАЕМ ДНИ И МЕСЯЦЫ
    elif day1 != day2 or mth1 != mth2:
        if mth1 == 12 and day1 == 31:  # увеличиваем год
            day1, mth1, yr1 = 1, 1, yr1 + 1
        elif (mth1 in thirty and day1 != 30) or \
                (mth1 in thirty_one and day1 != 31) or \
                (leap_year(yr1) and mth1 == 2 and day1 != 29) or \
                ((not leap_year(yr1)) and mth1 == 2 and day1 != 28):
            day1 += 1  # увеличиваем дни в зависимости от месяца
        else:
            day1, mth1 = 1, mth1 + 1  # увеличиваем месяц
        return cnt_day_rec(day1, mth1, yr1, day2, mth2, yr2) + 1
    else:                                 #
        return 0


try:
    print('Введите дату через пробел (dd mm yy)')
    d1, m1, y1 = [int(i) for i in input("Дата №1: ").split(' ')]  # Дата1
    d2, m2, y2 = [int(i) for i in input("Дата №2: ").split(' ')]  # Дата2
    # НОРМАЛИЗАЦИЯ ДАТ
    if (y1 > y2) or (m1 > m2 and y1 == y2) or (
            d1 > d2 and m1 == m2 and y1 == y2):
        d1, m1, y1, d2, m2, y2 = d2, m2, y2, d1, m1, y1
    if (d1 or d2) > 31 or (m1 or m2) > 12 or (0 > (y1 or y2)):
        raise ValueError('Дата введена неверно')
    print('Разность в днях:', cnt_day_rec(d1, m1, y1, d2, m2, y2))
except ValueError as err:
    print(err)
except RecursionError:
    print('Дата введена неверно')




