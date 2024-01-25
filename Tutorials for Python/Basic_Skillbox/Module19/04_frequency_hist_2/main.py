# TODO здесь писать код
def sign_count(in_str):
    result = dict()
    for sign in in_str:
        if sign in result:
            result[sign] += 1
        else:
            result[sign] = 1
    return result


def dict_invert(in_dict):
    inverted_dict = {}
    for i_ver in set(in_dict.values()):
        inverted_dict[i_ver] = []
        for i_key, i_value in in_dict.items():
            if i_value == i_ver:
                inverted_dict[i_ver].append(i_key)
    return inverted_dict


text = input("Введите текст: ")
sign_dict = sign_count(text)
inverted_dict = dict_invert(sign_dict)

print("Оригинальный словарь частот:")
for pair in sorted(sign_dict):
    print(pair, ":", sign_dict[pair])

print("\nИнвертированный словарь частот:")
for pair in inverted_dict.keys():
    print(pair, ":", inverted_dict[pair])

# зачтено
