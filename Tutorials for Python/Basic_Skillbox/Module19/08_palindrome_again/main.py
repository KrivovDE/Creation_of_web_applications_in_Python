# TODO здесь писать код

user_str = input('Введите строку: ')
# user_str = 'aabc'
count_sym = dict()
break_counter = 0

for symbol in user_str:
    if symbol in count_sym:
        count_sym[symbol] += 1
    else:
        count_sym[symbol] = 1

for key in count_sym.keys():
    if count_sym[key] % 2 != 0:
        break_counter += 1
    if break_counter > 1:
        print('Нельзя сделать палиндромом')
        break
else:
    print('Можно сделать палиндромом')

# зачтено
