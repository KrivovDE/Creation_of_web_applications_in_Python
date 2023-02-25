# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Два списка целых заполняются случайными числами.
# Необходимо:
# ■ Сформировать третий список, содержащий элементы обоих списков;
# ■ Сформировать третий список, содержащий элементы обоих списков
# без повторений;
# ■ Сформировать третий список, содержащий элементы общие для двух списков;
# ■ Сформировать третий список, содержащий только уникальные элементы каждого
# из списков;
# ■ Сформировать третий список, содержащий только минимальное и максимальное
# значение каждого из списков.
#
from random import randint

lst_1 = [randint(-10, 10) for i in range(5)]
lst_2 = [randint(-10, 10) for j in range(5)]

# lst_1 = [6, -1, -8, 2, -2]
# lst_2 = [1, 3, 0, -1, -9]

lst_all = lst_1 + lst_2
lst_cmm = []
lst_uniq = []
lst_min_max = [min(lst_1), max(lst_1), min(lst_2), max(lst_2)]

for digs in lst_all:
    if lst_all.count(digs) >= 2 and lst_cmm.count(digs) < 1:
        lst_cmm.append(digs)
    elif lst_all.count(digs) == 1:
        lst_uniq.append(digs)

print(f'Список 1: {lst_1}\n'
      f'Список 2: {lst_2}\n'
      f'\nСписок, содержащий элементы обоих списков:\n{lst_all}\n\n'
      f'Список без повторений:\n{lst_cmm + lst_uniq}\n\n'
      f'Список, содержащий элементы общие для двух списков:\n{lst_cmm}\n\n'
      f'Список, содержащий только уникальные элементы каждого '
      f'из списков:\n{lst_uniq}\n\n'
      f'Список, содержащий только минимальное и максимальное '
      f'значение каждого из списков:\n{lst_min_max}')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# В списке целых, заполненном случайными числами вычислить:
# ■ Сумму отрицательных чисел;
# ■ Сумму четных чисел;
# ■ Сумму нечетных чисел;
# ■ Произведение элементов с индексами кратными 3;
# ■ Произведение элементов между минимальным и максимальным элементом;
# ■ Сумму элементов, находящихся между первым и последним положительными
# элементами.

from random import randint

lst = [randint(-10, 10) for i in range(7)]

sum_negative = 0
sum_even = 0
sum_odd = 0
mltp_3 = 1
mltp_btw = min(lst) * max(lst)
i1 = None
i2 = 0

for i in range(len(lst)):
    if lst[i] % 2 == 0:
        sum_even += lst[i]
    if lst[i] % 2 != 0:
        sum_odd += lst[i]
    if lst[i] < 0:
        sum_negative += lst[i]
    if i % 3 == 0 and not i == 0:
        mltp_3 *= lst[i]
    if lst[i] > 0:
        if not i1 == None and i > i1:
            i2 = i
            continue
        i1 = i


sum_btw = sum(lst[i1+1:i2])

print(lst)
print(f'Сумма отрицательных чисел: {sum_negative}\n'
      f'Сумма четных чисел: {sum_even}\n'
      f'Сумма нечетных чисел: {sum_odd}\n'
      f'Произведение элементов с индексами кратными 3: {mltp_3}\n'
      f'Произведение элементов между минимальным и '
      f'максимальным элементом: {mltp_btw}\n'
      f'Сумму элементов, находящихся между первым и последним положительными'
      f' элементами: {sum_btw}\n')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Есть список целых, заполненный случайными числами.
# На основании данных этого массива нужно:
# ■ Создать список целых, содержащий только четные числа из списка;
# ■ Создать список целых, содержащий только нечетные числа из списка;
# ■ Создать список целых, содержащий только отрицательные числа из списка;
# ■ Создать список целых, содержащий только положительные числа из списка.

from random import randint

lst = [randint(-10, 10) for i in range(7)]

lst1 = [i for i in lst if i % 2 == 0]
lst2 = [i for i in lst if i % 2 != 0]
lst3 = [i for i in lst if i < 0]
lst4 = [i for i in lst if i > 0]

print(lst)
print(lst1)
print(lst2)
print(lst3)
print(lst4)