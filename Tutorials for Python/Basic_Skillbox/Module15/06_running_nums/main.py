# TODO здесь писать код


original_list = []
shifted_list = []
sequence_size = int(input("Введите размер последовательности: "))

for _ in range(sequence_size):
    ver = int(input("Введите число: "))
    original_list.append(ver)

shift = int(input("Сдвиг: "))

for i in range(0 - shift, len(original_list) - shift, 1):
    shifted_list.append(original_list[i])

print("Изначальный список:", original_list)
print("Сдвинутый список:", shifted_list)

# зачтено
