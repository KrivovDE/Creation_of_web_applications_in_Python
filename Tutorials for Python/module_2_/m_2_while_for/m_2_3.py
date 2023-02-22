# S = 0
# i = 1
# while i <= 1000:
#     S += 1/i
#     i += 1
# print(S)

# a = 8
# count = 0
# while a != count:
#     if count % 2 == 0 or count == 0 or count == 5:
#         print(count)
#     count += 1
#

#
# s = 0
# i = 1
#
# while True:
#     s += 1/i
#     i += 1
#     print(s)
# # # # # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#
# z = 0
# v = -4
#
# while v < 100:
#     if v == 0:
#         break
#     z += 1/v
#     v = v + 1
# else:
#     print("Сумма вычислена корретно")
# print(z)
#

# # # # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#
# a = 0
# b = -5
# while b < 4:
#     b = b + 1
#     if b == 0:
#         continue
#     print(b)
#     a += 1/b
#
# print(a)

# # # # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# for x in 1, 5, 2, 4:
#     print(x**2)

# # # # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# for x in range(-5, 5, 1):
#     print(x)

## # # # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# s = 0
#
# for i in range(1, 1001):
#     s += 1/i
# print(s)

# # # # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# k = 0.5
# b = 2
#
# lst = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
#
# for x in lst:
#     print(x*k+b)

# line = int(input("Enter some string: "))
#
# for c in line:
#     print(c)
## # # # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print("\n")
# # # # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#
# number = 1
# while number < 5:
#     print(number)
#     number += 1
#
#
# number = 1
# while True:
#     print(number)
#     number += 1
#
#     if number >= 5:
#         break
# # # # # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# number = 0
# count = 0
#
# while count < 5:
#
#    number += 1
#
#    print(number)
#    count += 1
# # #

# number = 0
# count = 0
#
# while count < 5:
#     number += 1
#     if (number % 2) == 1:
#         continue
#
#     print(number)


#     count += 1
# # #
# # # # # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# number = 0
# while number < 300:
#     number += 1
#     if number % 3 == 0 and number % 5 != 0:
#         print(number, "divides by 3")
#     elif number % 3 == 0:
#         if number % 5 == 0 and number % 7 != 0:
#             print(number, "divides by 3 and 5")
#         elif number % 5 == 0 and number % 7 == 0:
#             print(number, "divides by 3 and 5 and 7")
#
#
# number = 0
# while number < 300:
#     number += 1
#     if number % 3 != 0:
#         continue
#     elif number % 5 != 0:
#         print(number, "divides by 3")
#     elif number % 7 != 0:
#         print(number, "divides by 3 and 5")
#     else:
#         print(number, "divides by 3 and 5 and 7")

#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# floor = 1
# energy = 70
# print(f'Я на {floor} этаже')

# while floor != 5:
#     step = 0
#     while step != 20:
#         step += 1
#         energy -= 1
#         if energy == 0:
#             print('Я устал, я немного отдохну')
#             energy += 70
#     floor += 1
#     print(f'Сейчас я на {floor} этаже')
# print('пришел')