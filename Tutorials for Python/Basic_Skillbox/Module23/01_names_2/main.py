# TODO здесь писать код


common_long = 0
line = 0

with open("people.txt", encoding="utf8") as people_file, open(
    "errors.log",
    "w",
    encoding="utf8",
) as error_file:
    for man in people_file:
        line += 1
        try:
            if len(man) - 1 < 3:
                text_error = f"Ошибка: менее трёх символов в строке {line}"
                raise BaseException(text_error)
            common_long += len(man) - 1
        except BaseException:
            print(text_error)
            error_file.write(f"BaseException({text_error})")
    else:
        print("Общее количество символов: ", common_long)

# зачтено
