# TODO здесь писать код


def h_search(user_str):
    first_h, last_h = None, None
    flag = True
    for index_letter in range(len(user_str)):
        if user_str[index_letter] == "h":
            if flag:
                first_h = index_letter
                flag = False
            last_h = index_letter
    return first_h + 1, last_h - 1


original_str = input("Введите строку: ")
start, finish = h_search(original_str)
print(
    "Развёрнутая последовательность между первым и последним h:",
    original_str[finish : start - 1 : -1],
)

# зачтено
