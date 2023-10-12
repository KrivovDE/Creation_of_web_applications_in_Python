# TODO здесь писать код


zen = open('zen.txt', 'r')
temp_list = []

for i_str in zen:
    temp_list.append(i_str[:len(i_str) - 1])

for index_str in range( -1, -len(temp_list) - 1, -1):
    print(temp_list[index_str])

zen.close()