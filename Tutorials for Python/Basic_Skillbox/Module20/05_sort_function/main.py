# TODO здесь писать код

def tpl_sort(in_tuple):
    sort_list = list(in_tuple)
    for i_index_1, i_value in enumerate(in_tuple):
        if not isinstance(i_value, int):
            return in_tuple
        else:
            for i_index_2 in range(i_index_1 + 1, len(in_tuple)):
                if sort_list[i_index_1] > sort_list[i_index_2]:
                    sort_list[i_index_1], sort_list[i_index_2] = sort_list[i_index_2], sort_list[i_index_1]
    else:
        return tuple(sort_list)


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
print(tpl_sort((6, 3, -1, 8, 4, 11.30, -5)))
print(tpl_sort((6, 3, -1, 8, 4, "a", -5)))

# зачтено
