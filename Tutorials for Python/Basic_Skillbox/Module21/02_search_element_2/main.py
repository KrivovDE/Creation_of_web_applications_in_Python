# TODO здесь писать код

def search_value(orig_dict, key, deep=None):
    deep = deep_control(deep)
    if deep is None or deep:
        if key in orig_dict:
            return orig_dict[key]
        else:
            deep = deep_control(deep)
            if deep is None or deep:
                for i_key in orig_dict.values():
                    if isinstance(i_key, dict):
                        result = search_value(i_key, key)
                        if result:
                            return result
                else:
                    return False
            else:
                return False
    else:
        return False


def deep_control(depth):
    if depth is None:
        return None
    elif isinstance(depth, int):
        return depth - 1
    else:
        return False


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

searched_key = input('Введите искомый ключ: ')
search_depth = None

while True:
    set_deep = input('Хотите ввести максимальную глубину? Y/N: ').upper()
    if set_deep == 'Y':
        search_depth = int(input('Введите максимальную глубину: '))
        result = search_value(site, searched_key, search_depth + 1)
        break
    elif set_deep == 'N':
        result = search_value(site, searched_key)
        break
    else:
        print('Введён не верный параметр, повторите ввод.')

if result:
    print(result)
else:
    print('Значение для указанного ключа не найдено.')

# зачтено


def search_value2(orig_dict, key):


    if key in orig_dict:
        return orig_dict[key]
    else:
        for i_key in orig_dict.values():
            if isinstance(i_key, dict):
                result = search_value(i_key, key)
                if result:
                    return result
        else:
            return False


search_value2(site, "p")