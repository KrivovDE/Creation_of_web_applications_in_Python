# TODO здесь писать код


def num_check(ip_list):
    for num in ip_list:
        if not (num.isdigit()):
            return num
        elif not (0 <= int(num) <= 255):
            return num
    else:
        return False


ip_address = input("Введите IP: ")
num_list = ip_address.split(".")
result_check = num_check(num_list)

if not result_check:
    print("IP-адрес корректен.")
elif ip_address.count(".") < 3:
    print("Адрес — это четыре числа, разделённые точками.")
elif not (result_check.isdigit()):
    print(result_check, "— это не целое число.")
elif result_check:
    print(f"{result_check} выходит за допустимый диапазон [0 255]")

# зачтено
