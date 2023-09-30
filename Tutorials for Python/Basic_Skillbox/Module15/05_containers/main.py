# TODO здесь писать код


def search_place(weigth, sequence):
    result = 0
    for i in range(len(sequence)):
        result = i if sequence[i] > weigth else result
    return result + 2


def size_check(num):
    while num > 200:
        print('Число не может быть больше 200!')
        num = int(input('Повторите ввод: '))
    return num


containers_list = []

sequence_size = int(input('Количество контейнеров: '))
for _ in range(sequence_size):
    containers_list.append(size_check(int(input('Введите вес контейнера: '))))

new_container = size_check(int(input('Введите вес нового контейнера: ')))
print('Номер, который получит новый контейнер:', search_place(new_container, containers_list))

# зачтено
