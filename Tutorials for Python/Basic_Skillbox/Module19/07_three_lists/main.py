# TODO здесь писать код

def common_search(list_1, list_2):
    common_num = []
    for i_num in list_1:
        for i_ver in list_2:
            if i_num == i_ver:
                common_num.append(i_ver)
    return common_num


def unique_search(list_1, list_2):
    unique_num = []
    for i_num in list_1:
        for i_ver in list_2:
            if i_num == i_ver:
                break
        else:
            unique_num.append(i_num)
    return unique_num


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

array_4 = []
array_4.extend(array_2)
array_4.extend(array_3)

plenty_1 = set(array_1)
plenty_2 = set(array_2)
plenty_3 = set(array_3)

print('Задача 1:')
print('Решение без множеств:', common_search(array_1, common_search(array_2, array_3)))
print('Решение с множествами:', plenty_1 & (plenty_2 & plenty_3))

print('Задача 2:')
print('Решение без множеств:', unique_search(array_1, array_4))
print('Решение с множествами:', plenty_1 - plenty_2 - plenty_3)

# зачтено
