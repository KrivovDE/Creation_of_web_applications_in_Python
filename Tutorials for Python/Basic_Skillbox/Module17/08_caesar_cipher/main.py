# TODO здесь писать код
def is_letter(letter):
    for sign in alphabet:
        if letter == sign:
            return True
    else:
        return False


def index_search(letter, shift):
    required_index = (
        alphabet.index(letter) + shift
        if alphabet.index(letter) + shift
        < len(
            alphabet,
        )
        else alphabet.index(letter)
        + shift
        - ((alphabet.index(letter) + shift) // len(alphabet))
        * len(
            alphabet,
        )
    )
    return alphabet[required_index]


alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
user_text = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))
encrypted_text = ""

for letter in user_text:
    if is_letter(letter):
        encrypted_text += index_search(letter, shift)
    else:
        encrypted_text += letter

print("Зашифрованное сообщение:", encrypted_text)

# зачтено
