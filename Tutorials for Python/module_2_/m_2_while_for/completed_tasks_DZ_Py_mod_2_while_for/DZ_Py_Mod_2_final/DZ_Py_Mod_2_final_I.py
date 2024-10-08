# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Вводится натуральное число n. Вычислить сумму всех натуральных чисел меньше
# n, которые кратны или 3 или 5. Результат (сумму) вывести на экран.
# Пример: n = 10, имеем числа: 3, 5, 6, 9. Их сумма равна 23.

n = int(input("Число:\n--> "))
digits = ""
total = 0

for i in range(1, n):
    if i % 3 == 0 or i % 5 == 0:
        digits += str(i) + "; "
        total += i

print(
    f"n = {n}\n" f"Имеем числа: {digits}\n" f"Их сумма равна {total}",
)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# X красных машин и Y белых стоят в одном ряду.
# Напишите программу, которая выдаст, как нужно расположить красные и белые
# машины, чтобы рядом с каждой красной стояла хотя бы одна белая, а рядом
# с каждой белой — хотя бы одна красная.
# На вход подаются два числа - кол-во красных машин X и кол-во белых машин Y.
# В ответе выведите строку, в которой будет ровно X символов “R”
# (красные машины) и Y символов “W” (белые машины), удовлетворяющую условию
# задачи. Пробелы между символами выводить не нужно.
# Если расставить машины согласно условию задачи невозможно,
# выведите строку “Нет решения”.

red_cars = int(input("Кол-во красных: "))
white_cars = int(input("Кол-во белых: "))

if (red_cars > 2 * white_cars) or (white_cars > 2 * red_cars):
    print("Нет решения")
elif red_cars >= white_cars:
    diff_cars = red_cars - white_cars
    for _ in range(diff_cars):
        print("RWR", end="")
    for _ in range(white_cars - diff_cars):
        print("RW", end="")
else:
    diff_cars = white_cars - red_cars
    for _ in range(diff_cars):
        print("WRW", end="")
    for _ in range(red_cars - diff_cars):
        print("WR", end="")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Написать программу, которая проверяет пользователя на знание таблицы умножения.
# Программа выводит на экран два числа, пользователь должен ввести их произведение.
# Вывести пользователю оценку его знаний.
#
try:
    from random import randint

    print(
        "Оценка на знание таблицы умножения.\n"
        "Программа выводит на экран пример, пользователь должен ввести верный ответ.\n"
        "С каждым пятым верным ответом сложноть будет увеличиваться, всего 5 уровней.\n"
        "В любой момент можно выйти из программы и узнать результат написав в ответ 0.\n",
    )

    answer = 1
    lvl = 1
    total_y = 0
    total = 0

    while answer != 0:
        if lvl == 1:
            max1 = 10
            max2 = 10
            min1 = 1
            min2 = 1
        elif lvl == 2:
            max1 = 100
            max2 = 10
            min1 = 10
            min2 = 1
        elif lvl == 3:
            max1 = 100
            max2 = 100
            min1 = 10
            min2 = 10
        elif lvl == 4:
            max1 = 1000
            max2 = 100
            min1 = 100
            min2 = 10
        elif lvl >= 5:
            max1 = 1000
            max2 = 1000
            min1 = 100
            min2 = 100

        num_1 = randint(min1, max1)
        num_2 = randint(min2, max2)

        answer = int(input(f"{num_1} * {num_2} = "))

        if answer == 0:
            break
        elif answer == num_1 * num_2:
            print("Верно\n")
            total_y += 1
            total += 1
            if total_y % 5 == 0 and total_y != 0:
                print("LVL UP!")
                lvl += 1
        elif answer != num_1 * num_2:
            print(
                "Неверно\n" f"Правильный ответ: {num_1*num_2}\n",
            )
            total += 1

    grade = ""
    score = 0
    if total != 0:
        score = total_y * 100 / total

    if score <= 20:
        grade = (
            "(Отсылка на мем)\nЧе закибербуйлили тебя, да?\n"
            "Ну я не знаю, выключи компьютер хз\n"
            "Ди отсюда давай"
        )
    elif 20 < score <= 40:
        grade = "Все ясно, двоечник"
    elif 40 < score <= 60:
        grade = "Харош"
    elif 60 < score <= 80:
        grade = "МегаХарош"
    elif 80 < score:
        grade = "УльтраМегаХарош"

    print(
        f"Уровень сложности - {lvl}\n"
        f"Всего ответов: {total}\n"
        f"Кол-во верных ответов - {total_y}\n"
        f"Процентное соотношение вреных ответов - {round(score, 1)}\n"
        f"Ваша оценка - {grade}",
    )

except ValueError as err:
    print(f"Ops :(\nERROR: {err}")
