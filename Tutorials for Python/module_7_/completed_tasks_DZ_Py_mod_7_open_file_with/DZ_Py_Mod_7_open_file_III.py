# Задача 1. Сумма чисел 2
# Во входном файле numbers.txt записано N целых чисел,
# которые могут быть разделены пробелами и концами строк.
# Напишите программу, которая выводит сумму чисел во выходной файл answer.txt.
# Пример:
# Содержимое файла numbers.txt
#      2
# 2
#   2
#         2
# Содержимое файла answer.txt
# 8
#
# try:
#     file = open('numbers.txt')
#     c = file.read()
#     try:
#         file = open('answer.txt', 'w')
#     except:
#         print('не удалось открыть или прочитать файл answer.txt')
#     r = 0
#     for i in c:
#         if i != ' ' and i != '\n':
#             r += int(i)
#     file.write(str(r))
# except:
#     print('не удалось открыть или прочитать файл numbers.txt')

# Задача 2. Дзен Пайтона
# В файле zen.txt хранится так называемый
# Дзен Пайтона — текст философии программирования на языке Python.
# Выглядит он так:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# Напишите программу, которая выводит на экран все строки этого файла в обратном порядке.
# Кстати, попробуйте открыть консоль Python и ввести команду import this.
# Результат работы программы:
# Namespaces are one honking great idea -- let's do more of those!
# If the implementation is easy to explain, it may be a good idea.
# If the implementation is hard to explain, it's a bad idea.
# Although never is often better than *right* now.
# ………..
#
# try:
#  file = open('zen.txt')
#  try:
#     c = file.read()
#     for i in reversed(c.split('\n')):
#         print(i)
#  except:
#      print('ошибка чтения файла')
# except FileNotFoundError:
#     print('ошибка открытия файла')

# Задача 3. Турнир
# В файле first_tour.txt записано число K и данные об
# участниках турнира по настольной игре «Орлеан»: фамилии,
# имена и количество баллов, набранных в первом туре.
# Во второй тур проходят участники, которые набрали более K баллов в первом туре.
# Напишите программу, которая выводит в файл second_tour.txt
# данные всех участников, прошедших во второй тур, с нумерацией.
# В первой строке нужно вывести в файл second_tour.txt количество участников
# второго тура. Затем программа должна вывести фамилии, инициалы и количество
# баллов всех участников, прошедших во второй тур, с нумерацией.
# Имя нужно сократить до одной буквы.
# Список должен быть отсортирован по убыванию набранных баллов.
# Содержимое файла first_tour.txt:
# 80
# Petrov Vasiliy 110
# Petrov Vasiliy 100
# Ivanov Serg 80
# Sergeev Petr 92
# Petrov Vasiliy 98
# Vasiliev Maxim 78
#
# Содержимое файла second_tour.txt:
# 2
# 1) V. Petrov 98
# 2) P. Sergeev 92

# try:
#     file = open('first_tour.txt')
#     c = file.read().split('\n')
#     r = []
#     for i in c:
#         if int(i[-3:]) > int(c[0]):
#             r += [i]
#     d = []
#     for i in r:
#         d += (i.split(' '),)
#     n = sorted(d, key=lambda x: int(x[2]))
#     fff = []
#     for i in reversed(n):
#         fff += [i]
#     file = open('second_tour.txt', 'w')
#     file.write('2\n')
#     nv = 1
#     for i in fff:
#         file.write(f'{nv}) {i[1][0]}. {i[0]} {i[2]}\n')
#         nv += 1
# except:
#     print('ошибка открытия файла')


# Задача 5. Частотный анализ
# Есть файл text.txt, который содержит текст.
# Напишите программу, которая выполняет частотный анализ,
# определяя долю каждой буквы английского алфавита в общем
# количестве английских букв в тексте, и выводит результат в файл analysis.txt.
# Символы, не являющиеся буквами английского алфавита, учитывать не нужно.
# В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте,
# с тремя знаками в дробной части. Буквы должны быть отсортированы по убыванию
# их доли. Буквы с равной долей должны следовать в алфавитном порядке.
# Содержимое файла text.txt:
# Mama myla ramu.
#
# Содержимое файла analysis.txt:
# a 0.333
# m 0.333
# l 0.083
# r 0.083
# u 0.083
# y 0.083

# import string
# try:
#     file = open('text.txt')
#     c = file.read()
#     d = c.translate(str.maketrans('', '', string.punctuation))
#     r = ''
#     for i in d:
#         if i != '\n' and i != ' ':
#             r += i.lower()
#     g = set(list(r))
#     a = []
#     for i in g:
#         ff = float(r.count(i)/len(r))
#         a.append((i, ff))
#     n = sorted(a, key=lambda x: (-x[1], x[0]))
#     try:
#         file = open('analysis.txt', 'w')
#         for i in n:
#             file.write(f'{i[0]} {str(i[1])[0:5]}\n')
#     except:
#         print('ошибка открытия или чтения файла')
# except:
#     print('ошибка открытия или чтения файла')

# Задача 6. «Война и мир»**
# Мало кто не знает знаменитый роман Л. Н. Толстого «Война и мир».
# Это довольно объёмное произведение лежит в архиве voina-i-mir.zip.
# Напишите программу, которая подсчитывает статистику по буквам
# (не только русского алфавита) в этом романе и выводит результат
# на экран (или в файл). Результат должен быть отсортирован по
# частоте встречаемости букв (по возрастанию или убыванию).
# Регистр символов имеет значение.
# Постарайтесь написать программу так,
# чтобы для её работы не требовалась распаковка архива вручную.
#

# try:
#     str_open = open("textTolstoi.txt", 'r')
#     list_file = str_open.read()
#     count_dict = {}
#     count_letter = 0
#     for letter in list_file:
#         if (letter.isalpha()):
#             x = count_dict.get(letter, 0)
#             count_dict[letter] = x + 1
#             count_letter += 1
#     count_letter_dict = [(k, "{:8.6f}".format(count_dict[k] / count_letter)) for k in count_dict.keys()]
#     str_open.close()
#     count_letter_dict.sort(key=lambda x: x[1], reverse=True)
#     print()
#     for i in count_letter_dict:
#         print(i[0] + " " + i[1])
# except:
#     print('ошибка открытия файла')