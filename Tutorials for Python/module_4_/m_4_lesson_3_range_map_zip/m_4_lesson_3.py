# import random
#
# list_1 = [1, 2, 45.34, True]
# print(random.choice(list_1))


# Хороший пароль должен быть произвольным и состоять минимум из 6 символов, в нём должны быть цифры,
# строчные и прописные буквы. Приготовить такой пароль можно по следующему рецепту:
# import random
#
# str1 = '123456789'
# str2 = 'qwertyuiopasdfghjklzxcvbnm'
# str3 = str2.upper()
# ls = list(str1+str2+str3)
# # Тщательно перемешиваем список
# random.shuffle(ls)
# psw = ''.join([random.choice(ls) for x in range(12)])
#
# print(psw)
#
#
# import random
# print(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for _ in range(12)]))
#
# import random
# psw = ''
#
# for x in range(12):
#     psw = psw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
# print(psw)

#---------------------------------------------------
# lst = [1, -2, 3, -4, -5]
#
# def sq(x):
#     return x**2
#
# b = list(map(sq, lst))
# print(b)


#---------------------------------------------------
# lst = ["Москва", "Рязань", "Смоленск", "Тверь", "Томск"]
# b = map(len, lst)
# a = list(b)
# print(a)
# b = map(str.upper, lst)
# b = list(b)
# print(b)

# b = map(lambda x: x[::-1], lst)
# b = list(b)
# print(b)
# # ---------------------------------------------------
# lst = ["Москва", "Рязань", "Смоленск", "Тверь", "Томск"]
#
# b = map(lambda x: x.replace("а", "А"), lst)
#
# c = map(sorted, b)
# res1 = list(c)
# print(res1)
#
# #---------------------------------------------------
# a = list(map(int, input().split()))
# print(a)
# #---------------------------------------------------
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def odd(x):
#     return x % 2
#
# # b = list(filter(odd, a))
# # print(b)
# #
# b = list(filter(lambda x: x % 2, a))
# print(b)
#---------------------------------------------------

# lst = ["Москва", "Рязань1", "Смоленск", "Тверь2", "Воронеж45"]
# b = filter(str.isalpha, lst)
# print(*b)

# #---------------------------------------------------
# items = [1, 2, 3, 4, 5]
# #
# acc = 0
# for item in items:
#     acc = acc + item
#
#
# acc2 = 1
# for item in items:
#     acc2 = acc2 * item
#
# print(acc, acc2, sep='\n')
#
# from functools import reduce
#
# sum_all = reduce(lambda x,y: x+y, items)
# print('reduce', sum_all)
#
# mult_all = reduce(lambda x,y: x*y, items)
# print('reduce', mult_all)
# #---------------------------------------------------


# #---------------------------------------------------

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
#
# it = zip(a, b)
# print(it)
# print(dict(it))
#
#
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# c = "abracadabra"
#
# it = zip(a, b, c)
# print(list(it))
#---------------------------------------------------
# На вход поступает строка из целых чисел, записанных через пробел.
# С помощью функции map преобразовать эту строку в список целых чисел, взятых по модулю.
# Сформируйте именно список lst из таких чисел. Отобразите его на экране в виде набора чисел, идущих через пробел

# s = input().split()
# lst = map(lambda x: abs(int(x)), s)
# for i in lst:
#     print(i, end=' ')
#
# print(*list(map(abs, map(int, input().split()))))
#---------------------------------------------------
# Вводятся названия городов в одну строчку через пробел. Необходимо определить функцию map, которая бы возвращала названия
# городов только длиной более 5 символов. Вместо остальных названий - строку с дефисом ("-").
# Сформировать список из полученных значений и отобразить его на экране в одну строчку через пробел.

# print(*list(map(lambda x: x if len(x) > 5 else "-", input().split())))
#---------------------------------------------------
# Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.

# n = map(int, input().split())
# res = filter(lambda x: 10 <= x <= 99 or -99 <= x <= -10, n)
# print(*list(res))
#
# print(*filter(lambda x: 9 < abs(x) < 100, map(int, input().split())))

# Вводятся два списка целых чисел. Необходимо попарно перебрать их элементы и перемножить между собой.
# При реализации программы используйте функции zip и map.
#
# n=map(int, input().split())
# m=map(int, input().split())
# res=(x*y for x,y in zip(n, m))
# for _ in range(3):
#     print(next(res), end= " ")
#
# m=map(lambda x: x[0]*x[1], zip(map(int, input().split()), map(int, input().split())))
# print(next(m), next(m), next(m))