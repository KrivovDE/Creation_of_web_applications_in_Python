# TODO здесь писать код

number_of_person = int(input('Кол-во человек: '))
outgoing_order = int(input('Какое число в считалке? '))

people_list = list(range(1, number_of_person + 1))
starting_point = 0

print(f'Значит, выбывает каждый {outgoing_order}-й человек')
for _ in range(number_of_person - 1):
    print('\nТекущий круг людей:', people_list)
    print('Начало счёта с номера', people_list[starting_point])
    deleting_point = (starting_point + outgoing_order - 1) - (
                (starting_point + outgoing_order - 1) // len(people_list)) * len(people_list)
    print('Выбывает человек под номером:', people_list[deleting_point])
    people_list.remove(people_list[deleting_point])
    starting_point = deleting_point if (len(people_list) - 1) >= deleting_point else 0
print('\nОстался человек под номером', people_list[0])

# зачтено
