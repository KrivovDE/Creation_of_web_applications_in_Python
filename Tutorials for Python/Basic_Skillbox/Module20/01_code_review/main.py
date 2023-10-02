students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)

# TODO исправить код

def interests_surname_extract(user_dict):
    surname_summ = ''
    interests_list = []
    for id in user_dict:
        surname_summ += user_dict[id]['surname'] if isinstance(user_dict[id].get('surname'), str) else ''
        if user_dict[id].get('interests') != None:
            interests_list.extend(user_dict[id]['interests'])
        else:
            print('Для {0} нет данных по ключу- "interests"'.format(user_dict[id]['name']))
    else:
        interests_set = set(interests_list)
    return len(surname_summ), interests_set


id_age_list = []
for id, in_dict in students.items():
    if in_dict.get('age') != None:
        id_age_list.append((id, in_dict['age']))
    else:
        print('В списке нет ключа - "age"')
        break

common_surname_len, all_interests = interests_surname_extract(students)

print('Список пар "ID студента — возраст":', id_age_list)
print('Полный список интересов всех студентов:', all_interests)
print('Общая длина всех фамилий студентов:', common_surname_len)

# зачтено
