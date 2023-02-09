# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# a, z = input().split()
# a_k = str(ord(a))
# z_k = str(ord(z))
# print(f' Коды: {a} = {a_k}, {z} = {z_k}')
#
# print('Коды:', ', '.join([f'{i} = {ord(i)}' for i in input().split()]))
#
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print(input().replace('---', '--').replace('--', '-'))
#
# print('-'.join(input().replace('-',' ').split()))
#
# import re
# text = input()
# print(re.sub(r'[-]{2,3}', '-', text))
#
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a, b, c, = input().split()
# print(a.rjust(3, '0'), '\n', b.rjust(3, '0'), '\n', c.rjust(3, '0'), sep='')
#
# for i in input().split():
#     print(i.rjust(3, '0'))
#
# [print(i.rjust(3, '0')) for i in input().split()]
#
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a, b, c, d = input(), input(), int(input()), float(input()) * 2
# book = list([a, b, c, d])
# book[1] = 'Пушкин'
# del book[2]
# print(book)
#
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a = list(map(int, input().split()))
# print(max(a), min(a), sum(a))
#
# print(max(lst := [int(i) for i in input().split()]), min(lst), sum(lst))
#
#
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a = list(input())
# del a[0:2]
# a.insert(0, '8')
# lst = ''.join(a).replace('-', '')
# print(''.join(lst))
#
# print(input().replace('+7', '8').replace('-', ''))

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# name = input().split()
# # name = ['Дмитрий', 'Евгеньевич', 'Кривов']
#
# print(f"{name[-1]} {name[0][0]}.{name[1][0]}.")



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 8~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# n = int(input())
# s = []
# for i in range(n):
#     s.append([1] * n)
#     s[i][-1] = 5
#     print(*s[i], sep=' ')
# for i in lst:
#     print(*i)


import copy

n = int(input())

lst = [[1] * n] * n         # формируем вложенный список
print(f'lst--до--{lst}')    # [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
lst[0][-1] = 5              # меняем последний элемент на 5
print(f'lst----{lst}')      # [[1, 1, 5], [1, 1, 5], [1, 1, 5]]

lst3 = copy.deepcopy(lst)
print(f'lst3-до-{lst3}')
lst3[0][-1] = 5
print(f'lst3--{lst3}')

lst2 = copy.copy(lst)
print(f'lst2-до-{lst2}')
lst2[0][-1] = 5
print(f'lst2--{lst2}')

lst4 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(f'lst4-до-{lst4}')
lst4[0][-1] = 5
print(f'lst4--{lst4}')      # lst4--[[1, 1, 5], [1, 1, 1], [1, 1, 1]]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 9~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# n = int(input())
# s = []
# for i in range(n):
#     s.append([1] * n)
#     s[i][-1] = 5
#     print(*s[i], sep=' ')
#
# n=int(input())
# for i in range(n):
#     r=[]
#     for j in range(n-1):
#         r.append(1)
#     r.append(5)
#     print(*r)