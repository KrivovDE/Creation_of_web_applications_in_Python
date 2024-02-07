# TODO здесь писать код


def khoar_sort(data_list):
    data_list[-1]
    less, equal, bigger = less_equal_more(data_list)
    if len(less) != 0:
        result_3 = khoar_sort(less)
    else:
        result_3 = less

    if len(bigger) != 0:
        result_1 = khoar_sort(bigger)
    else:
        result_1 = bigger
    return result_3 + equal + result_1


def less_equal_more(in_list):
    bigger, less, equal = [], [], []
    for i_num in in_list:
        if i_num > in_list[-1]:
            bigger.append(i_num)
        elif i_num < in_list[-1]:
            less.append(i_num)
        else:
            equal.append(i_num)
    else:
        return [less, equal, bigger]


print(khoar_sort([4, 9, 2, 7, 5]))
print(khoar_sort([5, 8, 9, 4, 2, 9, 1, 8]))

# зачтено
