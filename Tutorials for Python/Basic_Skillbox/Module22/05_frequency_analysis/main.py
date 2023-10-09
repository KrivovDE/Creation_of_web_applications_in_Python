# TODO здесь писать код


# file_create = open('text.txt', 'w')
# file_create.write('Mama myla ramu.')
# file_create.close()

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# alphabet_dict = {}
# for order in range(len(alphabet)):
#     alphabet_dict[alphabet[order]] = order

letter_counter = 0
letter_dict = {}
sorted_list = []

alphabet_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

data_in = open('text.txt', 'r')

for i_str in data_in:
    for i_sign in i_str.lower():
        if i_sign.isalpha():
            if letter_dict.get(i_sign) != None:
                letter_dict[i_sign] += 1
            else:
                letter_dict[i_sign] = 1
            letter_counter += 1
data_in.close()


for i_key, i_value in letter_dict.items():
    if len(sorted_list) == 0:
        sorted_list.append((i_key, i_value))
    else:
        for index, i_elem in enumerate(sorted_list):
            if i_value > i_elem[1]:
                sorted_list.insert(index + 1, (i_key, i_value))
                sorted_list[index], sorted_list[index + 1] = sorted_list[index + 1], sorted_list[index]
                break
            elif i_value == i_elem[1]:
                if alphabet_dict[i_key] < alphabet_dict[i_elem[0]]:
                    sorted_list.insert(index + 1, (i_key, i_value))
                    sorted_list[index], sorted_list[index + 1] = sorted_list[index + 1], sorted_list[index]
                    break
        else:
            sorted_list.append((i_key, i_value))

result = open('analysis.txt', 'w')

for i_letter in sorted_list:
    result.write(f'{i_letter[0]} {round(i_letter[1] / letter_counter, 3)}\n')
result.close()
