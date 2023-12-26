# TODO здесь писать код


def number_summ(N):
    result_summ = 0
    while N > 0:
        result_summ += N % 10
        N //= 10
    return result_summ


def number_count(N):
    counter = 0
    while N > 0:
        counter += 1
        N //= 10
    return counter


user_number = int(input("Введите число: "))
print("Сумма чисел:", number_summ(user_number))
print("Количество цифр в числе:", number_count(user_number))
print(
    "Разность суммы и количества цифр:",
    number_summ(user_number) - number_count(user_number),
)

# зачтено
