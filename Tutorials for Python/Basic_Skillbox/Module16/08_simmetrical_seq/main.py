# TODO здесь писать код


def symmetry_check(list_num):
    limit = (
        int(len(list_num) / 2)
        if len(list_num) % 2 == 0
        else int((len(list_num) - 1) / 2)
    )
    for i_num in range(limit):
        if list_num[i_num] != list_num[-i_num - 1]:
            return False
    else:
        return True


sequence_size = int(input("Кол-во чисел: "))
input_seq = []
for _ in range(sequence_size):
    input_seq.append(int(input("Число: ")))

# input_seq = [1, 2, 1, 2, 2, 1, 2, 1]
add = []
counter = 0

print("\nПоследовательность:", input_seq)
if symmetry_check(input_seq):
    print("Введённая последовательность симметрична!")
else:
    temp_seq = input_seq
    while not (symmetry_check(temp_seq)):
        add.insert(0, temp_seq[0])
        temp_seq.remove(temp_seq[0])
        counter += 1
    print("Нужно приписать чисел:", counter)
    print("Сами числа:", add)

# зачтено
