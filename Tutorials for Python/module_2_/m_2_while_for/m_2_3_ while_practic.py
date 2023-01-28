# n = int(input())
# m = int(input())
# #
# while n <= m:
#     s = n ** 2
#     n += 1
#     print(s, end=' ')
# ////////////////////////////////////////////////////////

# x = float(input())
# i = 1
# s = x
# while i < 10:
#     s += x
#     i += 1
#     print(s, end=' ')

# ////////////////////////////////////////////////////////
# n = int(input())
# a = 1
# i = 3
# while i <= n:
#     a *= 2
#     i += 3
# print(a)
# ////////////////////////////////////////////////////////
# #
# n = 999
# i = 0
# while i <= n:
#     if i > 100:
#         if i % 47 == 43 and i % 3 == 0:
#             print(i, end=' ')
#     i += 1
#
#
# n = 99
# while n < 1000:
#     n += 3
#     if n % 47 == 43:
#         print(n, end=' ')
#
# i = 100
# j = 999
# while i <= j:
# #     while i % 47 == 43:
#         while i % 3 == 0:
#             print(i, end=' ')
#             i += 1
#         i += 1
#     i += 1
#
#
# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей
#
# ed, exp = 10000, 12000
#
# m = 1
# d = exp - ed
# while m < 10:
#     m += 1
#     exp *= 1.03
#     d += exp - ed
#
# d = round(d, 2)
# print('Студенту надо попросить', d, 'рублей.')
#
#
educational_grant = float(input('Введите размер дохода: '))
expenses = float(input('Введите сумму расходов: '))
time_period = int(input('Введите количество месяцов: '))

inflation = 1.03
month = 1
if educational_grant > expenses:
    print('по условию расходы превышают доходы, проверте введенные данные')
else:
    credit = expenses - educational_grant
    while month < time_period:
        month += 1
        expenses *= inflation
        credit += expenses - educational_grant
    print('------Студенту надо попросить', round(credit, 2), 'рублей.')
#
#
#
#
# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом
#
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
if month == 1:
    print('31 день')
elif month == 2:
    print('28 дней')
elif month == 3:
    print('31 день')
elif month == 4:
    print('30 дней')
elif month == 5:
    print('31 день')
elif month == 6:
    print('30 дней')
elif month == 7:
    print('31 день')
elif month == 8:
    print('31 день')
elif month == 9:
    print('30 дней')
elif month == 10:
    print('31 день')
elif month == 11:
    print('30 дней')
elif month == 12:
    print('31 день')
else:
    print('Такого месяца нет')
#
#
months_31 = [1, 3, 5, 7, 8, 10, 12]
months_30 = [4, 6, 9, 11]
months_february = [2]

choice = int(input("Введите, пожалуйста, номер месяца: "))
if choice in months_31:
    print('--31 день')
elif choice in months_30:
    print('--30 дней')
elif choice in months_february:
    print('--28 дней')
else:
    print('--Такого месяца нет')
#
#
#
