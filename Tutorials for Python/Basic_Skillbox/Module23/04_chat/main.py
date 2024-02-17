# TODO здесь писать код


def file_print() -> None:
    try:
        with open("messages.txt", encoding="utf-8") as messages_file:
            for i_massage in messages_file:
                print(i_massage, end="")
            else:
                print()
    except FileNotFoundError:
        print("В чате нет ни одного сообщения\n")


def new_massage(name: str, message: str) -> None:
    with open("messages.txt", "a", encoding="utf-8") as messages_file:
        messages_file.write(f"{name}: {message}\n")


user_name = input("Представьтесь: ")
while True:
    action = input(
        "1. Посмотреть текущий текст чата.\n"
        "2. Отправить сообщение (затем вводит сообщение).\n"
        "3. Выход\n",
    )
    if action == "1":
        file_print()
    elif action == "2":
        new_massage(user_name, input("Введите текст сообщения: "))
    elif action == "3":
        break
    else:
        print("Выбрано некорректное действие.")

# зачтено
