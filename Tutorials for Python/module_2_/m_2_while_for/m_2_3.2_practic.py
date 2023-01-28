# Задание 1
# s = 0
# n = 1
# while n:
#     n = int(input())
#     s += n
# print(s)

# Задание 2
# n = int(input())
# s = 1
# i = 2
# while i <= n:
#     s += 1/i
#     i += 1
# print(round(s, 3))

# Задание 3

try:
    deposit = float(input('Размер вклада - '))
    percent = float(input('проценты по вкладу - '))
    years = int(input('Количество лет - '))

    i = 1
    while i <= years:
        deposit += deposit / 100 * percent
        i += 1
    if deposit < 0:
        raise ValueError('Депозит получился отрицательный')
except ValueError as err:
    print(f'проверте корректность введенных данных - {err}')
else:
    print(f'баланс составит {round (deposit, 2)} руб.')

