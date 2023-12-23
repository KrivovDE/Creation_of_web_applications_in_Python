# import os
# abs_path = os.path.abspath('my_file')
# print(abs_path)
# print(type(abs_path))

# file = open('/Users/ШАГ/Course creating web applications with Python/Tutorials for Python/module_7_/my_file.txt')


#
# try:
#     file = open('my_file2.txt')
# except FileNotFoundError:
#     print('Невозможно открыть файл')
# # #
#
# file = open('out.txt', 'w')

# file = open('my_file.txt')
# print(file.read())

# _____________________________________________________
# try:
#     file = open('my_file.txt', encoding='utf-8')
#     print(file.read(13))
#     file.seek(0)
#     print(file.read(3))
#     print(file.tell())
#
# except FileNotFoundError:
#     print('Невозможно открыть файл')
# _____________________________________________________
#
# try:
#     file = open('my_file.txt', encoding='utf-8')
#     # print(file.readline(), end="")
#     # print(file.readline(), end="")
#     # for line in file:
#     #     print(line, end="")
#     s = file.readlines()
#     print(s)
# except FileNotFoundError:
#     print('Невозможно открыть файл')

# # _____________________________________________________
# try:
#     file = open('my_file.txt')
#     try:
#         s = file.readlines()
#         print(s)
#     finally:
#         file.close()
# except FileNotFoundError:
#     print('Невозможно открыть файл')
# # _____________________________________________________
# file = open("out.txt", "w")
# file.write("Hello World!\n")
#
# file.write("Привет мир!")
# #
# file.write("Hello1\n")
# file.write("Hello2\n")
# file.write("Hello3\n")

# # _____________________________________________________
# file = open("out.txt", "a+")
# file.writelines(["Hello11\n", "Hello22\n"])
# file.seek(0)
# print(file.read())
# # _____________________________________________________
# import pickle
# #
# books = [
#     ("Евгений Онегин", "Пушкин А.С.", 200),
#     ("Муму", "Тургенев И.С.", 250),
#     ("Мастер и Маргарита", "Булгаков М.А.", 500),
#     ("Мертвые души", "Гоголь Н.В.", 190)
# ]
# #
# try:
#     file = open("out.bin", "wb")
#     try:
#         pickle.dump(books, file)
#
#     finally:
#         file.close()
# except FileNotFoundError:
#     print('Невозможно открыть файл')
#
#
# try:
#     file = open("out.bin", "rb")
#     try:
#         bs = pickle.load(file)
#         print(bs)
#     finally:
#         file.close()
# except FileNotFoundError:
#     print('Невозможно открыть файл')

# _____________________________________________________
# import pickle
#
# book1 = ["Евгений Онегин", "Пушкин А.С.", 200]
# book2 = ["Муму", "Тургенев И.С.", 250]
# book3 = ["Мастер и Маргарита", "Булгаков М.А.", 500]
# book4 = ["Мертвые души", "Гоголь Н.В.", 190]
# try:
#     file = open("out.bin", "wb")
#     try:
#         pickle.dump(book1, file)
#         pickle.dump(book2, file)
#         pickle.dump(book3, file)
#         pickle.dump(book4, file)
#     finally:
#         file.close()
# except FileNotFoundError:
#     print("Невозможно открыть файл")
#
# try:
#     file = open("out.bin", "rb")
#     try:
#         b1 = pickle.load(file)
#         b2 = pickle.load(file)
#         b3 = pickle.load(file)
#         b4 = pickle.load(file)
#         print(b1, b2, b3, b4, sep="\n")
#     finally:
#         file.close()
# except FileNotFoundError:
#     print("Невозможно открыть файл")

#
# list_ = [1, 2, 3, 4, 5, 6]
# str = "str(list_)"
#
# for i in list_:
#     print(id(i))
#
# print()
# print(id(list_))


