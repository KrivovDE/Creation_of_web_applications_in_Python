nice_list = [
    1,
    2,
    [3, 4],
    [[5, 6, 7], [8, 9, 10]],
    [[11, 12, 13], [14, 15], [16, 17, 18]],
]


# TODO здесь писать код


def list_unpacking(data, result_list=None):
    if result_list is None:
        result_list = []
    for i_ver in data:
        if isinstance(i_ver, list):
            result_list.extend(list_unpacking(i_ver))
        else:
            result_list.append(i_ver)
    return result_list


print(list_unpacking(nice_list))

# зачтено
