# Задание 1
# Два списка целых заполняются случайными числами.
# Необходимо:
# ■ Сформировать третий список, содержащий элементы обоих списков;
# ■ Сформировать третий список, содержащий элементы обоих списков без повторений;
# ■ Сформировать третий список, содержащий элементы общие для двух списков;
# ■ Сформировать третий список, содержащий только уникальные элементы каждого из списков;
# ■ Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.

import random

lst1 = random.sample([i for i in range(51)], 10)
lst1.sort()
lst2 = random.sample([i for i in range(51)], 10)
lst2.sort()

lst_sum = lst1 + lst2
lst_sum.sort()
lst_no_repeat = lst_sum.copy()
lst_repeat = [i for i in lst1 if i in lst2]
lst_uniq = [i for i in lst_sum if not lst_sum.count(i) > 1]
lst_min_max = [min(lst1), max(lst1), min(lst2), max(lst2)]

for i in lst_repeat:
    lst_no_repeat.remove(i)

print(f'list 1_________: {lst1}',
      f'list 2_________: {lst2}',
      f'sum list_______: {lst_sum}',
      f'list no repeat_: {lst_no_repeat}',
      f'repeat elements: {lst_repeat}',
      f'uniq elements__: {lst_uniq}',
      f'min-max list___: {lst_min_max}', sep='\n')

# Задание 2
# В списке целых, заполненном случайными числами вычислить:
# ■ Сумму отрицательных чисел;
# ■ Сумму четных чисел;
# ■ Сумму нечетных чисел;
# ■ Произведение элементов с индексами кратными 3;
# ■ Произведение элементов между минимальным и максимальным элементом;
# ■ Сумму элементов, находящихся между первым и последним положительными элементами.

import random

N = random.randint(10, 20)
lst1 = [random.randint(-50, 50) for x in range(N)]
lst1.sort()
print(f' List: {lst1}')

sum_neg = 0
sum_odd = 0
sum_even = 0
mult_ind3 = 1
mult_between = 1
lst_pos = []
sum_between = 0

for i in range(len(lst1)):
    if lst1[i] < 0:
        sum_neg += lst1[i]
    elif lst1[i] > 0:
        lst_pos.append(lst1[i])
    if lst1[i] % 2 == 0:
        sum_even += lst1[i]
    else:
        sum_odd += lst1[i]
    if i % 3 == 0:
        mult_ind3 *= lst1[i]
    if i != 0 and i != (len(lst1) - 1):
        mult_between *= lst1[i]

sum_between = sum(lst_pos[1:len(lst_pos)-2])

print(f' Summ of negative elements: {sum_neg}\n',
      f'Summ of even elements: {sum_even}\n',
      f'Summ of odd elements: {sum_odd}\n',
      f'Multiplication of element with index / 3: {mult_ind3}\n',
      f'Multiplcation of elements between min and max: {mult_between}\n',
      f'Summ of elements between first and last positive: {sum_between}')

# Задание 3
# Есть список целых, заполненный случайными числами. На основании данных этого массива нужно:
# ■ Создать список целых, содержащий только четные числа из списка;
# ■ Создать список целых, содержащий только нечетные числа из списка;
# ■ Создать список целых, содержащий только отрицательные числа из списка;
# ■ Создать список целых, содержащий только положительные числа из списка.

import random

N = random.randint(10, 50)
lst1 = [random.randint(-50, 50) for x in range(N)]
print(f' List: {lst1}')

lst_odd = []
lst_even = []
lst_neg = []
lst_pos = []

for i in lst1:
    if i % 2 == 0:
        lst_even.append(i)
    else:
        lst_odd.append(i)
    if i > 0:
        lst_pos.append(i)
    elif i < 0:
        lst_neg.append(i)
print(f' List of even elements: {lst_even}\n',
      f'List of odd elements: {lst_odd}\n',
      f'List of negative elements: {lst_neg}\n',
      f'List of positive elements: {lst_pos}')

