# TODO здесь писать код


def chain_of_num(max_num):
    if max_num == 1:
        return 1
    print(chain_of_num(max_num - 1))
    return max_num


print(chain_of_num(int(input('Введите num: '))))

# зачтено
