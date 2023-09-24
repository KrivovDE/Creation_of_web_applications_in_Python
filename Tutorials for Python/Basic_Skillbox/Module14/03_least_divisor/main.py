# TODO здесь писать код

def smallest_divider(N):
    for i in range(2, N):
        if N % i == 0:
            return i
    else:
        return N


user_number = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', smallest_divider(user_number))

# зачтено
