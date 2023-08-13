# lst = ["Москва", "Санкт-Петербург", "Тверь", "Казань", "Воронеж"]
#
# for city in lst:
#     print(city)
#
# print(lst)
# /////////////////////////////////
# #
# digs = [-1, 0, 5, 3, 2]
#
# for i in range(len(digs)):
#     digs[i] **= 2
# print(digs)
# #
# /////////////////////////////////

# digs = [0] * 2
# n = 0
# x = 0
# while x >= 0:
#     x = int(input("Введите целое число: "))
#     digs[n] = x
#     n += 1
# print(digs)
#
# _sum = 0
# for i in range(n):
#     _sum += digs[i]
# _sum = _sum / n
#
# print("S = %f, N = %d" % (_sum, n))

# /////////////////////////////////

# A = [[1,2,3], [4,5,6], [7,8,9]]


# Инструмент list comprehensions

# A = []
# N = 10
# for x in range(N+1):
#     A.append(x ** 2)
#
# print(A)
#
# print('-'*100)
#
# N = 10
# A = [_**2 for _ in range(N+1)]
#
# print(A)
# /////////////////////////////////


# N = 10
# A = []
# for x in range(N):
#     if x % 2 == 0:
#         A.append(x ** 2)
#
# print(A)
#
# N = 10
#
# A = [x**2 for x in range(N) if x % 2 == 0]
#
# print(A)
# # /////////////////////////////////
#
# cities = ["Москва", "Тверь", "Рязань", "Ярославль", "Владимир"]
# A = [i for i in cities if len(i) < 7]
# print(A)

# # # /////////////////////////////////
#
# x = int(input("Введите целое положительное число: "))
# digs = []
# while x:
#     # digs.append(x % 10)   #берем последнюю цифру числа
#     # x = x//10             #отбрасываем последнюю цифру числа
#     digs = [x % 10] + digs
# print(digs)
# # # /////////////////////////////////
#
# # программа reverse
# N = 4
# A = list(range(N))
# print(A)
#
# for i in range(N // 2):
#     A[i], A[N - i - 1] = A[N - i - 1], A[i]
#
# print(A)

# # /////////////////////////////////


# сортировка методом выбора
# A = [2, 2, -1, -5, 55, 34, 0, 10]
# N = len(A)
# pr = 0
# for i in range(N-1):
#     for j in range(i+1, N):
#         if A[i] > A[j]:
#             pr += 1
#             A[i], A[j] = A[j], A[i]
# print(A)
# print(pr)
from copy import deepcopy

srt = [1, 7, 1, -10, 4, 76]
srt7 = deepcopy(srt)
# srt2 = srt.copy()
# srt.sort()
#
#
# # print(srt2)
# print(srt)
