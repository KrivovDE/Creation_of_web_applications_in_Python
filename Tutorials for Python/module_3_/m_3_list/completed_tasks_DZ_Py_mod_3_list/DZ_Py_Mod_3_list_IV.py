# Задание 1
# Два списка целых заполняются случайными числами.
# Необходимо:
# ■ Сформировать третий список, содержащий элементы обоих списков;
# ■ Сформировать третий список, содержащий элементы обоих списков без повторений;
# ■ Сформировать третий список, содержащий элементы общие для двух списков;
# ■ Сформировать третий список, содержащий только уникальные элементы каждого из списков;
# ■ Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.
#
a = [-1, 0, 5, -53, 100, 33, 6]
b = [666, -100, 100, 0, 23, 33]
f = a + b
print("Cписок, содержащий элементы обоих списков: ", f)
print("Список, содержащий элементы обоих списков без повторений: ", sorted(set(f)))
print("Cписок, содержащий элементы общие для двух списков: ", list(set(a) & set(b)))
print(
    "Cписок, содержащий только уникальные элементы каждого из списков: ",
    list(set(a) | set(b)),
)
print(
    "Cписок, содержащий только минимальное и максимальное значение каждого из списков: ",
    [min(a), min(b), max(a), max(b)],
)

#
# Задание 2
# В списке целых, заполненном случайными числами вычислить:
# ■ Сумму отрицательных чисел;
# ■ Сумму четных чисел;
# ■ Сумму нечетных чисел;
# ■ Произведение элементов с индексами кратными 3;
# ■ Произведение элементов между минимальным и максимальным элементом;
# ■ Сумму элементов, находящихся между первым и последним положительными элементами.

a = [-1, 0, 5, -53, 100, 33, 6]
sum_negative = sum([_ for _ in a if _ < 0])
sum_even = sum([_ for _ in a if _ % 2 == 0])
sum_odd = sum([_ for _ in a if _ % 2 != 0])
mult_3 = sum([_ for _ in range(0, len(a), 3)])
mult_min_max = sum([a[_] for _ in range(a.index(min(a)), a.index(max(a)) + 1)])
sum_first_last_positive = sum(
    [
        a[_]
        for _ in range(
            a.index([_ for _ in a if _ > 0][0]) + 1,
            a.index([_ for _ in a if _ > 0][-1]),
        )
    ],
)

print(
    f"Сумма отрицательных чисел: {sum_negative}",
    f"Сумма четных чисел: {sum_even}",
    f"Сумма нечетных чисел: {sum_odd}",
    f"Произведение элементов с индексами кратными 3: {mult_3}",
    f"Произведение элементов между минимальным и максимальным элементом: {mult_min_max}",
    f"Сумма элементов, находящихся между первым и последним положительными элементами: {sum_first_last_positive}",
    sep="\n",
)

#
# Задание 3
# Есть список целых, заполненный случайными числами. На основании данных этого массива нужно:
# ■ Создать список целых, содержащий только четные числа из списка;
# ■ Создать список целых, содержащий только нечетные числа из списка;
# ■ Создать список целых, содержащий только отрицательные числа из списка;
# ■ Создать список целых, содержащий только положительные числа из списка.

a = [-1, 0, 5, -53, 100, 33, 6]
even_list = [_ for _ in a if _ % 2 == 0]
odd_list = [_ for _ in a if _ % 2 != 0]
negative_list = [_ for _ in a if _ < 0]
positive_list = [_ for _ in a if _ > 0]
print(even_list)
print(odd_list)
print(negative_list)
print(positive_list)
