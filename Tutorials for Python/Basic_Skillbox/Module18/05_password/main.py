# TODO здесь писать код


def complexity_check(ps_wd):
    cointers = [len(ps_wd), 0, 0]
    for sign in ps_wd:
        if sign.isdigit():
            cointers[1] += 1
        elif sign.isupper():
            cointers[2] += 1
    if cointers[0] < 8 or cointers[1] < 3 or cointers[2] < 1:
        return False
    else:
        return True


while True:
    password = input("Придумайте пароль: ")
    if complexity_check(password):
        print("Это надёжный пароль!")
        break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")

# зачтено
