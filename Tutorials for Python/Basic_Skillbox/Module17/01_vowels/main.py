# TODO здесь писать код


def vowel_check(check_sign):
    vowel_list = "ауоыиэяюёе"
    for letter in vowel_list:
        if letter == check_sign:
            return True
    else:
        return False


original_text = list(input("Введите текст: "))
filtred_text = [sign for sign in original_text if vowel_check(sign)]

print("\nСписок гласных букв:", filtred_text)
print("Длина списка:", len(filtred_text))

# зачтено
