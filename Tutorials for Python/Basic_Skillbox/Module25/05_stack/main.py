# TODO здесь писать код


class Steck:
    """
    Базовый класс формирующий стек.

    """

    def __init__(self, data: str):
        self.__steck = [data]

    def __str__(self):
        return "; ".join(self.__steck)

    def add(self, data: str):
        """
        Метод для добавления нового элемента в начало списка.

        :param data: новый элемент
        """
        self.__steck.insert(0, data)

    def take(self):

        """
        Метод для получения первого элемента в списке, если список пуст вернётся None
        :return: __steck[0]
        """

        if len(self.__steck) > 1:
            first_one = self.__steck[0]
            self.__steck.remove(first_one)
            return first_one
        elif len(self.__steck) == 1:
            first_one = self.__steck[0]
            self.__steck = []
            return first_one
        else:
            return None


class TaskManager:
    """
    Базовый класс менеджера задач.

    Attributes:
        __task(dict): Пустой словарь для дальнейшего добавление задач
        в качестве места хранения задач используется Steck.
    """

    __task = {}

    def __str__(self):
        result = ""
        for i_key in sorted(self.__task.keys()):
            result += f"{i_key}) {self.__task[i_key]}\n"
        else:
            return result

    def new_task(self, task: str, priority: int):
        """
        Метод для добавления новой задачи.
        Приоритет выступает в качестве ключа при добавлении данных в словарь.

        :param task: Задача которую необходимо выполнить
        :param priority: Приоритет задачи
        """
        if self.__task.get(priority) is None:
            self.__task[priority] = Steck(task)
        else:
            self.__task[priority].add(task)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)

# зачтено
