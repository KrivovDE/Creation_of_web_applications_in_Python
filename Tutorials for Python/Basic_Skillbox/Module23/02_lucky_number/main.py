# TODO здесь писать код

import random


def error_chance():
    some_num = random.randint(0, 13)
    return True if some_num == 13 else False


common_num, new_num = 0, 0

with open('out_file.txt', 'w', encoding='utf-8') as out_file:
    try:
        while common_num < 777:
            new_num = int(input('Введите число: '))
            common_num += new_num
            if error_chance():
                raise TypeError
            else:
                out_file.write('{}\n'.format(new_num))
        else:
            print('Вы успешно выполнили условие для выхода из порочного цикла!')
    except TypeError:
        print('Вас постигла неудача!')

# зачтено
