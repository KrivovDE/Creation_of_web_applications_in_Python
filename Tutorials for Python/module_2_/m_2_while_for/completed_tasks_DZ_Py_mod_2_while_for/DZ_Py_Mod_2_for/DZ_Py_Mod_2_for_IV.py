# Задание 1
# Пользователь вводит с клавиатуры два числа.
# показать все числа в указанном диапазоне.
# показать все нечетные числа в указанном диапазоне.
# показать все четные числа в указанном диапазоне.
# показать все числа в указанном диапазоне в порядке убывания.
# показать все нечетные числа в указанном диапазоне.
# посчитать сумму чисел в диапазоне, а также среднеарифметическое.
#
# Если границы диапазона указаны неправильно требуется произвести нормализацию границ.
# Например, пользователь ввел 33 и 13, требуется нормализация после которой начало диапазона станет равно 13,
# а конец 33.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num2 < num1:
    num_temp = num2
    num2 = num1
    num1 = num_temp

res_all_numbers = ""
res_odd_numbers = ""
res_even_numbers = ""
res_reverse_number = ""
res_sum = 0
num_temp = num1

while num_temp < num2 + 1:
    res_all_numbers += str(num_temp) + " "
    if num_temp % 2 == 1:
        res_odd_numbers += str(num_temp) + " "
    else:
        res_even_numbers += str(num_temp) + " "
    res_reverse_number = str(num_temp) + " " + res_reverse_number
    res_sum += num_temp
    num_temp += 1
#
"""среднее арифметическое от всех целых чисел в диапазоне равно среднему арифметическому двух крайних чисел диапазона"""
res_middle = (num1 + num2) / 2

print(
    f"All numbers between {num1} and {num2} = {res_all_numbers}",
    f"All odd numbers between {num1} and {num2} = {res_odd_numbers}",
    f"All even numbers between {num1} and {num2} = {res_even_numbers}",
    f"All numbers between {num1} and {num2} in reverse order = {res_reverse_number}",
    f"Summa of all numbers between {num1} and {num2} = {res_sum}",
    f"Average of all numbers between {num1} and {num2} = {res_middle}",
    sep="\n",
)

# Задание 2
# Пользователь вводит с клавиатуры число. Требуется посчитать факториал числа.
# Например, если введено 3, факториал числа 1*2*3 = 6.
# Формула для расчета факториала: n! = 1*2*3…*n, где n — число для расчета факториала.

try:
    num = int(input("Enter positive number: "))
    if num == 0:
        print("Factorial = 1")
    elif num < 0:
        raise ValueError("Number is negative")
    else:
        res = 1

        while num > 1:
            res *= num
            num -= 1

        print("Factorial = ", res)

except ValueError as err:
    print(err)

# Задание 3
# Пользователь вводит с клавиатуры длину линии. Нужно отобразить на экране горизонтальную линию из *, указанной длины.
# Например, если было введено 7, тогда вывод на экран будет такой: *******.

try:
    length = int(input("Enter length of line: "))
    if length < 0:
        raise ValueError("Length is negative")
    else:
        for i in range(0, length):
            print("*", sep="", end="")

except ValueError as err:
    print(err)

# Задание 4
# Пользователь вводит с клавиатуры длину линии и символ для заполнения линии.
# Нужно отобразить на экране горизонтальную линию из введенного символа, указанной длины.
# Например, если было введено 5 и &, тогда вывод на экран будет такой: &&&&&.

try:
    length = int(input("Enter length of line: "))
    symbol = input("Enter any key: ")

    if length < 0:
        raise ValueError("Length is negative")
    else:
        for i in range(0, length):
            print(symbol, sep="", end="")

except ValueError as err:
    print(err)

# Задание 5
# Написать игру «Угадай число».
# Программа загадывает число в диапазоне от 1 до 500.
# Пользователь пытается его угадать.
# После каждой попытки программа выдает подсказки, больше или меньше его число загаданного.
# В конце программа выдает статистику: за сколько попыток угадано число.
# Предусмотреть выход при вводе 0 в случае, если пользователю надоело угадывать число.

import random

num = random.randint(1, 500)

user_num = 1
attempts = 0

while user_num != 0:
    attempts += 1
    user_num = int(input("Enter number [1-500]: "))
    if user_num == num:
        print("\nOK. You guess! Number is ", num)
        break
    elif user_num > num:
        print("Your number more (>) then my number")
    elif user_num == 0:
        print("\nTry again. Please!!!")
    else:
        print("Your number smaller (<) then my number")

print(f"You used {attempts} attempts")

# Задание 6
# Пользователь вводит с клавиатуры ширину и высоту прямоугольника.
# Требуется отобразить на экран заполненный прямоугольник с указанными высотой и шириной.
# Например, если пользователь ввёл высоту 3, а ширину 5 на экране будет выведено:
# *****
# *****
# *****
# А также отобразить на экран незаполненный прямоугольник (отображаются только границы прямоугольника).
# Размер длины и ширины равен введенным данным.

# # Добавил пробелы между элементами, чтобы выглядело симпатичнее
width = int(input("Enter width of rectangle: "))
height = int(input("Enter height of rectangle: "))

n = 0
rect = ""

while n < height:
    if n == 0:
        rect += "* " * width + "   " + " *" * width + "\n"
    elif n < height - 1:
        rect += "* " * width + "   " + " *" + "  " * (width - 2) + " *" + "\n"
    else:
        rect += "* " * width + "   " + " *" * width
    n += 1

print(rect)

# Задание 7
# Написать программу, которая выводит на экран шахматную доску с заданным размером клеточки. Например, три,
# ***---***---***---***---
# ***---***---***---***---
# ***---***---***---***---
# ---***---***---***---***
# ---***---***---***---***
# ---***---***---***---***

width = int(input("Enter width of cell: "))

desk = ""
for i in range(1, 5):
    desk += (
        ("*" * width + "-" * width) * 4 + "\n" + ("-" * width + "*" * width) * 4 + "\n"
    )

print(desk)

# Задание 8
# Написать программу, которая проверяет пользователя на знание таблицы умножения.
# Программа выводит на экран два числа, пользователь должен ввести их произведение.
# Разработать несколько уровней сложности (отличаются сложностью и количеством вопросов).
# Вывести пользователю оценку его знаний.
#
# Логика решения примерно такая—запускаем код в вечном цикле, который прерывается по какой-то команде пользователя,
# в теле цикла, предлагаем пять вариантов однозначных цифр, пять двузначных,
# причем не обязательно сначала только те потом другие,
# считаем верные и неверные ответы по пятибалльный шкале, исходя из процентного соотношения верных и неверных ответов.
# Пользователь должен иметь возможность прекратить игру в любой момент и сразу получить оценку
#
import random

level = int(input("Choose level [1-3]: "))

num1 = num2 = 1
ans = 0
ans_quan = 0
right_ans = 0
finish = ""

while finish != "f":
    if level == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif level == 2:
        num1 = random.randint(1, 10)
        num2 = random.randint(11, 30)
    elif level == 3:
        num1 = random.randint(11, 30)
        num2 = random.randint(11, 33)

    ans = float(input(f"{num1} * {num2} = "))
    right_ans += 1 if ans == num1 * num2 else 0
    ans_quan += 1
    finish = input('Enter "f" for finish. Push ENTER for continue.')

if 1 >= right_ans / ans_quan >= 0.8:
    res = "5"
elif 0.8 > right_ans / ans_quan >= 0.6:
    res = "4"
elif 0.6 > right_ans / ans_quan >= 0.4:
    res = "3"
else:
    res = "2"

print(f"Your mark: {res}")
