# TODO здесь писать код


def list_create(N):
    N = N if N % 2 != 0 else N - 1
    for i in range(1, N + 1, 2):
        result_list.append(i)
    return result_list


result_list = []
number_N = int(input('Введите число N: '))

print('Список из нечётных чисел от одного до N:', list_create(number_N))

# зачтено
