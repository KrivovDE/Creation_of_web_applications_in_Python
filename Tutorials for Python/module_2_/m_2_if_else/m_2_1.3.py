USERNAMES = {'peter', '123', 'progamer'}


def create_new_user(username, password):
    global USERNAMES
    USERNAMES.add(username)


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
# # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# if len(password) <= 3:
#     print("The password is too short")
#     return
# else:
#     create_new_user(username, password)
#     print("New user is created")
#
# if len(password) <= 3:
#     print("The password is too short")
#     return
# create_new_user(username, password)
# print("New user is created")
# # # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#
# def register_user():
#     username = input()
#     password = input()
#
#     if len(username) > 20:
#         print("Username is too long")
#         return
#
#     if len(username) <= 3:
#         print("Username is too short")
#         return
#
#     if username in USERNAMES:
#         print("User with this username already exists")
#         return
#
#     if len(password) <= 3:
#         print("The password is too short")
#         return
#

    # create_new_user(username, password)
#     # print("New user is created")
# #
# # # # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# def is_username_valid(username):
#     if len(username) > 20:
#         print("Username is too long")
#         return False
#
#     if len(username) <= 3:
#         print("Username is too short")
#         return False
#
#     if username in USERNAMES:
#         print("User with this username already exists")
#         return False
#
#     return True
#
#
# def is_password_valid(password):
#     if len(password) <= 3:
#         print("The password is too short")
#         return False
#     return True
#
#
# def register_user():
#     username = input()
#     password = input()
#
#     if not is_username_valid(username):
#         return
#
#     if not is_password_valid(password):
#         return
#
#     create_new_user(username, password)
#     print("New user is created")
