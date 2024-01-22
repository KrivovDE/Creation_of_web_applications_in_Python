# TODO здесь писать код


user_str_1 = input("Первая строка: ")
user_str_2 = input("Вторая строка: ")
temp_str = list(user_str_2)

if user_str_1 == user_str_2:
    print("Введённые строки идентичны.")
else:
    for counter in range(len(user_str_2) - 1):
        temp_str.insert(0, temp_str[-1])
        del temp_str[-1]
        if user_str_1 == "".join(temp_str):
            print(f"Первая строка получается из второй со сдвигом {counter + 1}.")
            break
    else:
        print("Первую строку нельзя получить из второй с помощью циклического сдвига.")

# зачтено
