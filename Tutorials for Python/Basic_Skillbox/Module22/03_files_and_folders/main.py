# TODO здесь писать код

import os


def dir_size(dir_path):
    size, sub_dir, sub_file = 0, 0, 0
    for i_elem in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, i_elem)):
            data_tuple = dir_size(os.path.join(dir_path, i_elem))
            size += data_tuple[0]
            sub_dir += data_tuple[1] + 1
            sub_file += data_tuple[2]
        elif os.path.isfile(os.path.join(dir_path, i_elem)):
            size += os.path.getsize(os.path.join(dir_path, i_elem))
            sub_file += 1
    else:
        return size, sub_dir, sub_file


# user_path = input('Введите путь относительно \PycharmProjects: ')
# user_path = 'Python_Basic\Module14'
user_path = "Python_Basic"

size, sub_dir, sub_file = dir_size(
    os.path.abspath(os.path.join("..", "..", "..", user_path))
)

print("Размер каталога (в Кб):", size)
print("Количество подкаталогов:", sub_dir)
print("Количество файлов:", sub_file)
