# file = open('/Users/ШАГ/Course creating web applications with Python/Tutorials for Python/module_7/my_file.txt')
#
#
# try:
#     file = open('my_file2.txt')
# except FileNotFoundError:
#     print('Невозможно открыть файл')
#
#
# file = open('out.txt', 'w')

# _____________________________________________________
# try:
#     file = open('my_file.txt', encoding='utf-8')
#     print(file.read(13))
# except FileNotFoundError:
#     print('Невозможно открыть файл')
# _____________________________________________________

# try:
#     file = open('my_file.txt', encoding='utf-8')
#     print(file.readline(), end="")
#     print(file.readline(), end="")
#     # for line in file:
#     #     print(line, end="")
# except FileNotFoundError:
#     print('Невозможно открыть файл')

# _____________________________________________________
# try:
#     file = open('my_file.txt')
#     try:
#         s = file.readlines()
#         print(s)
#     finally:
#         file.close()
# except FileNotFoundError:
#     print('Невозможно открыть файл')
# _____________________________________________________
# file = open("out.txt", "w")
# file.write("Hello World\n!")
#
# # file.write("Привет мир!")
#
# file.write("Hello1\n")
# file.write("Hello2\n")
# file.write("Hello3\n")

# _____________________________________________________
# file = open("out.txt", "a")
# file.writelines(["Hello1\n", "Hello2\n"])
# _____________________________________________________


# _____________________________________________________


# _____________________________________________________





























