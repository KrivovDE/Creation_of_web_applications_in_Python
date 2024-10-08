# Задание 1
# Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа.
# Функция принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.


def square(sym, n, filled=True):
    line = n * sym
    if filled:
        for i in range(n):
            print(line)
    else:
        print(line)
        for i in range(n - 2):
            print(sym + " " * (n - 2) + sym)
        print(line)


square("*", 10, True)


#
# Задание 2
# Напишите функцию, которая возвращает произведение чисел в указанном диапазоне.
# Границы диапазона передаются в качестве параметров.
# Если границы диапазона перепутаны (например, 5 — верхняя граница, 25 — нижняя граница), их нужно поменять местами.
#
def proizv(a, b):
    if a == b:
        return "Диапазон введен неверно."
    if a > b:
        a, b = b, a
    res = 1
    for i in range(a, b + 1):
        res *= i
    return res


print(
    proizv(
        int(input("Введите нижняя граница: ")),
        int(input("Введите вверхнюю границу: ")),
    ),
)
# print(proizv(2, 5))

#
# Задание 3
# Напишите функцию, которая считает количество цифр в числе. Число передаётся в качестве параметра.
# Из функции нужно вернуть полученное количество цифр. Например, если передали 3456, количество цифр будет 4.
#
def digit_number(x):
    res = 0
    for i in range(len(str(x))):
        res += 1
    return res


print(f"Количество цифр", digit_number(1234))

#
# Задание 4
# Напишите функцию, которая проверяет является ли число палиндромом. Число передаётся в качестве параметра.
# Если число палиндром нужно вернуть из функции true, иначе false.
# «Палиндром» — это число, у которого первая часть цифр равна второй перевернутой части цифр.
# Например, 123321 — палиндром (первая часть 123, вторая 321, которая после переворота становится 123),
# 546645 — палиндром, а 421987 — не палиндром.


def polindrom(x):
    """

    :param x:
    :return:
    """
    compil = "".join(reversed(str(x)))
    return str(x) == str(compil)


num = 1221
if polindrom(num):
    print("Число ", num, "- полиндром.")
else:
    print("Число ", num, "- не полиндром.")

# Задание 5
# Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа.
# Функция принимает в качестве параметра: длину линии, направление, символ.
# #
def line(leng, nap, sim):
    _end = "" if nap else "\n"

    for i in range(leng):
        print(sim, end=_end)


line(5, True, "#")
line(4, False, "!")
