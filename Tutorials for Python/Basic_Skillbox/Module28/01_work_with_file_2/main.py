# TODO здесь писать код


import os

class File:
    """Файловый менеджер, создаёт файл если его не существует, или открывает на
    дозапись, если такой файл есть.
    """
    def __init__(self, file_name: str, mode: str) :
        self._file = file_name
        self._mode = mode

    def __enter__(self):
        if os.path.exists(self._file):
            self._mode = 'a'
            self.file_object = open(self._file, self._mode, encoding='utf-8')
            return self.file_object
        else:
            self.file_object = open(self._file, self._mode, encoding='utf-8')
            return self.file_object
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file_object.close()
        return True


with File('example.txt', 'w') as file:
    file.write('Всем привет!\n')