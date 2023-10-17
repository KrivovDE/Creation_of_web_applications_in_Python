def site_print(in_dict, level=1):
    counter = 0
    for key in in_dict.keys():
        if isinstance(in_dict[key], dict):
            print('\t' * level, f"'{key}'", ': {')
            site_print(in_dict[key], level + 1)
            print('\t' * level, '}', end='')
            if len(in_dict.keys()) > counter + 1:
                print(',', end='')
                counter += 1
            print()
        else:
            print("\t" * (level + 1), "'{0}': '{1}'".format(key, in_dict[key]), end='')
            if len(in_dict.keys()) > counter + 1:
                print(',', end='')
                counter += 1
            print()


def site_gen(phone_name):
    return {
        'html': {
            'head': {
                'title': 'Куплю/продам {0} недорого'.format(phone_name)
            },
            'body': {
                'h2': 'У нас самая низкая цена на {0}'.format(phone_name),
                'div': 'Купить',
                'p': 'продать'
            }
        }
    }


amount_site = int(input('Сколько сайтов: '))
site_dict = {}

for _ in range(amount_site):
    phone_name = input('Введите название продукта для нового сайта: ')
    site_dict[phone_name] = site_gen(phone_name)
    for i_name, i_site in site_dict.items():
        print(f'Сайт для {i_name}: ')
        print('site = {')
        site_print(i_site)
        print('}\n')

# зачтено
