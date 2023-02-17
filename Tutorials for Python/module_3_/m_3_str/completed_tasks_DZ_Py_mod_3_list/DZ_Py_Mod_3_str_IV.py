# Задание 1
# Пользователь вводит с клавиатуры строку.
# - Произведите поворот строки.
# - Посчитайте количество букв, цифр в строке.
# Полученный результат выведите на экран.

msg = input('Enter string: ')

print(f'Reverse string: {msg[::-1]}')

res_let = 0
res_dig = 0

for i in range(len(msg)):
    if msg[i].isalpha():
        res_let += 1
    elif msg[i].isdigit():
        res_dig += 1

print(f'Quantity of letters: {res_let}\n'
      f'Quantity of digits: {res_dig}')
# --------------------Можно перебирать саму последовательность
# Задание 2
# Пользователь вводит с клавиатуры строку и символ или слово для поиска.
# Посчитайте сколько раз в строке встречается этот символ или слово,
# Полученный результат выведите на экран.

msg = input('Enter message: ')
set1 = input('Enter set for searching: ')

res_set = msg.count(set1)

print(f'Set in message: {res_set}')

# Задание 3
# Пользователь вводит с клавиатуры строку, слово для поиска, слово для замены.
# Произведите в строке замену одного слова на другое.
# Полученную строку отобразите на экране.

msg = input('Enter message: ')
set_search = input('Enter set for searching: ')
set_replace = input('Enter set for replace: ')

res = msg.replace(set_search, set_replace)

print(f'New message: {res}')

# Задание 4
# Есть некоторый текст.
# Реализуйте следующую функциональность:
# ■ Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
# ■ Посчитайте сколько раз цифры встречаются в тексте;
# ■ Посчитайте сколько раз знаки препинания встречаются в тексте;
# ■ Посчитайте количество восклицательных знаков в тексте.
# Полученный результат выведите на экран.

txt = input('Enter text: ')

end_mark = '.!?'
mark = '!()-;?:\'`",.'

L = len(txt)
mod_txt = txt[0].upper()
ind = 1
res_dig = 0
res_mark = 0
res_wow = 0

while ind < L:
    if txt[ind] in end_mark and ind < L-2:
        mod_txt += txt[ind] + ' ' + txt[ind+2].upper()
        ind += 3
    else:
        mod_txt += txt[ind]
        ind += 1

for i in range(L):
    if txt[i].isdigit():
        res_dig += 1
    elif txt[i] in mark:
        res_mark += 1

res_wow = txt.count('!')

print(f'Modified text : {mod_txt}\n'
      f'Digit\'s quantity: {res_dig}\n'
      f'Mark\'s quantity: {res_mark}\n'
      f'! quantity: {res_wow}')

