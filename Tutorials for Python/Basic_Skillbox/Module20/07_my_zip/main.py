# TODO здесь писать код


sign_str = 'abcd'
num_tuple = (10, 20, 30, 40)

print('Строка:', sign_str)
print('Кортеж чисел:', num_tuple)
smaller_length = len(sign_str) if len(sign_str) < len(num_tuple) else len(num_tuple)

pair_generator = ((sign_str[i_index], num_tuple[i_index])
                  for i_index in range(smaller_length))

print('\nРезультат:\n', pair_generator)

for i_pair in pair_generator:
    print(i_pair)

# зачтено
