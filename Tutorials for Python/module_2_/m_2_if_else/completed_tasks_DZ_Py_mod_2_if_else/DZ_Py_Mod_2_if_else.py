# # -----------------------------------TASK 1-----------------------------------
# # Пользователь вводит с клавиатуры время в секундах, прошедшее с начала дня.
# # В зависимости от выбора пользователя посчитать, сколько часов,
# # минут и секунд осталось до полуночи.
#
# seconds = int(input('Введите время в секундах с начала дня (от 0 до 86400 сек.)'
#                     '\n ---> '))
# choice = input('Нужно выбрать действие:\n'
#                '1 - посчитать сколько часов осталось до полуночи\n'
#                '2 - посчитать сколько минут осталось до полуночи\n'
#                '3 - посчитать сколько секунд осталось до полуночи\n'
#                'Ваш выбор: ')
#
# if choice == '1':
#     result = str((86400 - seconds)/3600) + ' часов'
# elif choice == '2':
#     result = str((86400 - seconds)/60) + ' минут'
# elif choice == '3':
#     result = str(86400 - seconds) + ' секунд'
# else:
#     result = 'Нет такого выбора'
#
# print(result)
#
#
#
# # -----------------------------------TASK 2-----------------------------------
# # Пользователь вводит с клавиатуры диаметр окружности. В зависимости от выбора
# # пользователя посчитать площадь или периметр окружности.
#
# diameter = float(input('Введите диаметр окружности: '))
# choice = input('Нужно выбрать действие:\n'
#                '1 - посчитать площадь окружности\n'
#                '2 - посчитать периметр окружности\n'
#                'Ваш выбор: ')
#
# if choice == '1':
#     result = 'Площадь = ' + str(3.14 * (diameter/2)**2)
# elif choice == '2':
#     result = 'Периметр = ' + str(3.14 * diameter)
# else:
#     result = 'Нет такого выбора'
#
# print(result)
#
#
# import math
# num = 25
# sqrt = math.sqrt(num)
# print("Квадратный корень из числа " + str(num) + " это " + str(sqrt))# -----------------------------------TASK 3-----------------------------------
# # Пользователь вводит с клавиатуры стоимость одной
# # игровой приставки, их количество и процент скидки.
# # В зависимости от выбора пользователя посчитать общую
# # сумму заказа или стоимость одной приставки с учетом скидки.
#
#
# price_gc = float(input('Введите стоимость одной игровой консоли: '))
# count_gc = int(input('Введите кол-во игровых консолей: '))
# discount_gc = int(input('Введите процент скидки: '))
# choice = input('Нужно выбрать действие:\n'
#                '1 - посчитать общую сумму заказа\n'
#                '2 - посчитать стоимость одной игровой консоли с учетом скидки\n'
#                'Ваш выбор: ')
#
# if choice == '1':
#     result = 'Общая стоимость заказа = ' + str(price_gc * count_gc)
# elif choice == '2':
#     result = 'Стоимость одной игровой консоли ' \
#              'с учетом скидки = ' + str(price_gc * (1 - discount_gc/100))
# else:
#     result = 'Нет такого выбора'
#
# print(result)
#
#
#
# # -----------------------------------TASK 4-----------------------------------
# # Пользователь вводит с клавиатуры размер файла в гигабайтах и скорость
# # интернет-соединения в битах в секунду. В зависимости от выбора пользователя
# # посчитать, за сколько часов или минут, или секунд скачается файл.
#
# file_size = float(input('Чтобы размер файла в ГБ был здесь до обеда ---> '))
# inet_speed = int(input('Бро, введи скорость инета в бит/c пж ---> '))
# if inet_speed != ' ':
#     print('спс, чумба')
# choice = input('Вилку в глаз или ...\n'
#                '1 - посчитать за сколько ЧАСОВ скачаеться файл\n'
#                '2 - посчитать за сколько МИНУТ скачаеться файл\n'
#                '3 - посчитать за сколько СЕКУНД скачаеться файл\n'
#                '4 - c adsl подключением - вилку\n'
#                'Ваш выбор: ')
#
# if choice == '1':
#     result = str(((file_size*8589934592)/inet_speed) / 3600) + ' часов'
# elif choice == '2':
#     result = str(((file_size*8589934592)/inet_speed) / 60) + ' минут'
# elif choice == '3':
#     result = str((file_size*8589934592)/inet_speed) + ' секунд'
# elif choice == '4':
#     result = 'Не будь киберпсихом, чумб\n' \
#              'Когда нибудь у тебя будет GPON'
# else:
#     result = 'Нет такого выбора'
#
# print(result)



# -----------------------------------TASK 5-----------------------------------
# Пользователь с клавиатуры вводит количество часов.
# Если полученное значение находится в диапазоне от 0 до 6 нужно вывести
# надпись Good Night, если в диапазоне от 6 до 13 Good Morning, если в
# диапазоне от 13 до 17 Good Day, если в диапазоне от 17 до 0 Good Evening.
# Верхняя граница диапазона не включается.
# Например, число 6 относится к 6 до 13

time = int(input('«Месье, месье, который час?»\n- спросила консоль'
                 ' с французским акцентом.\n'
                 'Пользователь ответил - '))

if 0 <= time < 6:
    result = 'Гуд найт'
elif 6 <= time < 13:
    result = 'Гуд монинг'
elif 13 <= time < 17:
    result = 'Гуд дэй'
elif 17 <= time < 0:
    result = 'Гуд эвинг'
else:
    result = 'Ай донт ноу'
print(f'«{result}» - кокетливо выдала результат консоль.')
