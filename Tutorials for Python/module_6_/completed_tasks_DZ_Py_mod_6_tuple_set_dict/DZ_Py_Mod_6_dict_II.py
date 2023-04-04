from typing import List

# ЗАДАНИЕ 1 Основы работы со словарями
# Дополните приведенный код, чтобы он вывел имена всех пользователей
# (в алфавитном порядке), чей номер оканчивается на 88.
# Примечание. Имена необходимо вывести на одной строке, разделяя символом
# пробела.


# users: List[dict, ...] = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
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
# print(*sorted([i['name'] for i in users if i['phone'].endswith('8')]))

# ЗАДАНИЕ 2 Основы работы со словарями
# Напишите программу, которая будет превращать натуральное число в строку,
# заменяя все цифры в числе на слова:

# digit: dict = {
# 	0: 'zero',
# 	1: 'one',
# 	2: 'two',
# 	3: 'three',
# 	4: 'four',
# 	5: 'five',
# 	6: 'six',
# 	7: 'seven',
# 	8: 'eight',
# 	9: 'nine'
# }
#
#
# def to_String(digs: int, dct: dict) -> None:
# 	for i in str(digs):
# 		print(dct[int(i)], end=' ')
# 	print(end='\n')
#
#
# to_String(230, digit)
# to_String(7, digit)
# to_String(11111111, digit)
# to_String(542221, digit)
# to_String(1234, digit)
# to_String(5768893421059687532109586321134, digit)
# ЗАДАНИЕ 3 Основы работы со словарями
#
# Напишите программу, которая по номеру курса выводит информацию о данном
# курсе.

# Формат входных данных
# На вход программе подается одна строка – номер курса.
# Формат выходных данных
# Программа должна вывести номер курса, затем номер аудитории, имя
# преподавателя и время проведения курса в соответствии с примерами.

# dicts: dict = {
#     'CS101': [3004, 'Хайнс', '8:00'],
#     'CS102': [4501, 'Альварадо', '9:00'],
#     'CS103': [6755, 'Рич', '10:00'],
#     'NT110': [1244, 'Берк', '11:00'],
#     'CM241': [1411, 'Ли', '13:00']
# }
#
#
# def to_Course(dct: dict, inp: str) -> None:
#     print(f'{inp}:', ', '.join(map(str, dct[inp])))
#
#
# to_Course(dicts, 'CS101')
# to_Course(dicts, 'CM241')
# to_Course(dicts, 'CS102')
# to_Course(dicts, 'NT110')
# to_Course(dicts, 'CS103')

# ЗАДАНИЕ 4 Основы работы со словарями
# Код Морзе для представления цифр и букв использует тире и точки.
# Напишите программу для кодирования текстового сообщения в соответствии с
# кодом Морзе.

# Формат входных данных
# На вход программе подается одна строка – текстовое сообщение.
# Формат выходных данных
# Программа должна вывести закодированное с помощью кода Морзе сообщение,
# оставляя пробел между каждым закодированным символом
# Примечание. Ваша программа должна игнорировать любые символы, не
# перечисленные в таблице.

import re
morze: dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
         'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
         'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
         'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
         'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
         'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
         '9': '----.'}


def to_Morze(mrz: dict, line: str) -> None:
    reg_letter = re.findall(r'[A-z0-9]', line)
    if len(reg_letter) > 0:                                         # В морзе
        for i in reg_letter:
            print(mrz[i.upper()], end=' ')
        print(end='\n')
    else:                                                           # Из морзе
        reg_morze = re.sub(r'[^\s.-]', '', line).split(' ')
        for i in reg_morze:
            for item, value in mrz.items():
                if i == value:
                    print(item, end='')
        print(end='\n')


to_Morze(morze, 'Interstellar')
to_Morze(morze, 'SOS')
to_Morze(morze, 'Agent 007')
to_Morze(morze, 'Hello, World!')
to_Morze(morze, 'zero000')
to_Morze(morze, '89+54=143')
to_Morze(morze, 'Interstellar')
to_Morze(morze, 'Python3.8')
to_Morze(morze, '.. -. - . .-. ... - . .-.. .-.. .- .-.')
to_Morze(morze, '... --- ...')
to_Morze(morze, '.- --. . -. - ----- ----- --...')
to_Morze(morze, '.... . .-.. .-.. --- .-- --- .-. .-.. -..')
to_Morze(morze, '--.. . .-. --- ----- ----- -----')
to_Morze(morze, '---.. ----. ..... ....- .---- ....- ...--')
to_Morze(morze, '.. -. - . .-. ... - . .-.. .-.. .- .-.')
to_Morze(morze, '.--. -.-- - .... --- -. ...-- ---..')
