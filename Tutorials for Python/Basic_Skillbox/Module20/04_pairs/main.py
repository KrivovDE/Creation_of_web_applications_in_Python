# TODO здесь писать код

import random


def split_by_two(input_list):
    prev_value = 0
    for index, value in enumerate(input_list):
        if index % 2 != 1:
            prev_value = value
        else:
            new_list_2.append((prev_value, value))


orig_list = [random.randint(0, 100) for _ in range(10)]
new_list = [
    (orig_list[i_num], orig_list[i_num + 1]) for i_num in range(0, len(orig_list), 2)
]
new_list_2 = []

split_by_two(orig_list)

print(orig_list)
print(new_list)
print(new_list_2)

# зачтено
