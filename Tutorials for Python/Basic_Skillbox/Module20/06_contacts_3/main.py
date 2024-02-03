# TODO здесь писать код


def add_contact():
    name, surname = input(
        "Введите имя и фамилию нового контакта (через пробел): "
    ).split()
    if (name, surname) in phone_book:
        print("Такой человек уже есть в контактах.")
        print("Текущий словарь контактов:", phone_book)
        return
    else:
        phone_book[(name, surname)] = input("Введите номер телефона: ")
        print("Текущий словарь контактов:", phone_book)
        return


def search_contact():
    searched_surname = input("Введите фамилию для поиска: ")
    for i_key in phone_book.keys():
        if i_key[1] == searched_surname:
            print(i_key[0], i_key[1], phone_book[i_key])
    else:
        return


phone_book = dict()

while True:
    action = input(
        "Введите номер действия: \n1. Добавить контакт \n2. Найти человека\n3. Выход\n"
    )
    if action == "1":
        add_contact()
    elif action == "2":
        search_contact()
    elif action == "3":
        break
    else:
        print("Выбрано некорректное действие.")

# зачтено
