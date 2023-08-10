# Имеется фрагмент программы
# При его выполнении возникает ошибка FileNotFoundError.
# Запишите конструкцию try / except, чтобы отображалось сообщение "File Not Found",
# если файл не удается открыть.


# try:
#     f = open('abc.txt')
#     r = f.read(1)
#     f.close()
# except FileNotFoundError:
#     print('File Not Found')


# Программа написана верно, однако содержат места потенциальных ошибок.
# •	найдите потенциальные источники ошибок (укажите номера строк в строке документации);
# •	используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:

try:
    a = float(input("a = "))
    b = float(input("b = "))
    if a * b > 0:
        c = (a * b) ** 0.5
    else:
        raise ValueError('Вы ввели отрицательное число')
    print(f'Среднее геометрическое = {c}')
except ValueError as value:
    print(value)
except Exception as Except:
    print(Except)