# class X:
#     def var(self, lif):
#         return lif - 2
#
#
# class A(X):
#     x = 100
#
# class B(X):
#     x = 10
#
# a = A()
# d = a.x
# b = B()
#
# print(a.var(a.x))
#
#

# def say_name(name):
#     def say_goodbye():
#         print("Don't say me goodbye, " + name + "!")
#
#     say_goodbye()
#
# say_name("Sergey")


def outer():  # внешняя функция
    n = 5  # лексическое окружение - локальная переменная

    def inner():  # локальная функция
        nonlocal n
        n += 1  # операции с лексическим окружением
        print(n)

    return inner


outer()  # fn = inner, так как функция outer возвращает функцию inner
outer()  # fn = inner, так как функция outer возвращает функцию inner
outer()  # fn = inner, так как функция outer возвращает функцию inner
# вызываем внутреннюю функцию inner
# fn()  # 6
# fn()  # 7
# fn()  # 8

# def mergeSort(alist):
#     print("Splitting ",alist)
#     if len(alist)>1:
#         mid = len(alist)//2
#         lefthalf = alist[:mid]
#         righthalf = alist[mid:]
#
#         mergeSort(lefthalf)
#         mergeSort(righthalf)
#
#         i=0
#         j=0
#         k=0
#         while i<len(lefthalf) and j<len(righthalf):
#             if lefthalf[i]<righthalf[j]:
#                 alist[k]=lefthalf[i]
#                 i=i+1
#             else:
#                 alist[k]=righthalf[j]
#                 j=j+1
#             k=k+1
#
#         while i<len(lefthalf):
#             alist[k]=lefthalf[i]
#             i=i+1
#             k=k+1
#
#         while j<len(righthalf):
#             alist[k]=righthalf[j]
#             j=j+1
#             k=k+1
#     print("Merging ",alist)
#
# alist = [54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)
#
# def merge(left_list, right_list):
#     sorted_list = []
#     left_list_index = right_list_index = 0
#
#     # Т. к. длина списков применяется часто, создадим для удобства переменные
#     left_list_length, right_list_length = len(left_list), len(right_list)
#
#     for _ in range(left_list_length + right_list_length):
#         if left_list_index < left_list_length and right_list_index < right_list_length:
#             # Сравниваем первые элементы в начале каждого списка
#             # Если 1-й элемент левого подсписка меньше, добавляем его
#             # в сортированный массив
#             if left_list[left_list_index] <= right_list[right_list_index]:
#                 sorted_list.append(left_list[left_list_index])
#                 left_list_index += 1
#             # Если 1-й элемент правого подсписка меньше, добавляем его
#             # в сортированный массив
#             else:
#                 sorted_list.append(right_list[right_list_index])
#                 right_list_index += 1
#
#         # Когда достигнут конец левого списка, добавляем элементы правого списка
#         # в конец результирующего списка
#         elif left_list_index == left_list_length:
#             sorted_list.append(right_list[right_list_index])
#             right_list_index += 1
#         # Когда достигнут конец правого списка, добавляем элементы левого списка
#         # в сортированный массив
#         elif right_list_index == right_list_length:
#             sorted_list.append(left_list[left_list_index])
#             left_list_index += 1
#
#     return sorted_list
#
# def merge_sort(nums):
#     # Возвращаем список, когда он состоит из одного элемента
#     if len(nums) <= 1:
#         return nums
#
#     # Чтобы найти середину списка, применяем деление без остатка
#     # Индексы должны быть integer
#     mid = len(nums) // 2
#
#     # Сортируем и объединяем подсписки
#     left_list = merge_sort(nums[:mid])
#     right_list = merge_sort(nums[mid:])
#
#     # Объединяем сортированные списки в результирующий
#     return merge(left_list, right_list)
#
# # Проверяем, что всё работает
# random_list_of_nums = [120, 45, 68, 250, 176]
# random_list_of_nums = merge_sort(random_list_of_nums)
# print(random_list_of_nums)
