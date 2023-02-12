# Задание 1
# Пользователь вводит с клавиатуры время в секундах, прошедшее с начала дня. В зависимости от выбора пользователя
# посчитать, сколько часов, минут и секунд осталось до полуночи.

time_past = int(input('Enter time in seconds: '))
time_left = input('Option:\n'
                  '1 - time left in hours\n'
                  '2 - time left in minutes\n'
                  '3 - time left in seconds\n'
                  'Enter what do you want to know: ')

if time_left == '3':
    rem = (86400 - time_past)
    print(rem, ' seconds left')
elif time_left == '2':
    rem = (86400 - time_past)//60
    print(rem, ' full minutes left')
elif time_left == '1':
    rem = (86400 - time_past)//3600
    print(rem, ' full hours left')
else:
    print('Choose option correctly')

# Задание 2
# Пользователь вводит с клавиатуры диаметр окружности. В зависимости от выбора пользователя посчитать площадь или
# периметр окружности.

du = float(input('Enter diameter: '))
choice = input('Option:\n'
               '1 - Square\n'
               '2 - Perimeter\n'
               'Choose what do you want to know: ')
if choice == '1':
    res = 3.14 * (du / 2)**2
    print('Circle\'s square is ', res)
elif choice == '2':
    res = 3.14 * du
    print('circle\'s perimeter is ', res)
else:
    print('Choose option correctly')

# Задание 3
# Пользователь вводит с клавиатуры стоимость одной
# игровой приставки, их количество и процент скидки.
# В зависимости от выбора пользователя посчитать общую
# сумму заказа или стоимость одной приставки с учетом скидки.

price = float(input('Enter price of console: '))
quan = int(input('Enter quantity: '))
disc = float(input('Enter % of discount: '))

print('What do you want to know?\n'
      '1 - total price\n'
      '2 - price of console with discount')
choice = input('Choose! ')

price_disc = price * (100 - disc)/100
if choice == '1':
    print('total price: ', price_disc * quan)
elif choice == '2':
    print('Price with discount: ', price_disc)
else:
    print('Choose option correctly')

# Задание 4
# Пользователь вводит с клавиатуры размер файла
# в гигабайтах и скорость интернет-соединения в битах в секунду. В зависимости от выбора пользователя посчитать,
# за сколько часов или минут, или секунд скачается файл.

file_size = float(input('Enter size of file (GB): '))
load_speed = float(input('Enter speed of download (b/sec): '))

print('Option:\n'
      '1 - hours, minutes and seconds\n'
      '2 - minutes and seconds\n'
      '3 - only seconds')
choice = input('Choose!____')

time_sec = file_size * 8589934592 // load_speed

if choice == '3':
    print('file will download in', time_sec, ' seconds')
elif choice == '2':
    time_min = time_sec//60
    sec_rem = time_sec % 60
    print('file will download in', time_min, ' minutes and', sec_rem, ' seconds')
elif choice == '1':
    time_hours = time_sec//3600
    min_rem = (time_sec % 3600) // 60
    sec_rem = time_sec % 60
    print('file will download in', time_hours, ' hours,', min_rem, ' minutes and', sec_rem, ' seconds')
else:
    print('Choose option correctly')

# Задание 5
# Пользователь с клавиатуры вводит количество часов. Если полученное значение находится в диапазоне от 0 до 6 нужно
# вывести надпись Good Night, если в диапазоне от 6 до 13 Good Morning, если в диапазоне от 13 до 17 Good Day,
# если в диапазоне от 17 до 0 Good Evening. Верхняя граница диапазона не включается.
# Например, число 6 относится к 6 до 13

hours = int(input('Enter hours [0-23]: '))

if 0 <= hours < 6:
    print('Good Night')
elif 6 <= hours < 13:
    print('Good Morning')
elif 13 <= hours < 17:
    print('Good Day')
elif 17 <= hours <= 23:
    print('Good Evening')
else:
    print('Enter number between 0 and 23')
