# Задание 1
# Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа.
# Функция принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.


def square(side_length, char, fill):
    if fill:
        print(*[char * side_length for i in range(side_length)], sep="\n")
    else:
        res = [char + " " * (side_length - 2) + char for i in range(side_length - 2)]
        res.append(char * side_length)
        res.insert(0, char * side_length)
        print(*res, sep="\n")


square(5, "#", False)
square(6, "&", True)

# Задание 2
# Напишите функцию, которая возвращает произведение чисел в указанном диапазоне.
# Границы диапазона передаются в качестве параметров. Если границы диапазона перепутаны (например, 5 — верхняя граница,
# 25— нижняя граница), их нужно поменять местами.


def multiply(num1, num2):
    res = 1
    if num1 > num2:
        num1, num2 = num2, num1
    while not num1 > num2:
        res *= num1
        num1 += 1
    return res


print(multiply(int(input("Enter num1: ")), int(input("Enter num2: "))))

# Задание 3
# Напишите функцию, которая считает количество цифр в числе. Число передаётся в качестве параметра.
# Из функции нужно вернуть полученное количество цифр. Например, если передали 3456, количество цифр будет 4.
#
# def quan_digit(num):
#     return len(str(abs(num)))
#
#
# print(quan_digit(int(input('Enter number: '))))

# Задание 4
# Напишите функцию, которая проверяет является ли число палиндромом. Число передаётся в качестве параметра.
# Если число палиндром нужно вернуть из функции true, иначе false.
# «Палиндром» — это число, у которого первая часть цифр равна второй перевернутой части цифр.
# Например, 123321 — палиндром (первая часть 123, вторая 321, которая после переворота становится 123),
# 546645 — палиндром, а 421987 — не палиндром.


def palindrom(num):
    lst1 = [*str(num)]
    lst2 = lst1.copy()
    lst2.reverse()
    return lst1 == lst2


print(palindrom(int(input("Enter number: "))))

# Задание 5
# Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа.
# Функция принимает в качестве параметра: длину линии, направление, символ.


def line(leng, direct, char):
    if direct == "hor":
        print(*[char for i in range(leng)])
    elif direct == "ver":
        print(*[char for i in range(leng)], sep="\n")


quantity = int(input("Enter length of line: "))
direction = input("Choose direction (hor / ver): ")
character = input("Enter symbol: ")

line(quantity, direction, character)
