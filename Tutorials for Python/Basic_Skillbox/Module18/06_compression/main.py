# TODO здесь писать код


user_str = input("Введите строку: ")
encrypted_list = []
counters = [user_str[0], 0]

for sign in user_str:
    if sign == counters[0]:
        counters[1] += 1
    else:
        encrypted_list.append(counters.copy())
        counters[0] = sign
        counters[1] = 1
encrypted_list.append(counters.copy())

encrypted_str = [str(ver) for level_2 in encrypted_list for ver in level_2]

print("".join(encrypted_str))

# зачтено
