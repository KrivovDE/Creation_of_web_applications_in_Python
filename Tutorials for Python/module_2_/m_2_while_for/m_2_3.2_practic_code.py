# # Задание 1
# s = 0
# n = 1
# while n:
#     n = int(input())
#     s += n
# print(s)
#
# # Задание 2
# n = int(input())
# s = 1
# i = 2
# while i <= n:
#     s += 1/i
#     i += 1
# print(round(s, 3))

# Задание 3
# try:
#     deposit = float(input('Размер вклада - '))
#     percent = float(input('проценты по вкладу - '))
#     years = int(input('Количество лет - '))
#
#     if percent < 0:
#         raise ValueError('Проценты по вкладу не могут быть отрицательными')
#
#     i = 1
#     while i <= years:
#         deposit += deposit / 100 * percent
#         i += 1
#
#     if deposit < 0:
#         raise ValueError('Депозит получился отрицательный')
#
# except ValueError as err:
#     print(f'проверте корректность введенных данных - {err}')
#
# else:
#     print(f'баланс составит {round (deposit, 2)} руб.')

# # Задание 4
# p = 1
# a = 1
# while a != 0:
#     a = int(input())
#     if a <= 0:
#         continue
#     p *= a
# print(p)
#
# n = int(input())
# i = 1
# while True:
#     if i ** 2 > n:
#         print(i)
#         break
#
#     i += 1

# Задание 5
# a = int(input())
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i)

# Задание 6
n = int(input())
for i in range(2, n):
    if n % i == 0:
        print('НЕТ')
        break
else:
    print('ДА')

# Задание 7
# n = int(input())
# s = 0
# for i in range(1, n):
#     if i % 3 == 0 or i % 5 == 0:
#         s += i
# print(s)

# Задание 8
# n = int(input())
#
# for i in range(2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=' ')

# Задание 9
# car_r = int(input('Введите количество красных машин: '))
# car_w = int(input('Введите количество белых машин: '))
# answer = ''
#
# if car_r > 2 * car_w or car_w > 2 * car_r:
#     print('Нет решения')
#
# elif car_r >= car_w:
#     difference = car_r - car_w
#     for i in range(car_r - difference):
#         answer += 'RWR'
#     for j in range(car_w - difference):
#         answer += 'RW'
#
# else:
#     difference = car_w - car_r
#     for i in range(car_w - difference):
#         answer += 'WRW'
#     for j in range(car_r - difference):
#         answer += 'WR'
#
# print(answer)