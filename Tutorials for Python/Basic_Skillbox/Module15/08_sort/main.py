# TODO здесь писать код

# original_list = []
# sequence_size = int(input('Введите размер списка: '))
#
# for _ in range(sequence_size):
#     num = int(input('Введите число: '))
#     original_list.append(num)

original_list = [1, 4, -3, 0, 10]

print('Изначальный список:', original_list)
for MKAD in range(len(original_list) - 1):
    for TTR in range(MKAD + 1, len(original_list)):
        if original_list[TTR] < original_list[MKAD]:
            original_list[MKAD], original_list[TTR] = original_list[TTR], original_list[MKAD]

print('Отсортированный список:', original_list)

# зачтено
