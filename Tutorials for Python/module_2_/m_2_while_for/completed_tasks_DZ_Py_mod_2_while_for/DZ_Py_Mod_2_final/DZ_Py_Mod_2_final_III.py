# Задание 1
# Вводится натуральное число n. Вычислить сумму всех натуральных чисел меньше n, которые кратны или 3 или 5.
# Результат (сумму) вывести на экран.
# Пример: n = 10, имеем числа: 3, 5, 6, 9. Их сумма равна 23.

num_x = int(input('Enter number: '))

res = 0

for i in range(3, num_x):
    if i % 3 == 0 or i % 5 == 0:
        res += i
#
# print(res)

# Задание 2
# X красных машин и Y белых стоят в одном ряду.
# Напишите программу, которая выдаст, как нужно расположить красные и белые машины,
# чтобы рядом с каждой красной стояла хотя бы одна белая, а рядом с каждой белой — хотя бы одна красная.
# На вход подаются два числа - кол-во красных машин X и кол-во белых машин Y.
# В ответе выведите строку, в которой будет ровно X символов “R” (красные машины) и Y символов “W” (белые машины),
# удовлетворяющую условию задачи. Пробелы между символами выводить не нужно.
# Если расставить машины согласно условию задачи невозможно, выведите строку “Нет решения”.

red_car = int(input('Enter number of red car: '))
white_car = int(input('Enter number of white car: '))

if red_car / white_car > 2 or red_car / white_car < 0.5:
    res = 'Mission impossible!'
else:
    if red_car > white_car:
        color_more = 'R'
        color_less = 'W'
    else:
        color_more = 'W'
        color_less = 'R'
        red_car, white_car = white_car, red_car

    res = ''

    while red_car - white_car > 1:
        res += color_more + color_less + color_more
        red_car -= 2
        white_car -= 1
    while white_car != 0:
        res += color_more + color_less
        red_car -= 1
        white_car -= 1
    if red_car == 1:
        res += color_more

print(res)

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

import random

level = 1
num1 = num2 = 1
ans = 1
ans_quan = 0
right_ans = 0

print('Start game!',
      f'Level: {level}',
      'Enter answer "0" for finish', sep='\n')

while ans != 0:

    if level == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif level == 2:
        num1 = random.randint(1, 10)
        num2 = random.randint(11, 30)
    elif level == 3:
        num1 = random.randint(11, 30)
        num2 = random.randint(11, 33)

    ans = int(input(f'{num1} * {num2} = '))

    right_ans += 1 if ans == num1 * num2 else 0
    ans_quan += 1

    if ans_quan % 5 == 0 and level == 3:
        print('It was a maximum level')
        break
    elif ans_quan % 5 == 0:
        ans = int(input(f'Enter "0" for FINISH. Enter "1" if you want LEVEL UP. Another key for continue.'))
        if ans == 1:
            level += 1
            print('Continue game!',
                  f'Level: {level}', sep='\n')

if 1 >= right_ans / ans_quan >= 0.8:
    res = '5'
elif 0.8 > right_ans / ans_quan >= 0.6:
    res = '4'
elif 0.6 > right_ans / ans_quan >= 0.4:
    res = '3'
else:
    res = '2'

print(f'Total {ans_quan} answers',
      f'Right answers is {right_ans}',
      f'Your mark: {res}',
      f'Try again!', sep='\n')

