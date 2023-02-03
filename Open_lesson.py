# x = int(input('Введите число - '))
#
# if x < 0:
#     print("x отрицательное число")
# if x >= 0:
#     print("x неотрицательное число")

#
# speed_const = 60
# speed_car = float(input('Введите скорость автомобиля: '))
#
# if speed_car <= 60:
#     print('Скоростной режим не нарушен')
# elif 60 > speed_car <= 80:
#     print('Превышение скорости от 20 до 40 км/ч - штраф 500 рублей')
# elif 80 > speed_car <= 120:
#     print('Превышение скорости от 40 до 60 км/ч - штраф 1000 рублей')
# else:
#     print('Превышение скорости от 80 км/ч - штраф 5000 рублей')
#
# # #
#
# speed_const = int(input('Введите разрешенную скорость: '))
# while True:
#     speed_car = float(input('Введите скорость автомобиля: '))
#
#     difference = speed_car - speed_const
#
#     if difference <= 0:
#         print('Скоростной режим не нарушен')
#     elif difference <= 40:
#         print('Превышение скорости от 20 до 40 км/ч - штраф 500 рублей')
#     elif difference <= 60:
#         print('Превышение скорости от 40 до 60 км/ч - штраф 1000 рублей')
#     else:
#         print('Превышение скорости от 80 км/ч - штраф 5000 рублей')


#

USERNAMES = {'peter', '123', 'progamer'}


def create_new_user(username, password):
    global USERNAMES
    USERNAMES.add(username)

#
def register_user():
    username = input()
    password = input()

    if len(username) <= 20:
        if len(username) > 3:
            if username in USERNAMES:
                print("User with this username already exists")
            else:
                if len(password) > 3:
                    create_new_user(username, password)
                    print("New user is created")
                else:
                    print("The password is too short")
        else:
            print("Username is too short")
    else:
        print("Username is too long")


if __name__ == '__main__':
    register_user()


#
# a = input('Город - ')
#
# if a == 'Воронеж':
#     print('Добро пожаловать в ' + a)
# elif a == 'Липецк':
#     print('Добро пожаловать в ' + a)
# else:
#     x = int(input('Введите число1 - '))
#     x1 = int(input('Введите число2 - '))
#     print(x**x1)


