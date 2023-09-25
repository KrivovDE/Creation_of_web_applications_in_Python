# TODO здесь писать код

group_1 = []
group_2 = []
common_group = []

for add_1 in range(160, 178, 2):
    group_1.append(add_1)

for add_2 in range(162, 183, 3):
    group_2.append(add_2)

common_group.extend(group_1)
common_group.extend(group_2)

for level_1 in range(len(common_group) - 1):
    for level_2 in range(level_1 + 1, len(common_group)):
        if common_group[level_2] < common_group[level_1]:
            common_group[level_1], common_group[level_2] = common_group[level_2], common_group[level_1]

print('Отсортированный список учеников:', common_group)

# зачтено
