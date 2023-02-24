
# iter_1 = (x**2 for x in range(10))
#
# for i in iter_1:
#    print(i, end=" ")

# print(list(range(1000000000)))

# lst = (x for x in range(1000000000))
#
# for i in lst:
#     print(i, end="-")
#     if i > 1000000000:
#         break
# #---------------------------------------------------

def _get_all_average(n):
    avs = []
    count = 0
    res = 0
    for i in range(1, n + 1):
        count += 1
        res += i
        avs.append(res / count)
    return avs

print(_get_all_average(100000).__sizeof__())

def get_all_average(n):
    count = 0
    res = 0
    for i in range(1, n+1):
        count += 1
        res += i
        yield res/count

it = get_all_average(100000)
# print(next(it))
# print(next(it))
# print(next(it))
print('generator', next(it).__sizeof__())


#
#
# print(get_all_average(100))
# print(get_all_average(100000).__sizeof__())
#---------------------------------------------------

# def f():
#     return list(range(10))
#
# print(f())
#
#
# def f():
#     for x in range(10):
#         yield x
# #
# s = f()
# # print(s)
# print(next(s))
# print(next(s))
# #---------------------------------------------------
# На вход программы поступают два целых числа a и b (a < b), записанные в одну строчку через пробел.
# На их основе запишите генератор для формирования квадратов чисел в диапазоне [a; b].
# Преобразуйте этот генератор в список (без использования операторов циклов) и выведите на экран.

# a, b = map(int, input().split())
#
# lst_1 = list(i ** 2 for i in range(a, b + 1))
#
# print(lst_1)
#---------------------------------------------------

# На вход программы поступают два целых числа a и b (a < b), записанные в одну строчку через пробел.
# Определите генератор, который бы выдавал модули целых чисел из диапазона [a; b].
# В цикле выведите первые пять значений этого генератора. Каждое значение с новой строки.
# (Гарантируется, что пять значений имеются).

a, b = map(int, input().split())
gen = (abs(x) for x in range(a, b + 1))
for i in range(5):
    print(next(gen))

#---------------------------------------------------
# Необходимо записать генератор, который бы используя этот список, выдавал 1 000 000 наименований городов
# по циклу. То есть, дойдя до конца списка, возвращался в начало и повторял перебор. И так, для выдачи миллиона названий.
# Вывести на экран первые 20 наименований городов с помощью генератора в одну строчку через пробел.

cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
gen = (city for j in range(1000001) for city in cities)
counter = 0
for x in gen:
    if counter == 20:
        break
    print(x, end=' ')
    counter += 1











cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
gen = (city for j in range(1000001) for city in cities)
print(*list(gen)[:20])
#
#


