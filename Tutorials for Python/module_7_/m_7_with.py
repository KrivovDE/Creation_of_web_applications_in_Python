#
# for line in file:
#     print(line)
#
# file.close()              # ручное закрытие файла
#
# print('Файл закрыт')
#
# # можно переписать в виде:
# with open('languages.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line)
#                           # автоматическое закрытие файла
# print('Файл закрыт')

# ==========================================================

# try:
#     with open("my_file.txt") as fp:
#         for t in fp:
#             print(t)
# except Exception as e:
#     print(e)

# ==========================================================
try:
    with open("my_file.txt") as fin:
        with open("out.txt", "w") as fout:
            for line in fin:
                fout.write(line)
except Exception as e:
    print(e)

# ==========================================================

with open("philosophers.txt", "w", encoding="utf-8") as output:
    print("Джoн Локк", file=output)
    print("Дэвид Хьюм", file=output)
    print("Эдмyнд Берк", file=output)

# ==========================================================
#
# with open('philosophers.txt', 'a+', encoding='utf-8') as output:
#     print('Джoн Локк', 'Дэвид Хьюм', 'Эдмyнд Берк', sep='|||||', file=output, end=' ')
