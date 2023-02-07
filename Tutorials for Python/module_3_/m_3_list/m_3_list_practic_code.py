# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# a, z = input().split()
# a_k = str(ord(a))
# z_k = str(ord(z))
# print(f' Коды: {a} = {a_k}, {z} = {z_k}')
#
# print('Коды:', ', '.join([f'{i} = {ord(i)}' for i in input().split()]))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print(input().replace('---', '--').replace('--', '-'))
#
# print('-'.join(input().replace('-',' ').split()))
#
# import re
# text = input()
# print(re.sub(r'[-]{2,3}', '-', text))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a, b, c, = input().split()
# print(a.rjust(3, '0'), '\n', b.rjust(3, '0'), '\n', c.rjust(3, '0'), sep='')
#
# for i in input().split():
#     print(i.rjust(3, '0'))
#
# [print(i.rjust(3, '0')) for i in input().split()]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a, b, c, d = input(), input(), int(input()), float(input()) * 2
# book = list([a, b, c, d])
# book[1] = 'Пушкин'
# del book[2]
# print(book)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a = list(map(int, input().split()))
# print(max(a), min(a), sum(a))
#
# print(max(lst := [int(i) for i in input().split()]), min(lst), sum(lst))
#

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a = list(input())
# del a[0:2]
# a.insert(0, '8')
# lst = ''.join(a).replace('-', '')
# print(''.join(lst))
#
# print(input().replace('+7', '8').replace('-', ''))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
name = input().split()
print(f"{name[-1]} {name[0][0]}.{name[1][0]}.")



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 8~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
