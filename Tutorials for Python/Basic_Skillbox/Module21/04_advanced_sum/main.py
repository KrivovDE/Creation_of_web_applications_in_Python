# TODO здесь писать код


def my_summ(data_list):
    result = 0
    for i_ver in data_list:
        if isinstance(i_ver, list):
            result += my_summ(i_ver)
        else:
            result += i_ver
    else:
        return result


print(my_summ([[1, 2, [3]], [1], 3]))
print(my_summ((1, 2, 3, 4, 5)))

# зачтено
