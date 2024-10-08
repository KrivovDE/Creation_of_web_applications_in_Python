#  ЗАДАНИЕ 1
#
#  Основы работы со словарями
# Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке),
#  чей номер оканчивается на 8.
# Примечание. Имена необходимо вывести на одной строке, разделяя символом пробела.


# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# users.sort(key=lambda x: x['name'])
# print(*[i['name'] for i in list(filter(lambda x: x['phone'].endswith('8'), users))])


#  ЗАДАНИЕ 2
#
#  Основы работы со словарями
# Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова:
#
# 0 на zero;
# 1 на one;
# 2 на two;
# 3 на three;
# 4 на four;
# 5 на five;
# 6 на six;
# 7 на seven;
# 8 на eight;
# 9 на nine.
#
# Формат входных данных
# На вход программе подается натуральное число.
# Формат выходных данных
# Программа должна вывести строковое представление числа.


# Входные данные	Выходные данные
# 230	two three zero
# 7	seven
# 11111111	one one one one one one one one
# 542221	five four two two two one
# 1234	one two three four
# 5768893421059687532109586321134	five seven six  nine three four two one zero five nine six eight seven five th


# number ={'0': 'zero',
#         '1':  'one',
#         '2': 'two',
#         '3': 'three',
#         '4': 'four',
#         '5': 'five',
#          '6': 'six',
#          '7': 'seven',
#          '8': 'eight',
#          '9': 'nine'
# }
# print(*[number[key] for key in input('Введите числа: ')])


# ЗАДАНИЕ 3
#
# Основы работы со словарями
#
# Напишите программу, которая по номеру курса выводит информацию о данном курсе.
# Номер курса (ключ)	Номер аудитории (значение)	Преподаватель (значение)	Время (значение)
# CS101	3004	Хайнс	8:00
# CS102	4501	Альварадо	9:00
# CS103	6755	Рич	10:00
# NT110	1244	Берк	11:00
# CM241	1411	Ли	13:00
#
# Формат входных данных
# На вход программе подается одна строка – номер курса.
# Формат выходных данных
# Программа должна вывести номер курса, затем номер аудитории, имя преподавателя и
# время проведения курса в соответствии с примерами.
#
# Номер теста	Входные данные	Выходные данные
# 1	CS101	CS101: 3004, Хайнс, 8:00
# 2	CM241	CM241: 1411, Ли, 13:00
# 3	CS102	CS102: 4501, Альварадо, 9:00
# 4	NT110	NT110: 1244, Берк, 11:00
# 5	CS103	CS103: 6755, Рич, 10:00

# keis = input('Введите данные: ')
# record = {'CS101': '3004, Хайс, 8:00',
#           'CM241': '1411, Ли, 13:00',
#           'CS102': '4501, Альварадо, 9:00',
#           'NT110': '1244, Берк, 11:00',
#           'CS103': ' 6755, Рич, 10:00'}
#
# print('{}:{}'.format(keis, record[keis]))


# ЗАДАНИЕ 4
#
# Основы работы со словарями
# Код Морзе для представления цифр и букв использует тире и точки.
# Напишите программу для кодирования текстового сообщения в соответствии с кодом Морзе.
# Символ	Код	Символ	Код	Символ	Код	Символ	Код
# A	.-	J	.---	S	...	1	.----
# B	-...	K	-.-	T	-	2	..---
# C	-.-.	L	.-..	U	..-	3	...--
# D	-..	M	--	V	...-	4	....-
# E	.	N	-.	W	.--	5	.....
# F	..-.	O	---	X	-..-	6	-....
# G	--.	P	.--.	Y	-.--	7	--...
# H	....	Q	--.-	Z	--..	8	---..
# I	..	R	.-.	0	-----	9	----.
# Формат входных данных
# На вход программе подается одна строка – текстовое сообщение.
# Формат выходных данных
# Программа должна вывести закодированное с помощью кода Морзе сообщение,
# оставляя пробел между каждым закодированным символом
# Примечание. Ваша программа должна игнорировать любые символы, не перечисленные в таблице.
# 1	Interstellar	.. -. - . .-. ... - . .-.. .-.. .- .-.
# 2	SOS	... --- ...
# 3	Agent 007	.- --. . -. - ----- ----- --...
# 4	Hello, World!	.... . .-.. .-.. --- .-- --- .-. .-.. -..
# 5	zero000	--.. . .-. --- ----- ----- -----
# 6	89+54=143	---.. ----. ..... ....- .---- ....- ...--
# 8	Python3.8	.--. -.-- - .... --- -. ...-- ---..
#


# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morze = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
#          '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
#          '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----',
#          '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
#
# work_map = dict(zip(letters,morze))
#
# input_string = input('Введите текст: ').upper()
# output_string =(work_map.get(letters) for letters in input_string if work_map.get(letters))
#
# print(' '.join(output_string))
