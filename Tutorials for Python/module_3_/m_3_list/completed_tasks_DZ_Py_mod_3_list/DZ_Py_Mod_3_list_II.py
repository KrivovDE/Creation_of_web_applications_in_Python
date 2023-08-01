# Задание 1
# Два списка целых заполняются случайными числами.
# Необходимо:
# ■ Сформировать третий список, содержащий элементы обоих списков;
# ■ Сформировать третий список, содержащий элементы обоих списков без повторений;
# ■ Сформировать третий список, содержащий элементы общие для двух списков;
# ■ Сформировать третий список, содержащий только уникальные элементы каждого из списков;
# ■ Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.

lst_first = [1, 9, 4, 15, 94, 33, 12]
lst_second = [4, 33, 52, 94, 31, 58, 33]
lst_third_all = lst_first + lst_second  # элементы обоих списков
lst_third_norepeat = []  # обоих списков без повторений
lst_third_general = []  # общие для двух списков
lst_third_unicum = []  # уникальные элементы
lst_third_max_min = [
    min(lst_first),
    max(lst_first),
    min(lst_second),
    max(lst_second),
]  # минимальное и максимальное значение
for i in lst_third_all:
    if i not in lst_third_norepeat:
        lst_third_norepeat.append(i)
    elif i not in (lst_third_norepeat and lst_third_general):
        lst_third_general.append(i)
    if lst_third_all.count(i) == 1:
        lst_third_unicum.append(i)
print(
    f"Содержит элементы обоих списков: {lst_third_all}\n"
    f"Элементы обоих списков без повторений:{lst_third_norepeat}\n"
    f"Элементы общие для двух списков: {lst_third_general}\n"
    f"Только уникальные элементы: {lst_third_unicum}\n"
    f"Tолько минимальное и максимальное значение: {lst_third_max_min}",
)

# Задание 2
# В списке целых, заполненном случайными числами вычислить:
# ■ Сумму отрицательных чисел;
# ■ Сумму четных чисел;
# ■ Сумму нечетных чисел;
# ■ Произведение элементов с индексами кратными 3;
# ■ Произведение элементов между минимальным и максимальным элементом;
# ■ Сумму элементов, находящихся между первым и последним положительными элементами.

import random

lst_full = [random.randint(-100, 100) for i in range(10)]
lst_sum_negative = 0  # Сумму отрицательных чисел
lst_sum_even = 0  # Сумму четных чисел
lst_sum_uneven = 0  # Сумму нечетных чисел
lst_piece_for3 = 1  # с индексами кратными 3
index = []  # запись индексов положительных чисел

for i in range(len(lst_full)):
    if lst_full[i] < 0:
        lst_sum_negative += lst_full[i]
    else:
        index += [i]
    if lst_full[i] % 2 == 0:
        lst_sum_even += i
    else:
        lst_sum_uneven += i
    if i % 3 == 0:
        lst_piece_for3 *= lst_full[i]

lst_piece_min_max = min(lst_full) * max(
    lst_full
)  # между минимальным и максимальным элементом
lst_between_positive = lst_full[index[0] + 1 : index[-1]]  # между первым и последним

print(
    f"Полный список: {lst_full}\n"
    f"Cумма отрицательных чисел: {lst_sum_negative}\n"
    f"Сумма четных чисел: {lst_sum_even}\n"
    f"Сумма не четных чисел: {lst_sum_uneven}\n"
    f"Произведение чисел с индексом кратных 3м: {lst_piece_for3}\n"
    f"Произведение минимального и максимального числа: {lst_piece_min_max}\n"
    f"Промежуток между положительными числами: {lst_between_positive}\n"
    f"Сумма промежутка между положительными числами: "
    f"{sum(lst_between_positive)}\n",
)


# Задание 3
# Есть список целых, заполненный случайными числами. На основании данных этого массива нужно:
# ■ Создать список целых, содержащий только четные числа из списка;
# ■ Создать список целых, содержащий только нечетные числа из списка;
# ■ Создать список целых, содержащий только отрицательные числа из списка;
# ■ Создать список целых, содержащий только положительные числа из списка.

import random

lst_full = [random.randint(-100, 100) for i in range(10)]
even, uneven, positive, negative = [], [], [], []
for i in lst_full:
    if i % 2 == 0:
        even.append(i)
    else:
        uneven.append(i)
    if i > 0:
        positive.append(i)
    else:
        negative.append(i)
print(
    f"Четные: {even}\nНе четные: {uneven}\nПоложительные: {positive}\n"
    f"Отрицательные: {negative}",
)
