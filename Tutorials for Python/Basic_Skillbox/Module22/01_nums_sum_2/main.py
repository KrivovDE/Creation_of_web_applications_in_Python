# TODO здесь писать код

in_data = open('numbers.txt', 'r')
out_data = open('answer.txt', 'w')
result = 0

for i_str in in_data:
    for i_sign in i_str:
        if i_sign.isdigit():
            result += int(i_sign)
else:
    out_data.write(str(result))

in_data.close()
out_data.close()