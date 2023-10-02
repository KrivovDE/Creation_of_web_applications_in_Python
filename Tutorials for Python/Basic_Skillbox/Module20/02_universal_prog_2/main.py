# TODO здесь писать код

def is_prime(index):
    if index == 0 or index == 1:
        return False
    else:
        for i_num in range(2, index):
            if index % i_num == 0:
                return False
        else:
            return True


def crypto(data):
    return [sign for index, sign in enumerate(data) if is_prime(index)]


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))

# зачтено
