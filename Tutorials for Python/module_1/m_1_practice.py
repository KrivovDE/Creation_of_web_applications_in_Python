# Задание 1
# Выведите на экран надпись Nothing will work unless you do на разных строках. Пример вывода:
# Nothing
#   will work
#       unless you do.

# print('Nothing\n'
#       '     will work\n'
#       '        unless you do')

#####################################################
# Задание 2
# Пользователь вводит с клавиатуры два числа. Необходимо найти сумму чисел, разницу чисел, произведение.
#Результат вычислений вывести на экран.

# first = int(input('Введите первое число: '))
# second = int(input('Введите второе число: '))
#
# print('сумма чисел: '+ str(first+second))
#
# subtraction = first - second
# subtraction_str = str(subtraction)
# print('разница чисел: ' + subtraction_str)
#
# print('произведение чисел: ', first*second)


#####################################################
# Задание 3
# Пользователь вводит с клавиатуры два числа. Первое число — это значение, второе число процент, который необходимо посчитать.
# Например, мы ввели с клавиатуры 50 и 10. Требуется вывести на экран 10 процентов от 50.
# Результат: 5

# num = int(input('Введите число: '))
# perc = int(input('Введите процент: '))
#
# result = num * perc / 100
# print(result)


#####################################################
# Задание 5
# Пользователь с клавиатуры вводит двухзначное число. Например, 26. Нужно показать на разных строках значение первого и второго разряда. В нашем случае это будет выглядеть так:
# 2
# 6

# num = int(input('Введите двузначное число: '))
# a = num//10
# b = num % 10
# print(a)
# print(b)
#####################################################

# num = input('Введите двузначное число: ')
# a, *b = '12345'
# print(a)
# print(b)
#####################################################
# print(*input(), sep='\n')

#####################################################
# Задание 6
# Пользователь с клавиатуры вводит трёхзначное число. Например, 891.
# Нужно показать на разных строках значение первого, второго и третьего разряда.
# Также нужно показать на отдельной строке сумму этих трёх чисел.
# В нашем случае это будет выглядеть так:
# 8
# 9
# 1
# 18

# num = int(input('Введите трехзначное число: '))
#
# first = num//100
# second = (num - (first*100))//10
# third = num - (first*100 + second*10)
# _sum = first + second + third
#
# print(first, '\n', second, '\n', third, '\n', _sum)
#####################################################

# num = input('Введите трехзначное число: ')
#
# print(num[0])
# print(num[1])
# print(num[2])
# print(int(num[0])+int(num[1])+int(num[2]))

# x = input()
# print(*x, sep='\n')
# x = int(x)
# b = x//100 + x//10%10 + x%10
# print(b)

#####################################################
# Задание 7
# Пользователь вводит с клавиатуры две цифры. Необходимо создать число, содержащее эти цифры.
# Например, если с клавиатуры введено 9, 7, тогда нужно сформировать число 97.

# num1 = input('Введите первое число: ')
# num2 = input('Введите второе число: ')
#
# concat = int(num1+num2)
# print(concat)

#####################################################
# Задание 8
# Пользователь вводит с клавиатуры температуру по шкале Цельсия.
# Требуется перевести температуру в градусы по Фаренгейту и вывести на экран.
#
# temperature_C = float(input('Введите температуру в градусах Цельсия: '))
# temperature_F = (temperature_C * 1.8) + 32
#
# print(f'Температура в цельсиях = {temperature_C}\n значит в Фарингейтах это = {temperature_F}')

# a = float(input())
# c = a // 1
# print((a-c)*100 > 50)