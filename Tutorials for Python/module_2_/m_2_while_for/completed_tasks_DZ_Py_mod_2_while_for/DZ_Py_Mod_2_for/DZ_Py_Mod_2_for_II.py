# # Задание 1
# # Пользователь вводит с клавиатуры два числа.
# # •	показать все числа в указанном диапазоне.
# # •	показать все нечетные числа в указанном диапазоне.
# # •	показать все четные числа в указанном диапазоне.
# # •	показать все числа в указанном диапазоне в порядке убывания.
# # •	показать все нечетные числа в указанном диапазоне.
# # •	посчитать сумму чисел в диапазоне, а также среднеарифметическое.
# # Если границы диапазона указаны неправильно требуется произвести нормализацию границ.
# # Например, пользователь ввел 33 и 13, требуется нормализация после которой начало диапазона станет равно 13, а конец 33.
# #
#
# a = int(input('Первое число: '))
# b = int(input('Второе число: '))
# if a > b:
#     a, b = b, a
# print("Все числа от", a, "до", b, "включительно:", end=" ")
# for i in range(a, b+1):
#     print(i, end=" ")
# print("\n Нечетные числа от", a, "до", b, "включительно:", end=" ")
# for i in range(a, b+1):
#     if i % 2 != 0:
#         print(i, end=" ")
# print("\nЧетные числа от", a, "до", b, "включительно:", end=" ")
# for i in range(a, b+1):
#     if i % 2 == 0:
#         print(i, end=" ")
# print("\nВсе числа от", b, "до", a, "включительно в обратном порядке:", end=" ")
# for i in range(b, a-1, -1):
#     print(i, end=" ")
# print("\nСумма всех чисел от", a, "до", b, "включительно:", end=" ")
# sum = 0
# count = 0
# for i in range(a, b+1):
#     count += 1
#     sum += i
# print(sum)
# mid = sum/count
# print("Среднее арифмитическое: ", mid)
#
#
# # Задание 2
# # Пользователь вводит с клавиатуры число. Требуется посчитать факториал числа.
# # Например, если введено 3, факториал числа 1*2*3 = 6.
# # Формула для расчета факториала: n! = 1*2*3…*n, где n — число для расчета факториала.
#
# n = int(input('Введите число: '))
# f = 1
# for i in range(2, n+1):
#     f *= i
# print(f)
#
# # Задание 3
# # Пользователь вводит с клавиатуры длину линии.
# # Нужно отобразить на экране горизонтальную линию из *, указанной длины.
# # Например, если было введено 7, тогда вывод на экран будет такой: *******.
#
# a = int(input('Введите длину волны: '))
# b = '*'
# print(a * b)
#
#
# # Задание 4
# # Пользователь вводит с клавиатуры длину линии и символ для заполнения линии.
# # Нужно отобразить на экране горизонтальную линию из введенного символа, указанной длины.
# # Например, если было введено 5 и &, тогда вывод на экран будет такой: &&&&&.
#
# a = int(input('Введите число: '))
# b = input('введите символ: ')
# print(a * b)
#
# # Задание 5
# # Написать игру «Угадай число».
# # Программа загадывает число в диапазоне от 1 до 500.
# # Пользователь пытается его угадать. После каждой попытки программа выдает подсказки,
# # больше или меньше его число загаданного.
# # В конце программа выдает статистику: за сколько попыток угадано число,
# # сколько времени это заняло. Предусмотреть выход при вводе 0 в случае, если пользователю надоело угадывать число.
# #
#
# entered_number = 0
# counter = 0
# random_int = 300
# print('отгадай число')
# while entered_number != random_int:
#     entered_number = int(input('Введите число: '))
#     counter = counter + 1
#     if entered_number > random_int:
#         print('введите меньше')
#     elif entered_number < random_int:
#         print('введите больше')
#     else:
#         print('Ура')
#     print('Число попыток: ', counter)
# #
# #
# Задание 6
# Пользователь вводит с клавиатуры ширину и высоту прямоугольника.
# Требуется отобразить на экран заполненный прямоугольник с указанными высотой и шириной.
# Например, если пользователь ввёл высоту 3, а ширину 5 на экране будет выведено:
# *****
# *****
# *****
# А также отобразить на экран незаполненный прямоугольник (отображаются только границы прямоугольника).
# Размер длины и ширины равен введенным данным.
# #
# width = int(input('Ширина: '))
# length = int(input('Длина: '))
#
# for i in range(length):
#     for j in range(width):
#         print('*', end='')
#     print()
# print()
# print("*", '*' * (width-2), '*', sep='')
#
# for i in range(length-2):
#     print('*' + ' ' * (width - 2) + '*')
# print("*", '*' * (width-2), "*", sep='')

# Задание 7
# Написать программу, которая выводит на экран шахматную доску с заданным размером клеточки. Например, три,
# ***---***---***---***---
# ***---***---***---***---
# ***---***---***---***---
# ---***---***---***---***
# ---***---***---***---***
# ---***---***---***---***
#
black = "*" * 3
white = "_" * 3
length = 8
width = 8
for i in range(length):
    for j in range(width):
        if (i + j) % 2 == 0:
            print(black, end="")
        else:
            print(white, end="")
    print()


# Задание 8
# Написать программу, которая проверяет пользователя на знание таблицы умножения.
# Программа выводит на экран два числа, пользователь должен ввести их произведение.
# Вывести пользователю оценку его знаний.

# # При выполнении сделал,что бы был запрос 10раз и исходя из числа правильных ответов и выводилась оценка по 5 бальнйо системе)

#
# from random import randint
# right_answer = 0
# wrong_answer = 0
# for i in range(10):
#     a = randint(1, 10)
#     b = randint(1, 10)
#     answer = int(input(f'{a} * {b} = '))
#     if answer == a * b:
#         print('Right!')
#         right_answer += 1
#     else:
#         print('Wrong!')
#         wrong_answer += 1
# print(f"Результат: {right_answer} правиильно и  {wrong_answer} неправильно.")
# print(f"Your grade is {right_answer * 5 / 10}.")
