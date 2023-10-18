# TODO здесь писать код

from zipfile import ZipFile

file_name = 'voyna-i-mir.txt'

# input_zip = ZipFile('voyna-i-mir.zip', 'r')
# input_zip.extract(file_name)
# input_zip.close()

letter_dict = {}
letter_list = []

data_in = open(file_name, 'r', encoding='utf-8')

for i_str in data_in:
    for i_sign in i_str:
        if i_sign.isalpha():
            if letter_dict.get(i_sign) != None:
                letter_dict[i_sign] += 1
            else:
                letter_dict[i_sign] = 1
data_in.close()

for i_key, i_value in letter_dict.items():
    letter_list.append((i_value, i_key))

print(sorted(letter_list, reverse = True))