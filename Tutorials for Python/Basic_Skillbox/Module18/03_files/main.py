# TODO здесь писать код


def start_check(text):
    special_sign = '@№$%^&\*()'
    for sign in special_sign:
        if text.startswith(sign):
            return True
    else:
        return False


text = input('Название файла: ')

if start_check(text):
    print('Ошибка: название начинается на один из специальных символов.')
elif not (text.endswith('.txt') or text.endswith('.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')

# зачтено
