# Задание 1
# Вводится натуральное число n. Вычислить сумму всех натуральных чисел меньше n
# которые кратны или 3 или 5. Результат (сумму) вывести на экран.
# Пример: n = 10, имеем числа: 3, 5, 6, 9. Их сумма равна 23.
try:
    n = int(input("Введите натуральное число: "))
    amount = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            amount += i
    print(amount)
except ValueError:
    print("На ввод подаются только цифры")

# Задание 2
# X красных машин и Y белых стоят в одном ряду.
# Напишите программу, которая выдаст, как нужно расположить красные и белые
# машины, чтобы рядом с каждой красной стояла хотя бы одна белая, а рядом с
# каждой белой — хотя бы одна красная.
# На вход подаются два числа - кол-во красных машин X и кол-во белых машин Y.
# В ответе выведите строку, в которой будет ровно X символов “R” (красные машины)
# и Y символов “W” (белые машины), удовлетворяющую условию задачи. Пробелы между
# символами выводить не нужно.
# Если расставить машины согласно условию задачи невозможно, выведите строку
# “Нет решения”.

X = int(input("Введите количество красных машин: "))
Y = int(input("Введите количество белых машин: "))
car_first, car_second = "R", "W"
if Y > X:  # Переопределение если машин Y больше X
    X, Y = Y, X
    car_first, car_second = car_second, car_first
car_str = car_first
try:
    residue = X - Y  # Остаток машин
    for i in range(X + Y - 1):
        if not residue <= Y:  # Если остаток больше чем второе число - ошибка
            raise ValueError("Нет решения")
        elif (
            i < residue * 3
        ):  # если у нас есть остаток то каждая 3 машина будет стоять одна
            car_str += car_second if i % 3 == 0 else car_first
        elif residue % 2 == 0:  # порядок машин если остаток кратен двум
            car_str += car_second if i % 2 == 0 else car_first
        else:  # порядок если остаток не кратен двум или остатка нет
            car_str += car_second if i % 2 != 0 else car_first
except ValueError as err:
    print(err)
else:
    print(car_str)


# Задание 8
# Написать программу, которая проверяет пользователя на знание таблицы умножения.
# Программа выводит на экран два числа, пользователь должен ввести их произведение.
# Вывести пользователю оценку его знаний.

import random

print(
    "Тест на знание таблицы умножения, каждые 5 примеров сложность "
    "увеличивается.\nРейтинговая оценка, Европейская оценка.\n«Отлично - 5»,"
    " 99-86 %.\n«Хорошо - 4», 85-66 %.\n«Удовлетворительно - 3», 65-41 %.\n"
    "«Неудовлетворительно - 2», ниже 40% %.\nОценка будет объявлена в конце "
    "тестирования.\nДля окончания тестирования в ОТВЕТ ПРИМЕРА НЕОБХОДИМО "
    "ПОСТАВИТЬ 0.\nНачинаем!!!\n",
)
count_answer = 0  # Счетчик ответов
correct_answer = 0  # Счетчик правильных ответов
wrong_answer = 0  # Счетчик не правильных ответов
interest_answer = 0  # Записывает процент правильных ответов
first_num, second_num = 0, 0  # множители
try:
    while True:
        # Проверка уровней сложности
        if count_answer < 5:  # уровень сложности 1
            first_num = random.randrange(2, 10)
            second_num = random.randrange(2, 10)
        elif count_answer < 10:  # уровень сложности 2
            first_num = random.randrange(2, 10)
            second_num = random.randrange(11, 99)
        elif count_answer < 15:  # уровень сложности 3
            first_num = random.randrange(101, 999)
            second_num = random.randrange(11, 99)
        else:
            first_num = random.randrange(101, 999)  # уровень сложности 4
            second_num = random.randrange(101, 999)
        answer = int(input(f"Введите ответ {first_num} * {second_num} = "))
        if answer == first_num * second_num:
            correct_answer += 1
        elif answer == 0:
            break
        else:
            wrong_answer += 1
        count_answer += 1
        interest_answer = correct_answer / count_answer * 100  # Процент ответов
except ValueError:
    print("Тест завершился, возможно вы в ответ ввели не цифру!")

if interest_answer >= 86:
    print(
        "\nМолодец отличные знания!!!\n" "Оценка - 5 баллов",
    )
elif interest_answer >= 66:
    print(
        "\nУ тебя хорошие знания, но нужно потренироваться ещё\n" "Оценка - 4 балла",
    )
elif interest_answer >= 41:
    print(
        "\nПодучи математику возвращайся снова\n" "Оценка - 3 балла",
    )
else:
    print(
        "\nПлохой результат\n" "Оценка 2 - балла",
    )
print(
    f"Верные ответы - {correct_answer}\nНе верные ответы - {wrong_answer}\n"
    f"Количество вопросов - {count_answer}",
)
