# TODO здесь писать код


def name_check(name: str) -> bool:
    return False if name.isalpha() else True


def email_check(email: str) -> bool:
    return False if email.find("@") >= 0 and email.find(".") >= 0 else True


def age_check(age: int) -> bool:
    return False if 10 <= age <= 99 else True


with open("registrations.txt", encoding="utf-8") as reg_file, open(
    "registrations_bad.log",
    "w",
    encoding="utf-8",
) as bad_file, open("registrations_good.log", "w", encoding="utf-8") as good_file:
    for i_info in reg_file:
        i_info = i_info[:-1] if i_info.endswith("\n") else i_info
        try:
            user_data = i_info.split(" ")
            if len(user_data) < 3:
                raise IndexError
            elif name_check(user_data[0]):
                raise NameError
            elif email_check(user_data[1]):
                raise SyntaxError
            elif age_check(int(user_data[2])):
                raise ValueError
            else:
                good_file.write(f"{i_info}\n")

        except IndexError:
            bad_file.write(f"{i_info}\tНЕ присутствуют все три поля.\n")
        except NameError:
            bad_file.write(
                f"{i_info}\tПоле «Имя» содержит НЕ только буквы.\n",
            )
        except SyntaxError:
            bad_file.write(
                f"{i_info}\tПоле «Имейл» НЕ содержит @ или . (точку)\n",
            )
        except ValueError:
            bad_file.write(
                f"{i_info}\tПоле «Возраст» НЕ является числом от 10 до 99\n",
            )

# зачтено
