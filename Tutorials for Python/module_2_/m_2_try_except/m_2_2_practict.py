# try:
#     f = open('abc.txt')
#     r = f.read(1)
#     f.close()
# except FileNotFoundError:
#     print('File Not Found')



# a = float(input("a = "))
# b = float(input("b = "))
#
# c = (a * b) ** 0.5
# print(f'Среднее геометрическое = {c}')


try:
    a = float(input("a = "))
    b = float(input("b = "))

    if a * b >= 0:
        c = (a * b) ** 0.5
    else:
        raise ValueError("Невозможно определить среднее геометрическое введенных чисел.")
    print(f'Среднее геометрическое = {c}')

except ValueError as err:
    print("Ошибка:", err, "Проверьте введенные числа")
except Exception as err:
    print("Ошибка:", err)
