# TODO здесь писать код


class NumSquares:
    def __init__(self, max_num: int):
        self.max_num = max_num
        self.num = 0

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self) -> int:
        self.num += 1
        if self.num <= self.max_num:
            return self.num**2
        else:
            raise StopIteration


def num_squares(max_num: int):
    for i_num in range(1, max_num + 1):
        yield i_num**2
    else:
        return


max_num = int(input("Введите число: "))

squares_gen = (i_num**2 for i_num in range(1, max_num + 1))
ver_1 = NumSquares(max_num)

print("Класс-итератор -", end=" ")
for i_num in ver_1:
    print(i_num, end=" ")
print()

print("Функция-генератор -", end=" ")
for i_num in num_squares(max_num):
    print(i_num, end=" ")
print()

print("Генераторное выражение -", end=" ")
for i_num in squares_gen:
    print(i_num, end=" ")

# зачтено
