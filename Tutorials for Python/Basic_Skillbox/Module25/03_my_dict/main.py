# TODO здесь писать код


class MyDict(dict):
    """Класс словаря Родитель dict."""

    def __init__(self, seq=None, **kwargs):
        super().__init__(**kwargs)

    def get(self, *args, **kwargs):
        """
        Переопределение функции get родительского словаря.
        Возвращает 0 вместо None если элемента нет в словаре.
        """
        return (
            super().get(*args, **kwargs)
            if not super().get(*args, **kwargs) is None
            else 0
        )


my_dict = MyDict()
my_dict[1] = "1"

print(my_dict.get(2))

# зачтено
