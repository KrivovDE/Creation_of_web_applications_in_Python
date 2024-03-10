# TODO здесь писать код

from typing import Any, Optional


class Node:
    def __init__(self, value: Any, link: Optional["Node"] = None, index: int = 0):
        self.value = value
        self.link = link
        self.index = index

    def __str__(self):
        return "({value})[{index}] -> {link}".format(
            value=self.value,
            index=self.index,
            link=self.link,
        )


class LinkedList:
    def __init__(self, value: Any):
        self.head = Node(value)
        self.tail = self.head
        self.current = self.head
        self.length = 1

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.length < 1:
            print("Список пуст")
            return
        else:
            if self.current is None:
                raise StopIteration
            while self.current.link is not None:
                value = self.current.value
                self.current = self.current.link
                return value
            else:
                value = self.current.value
                self.current = None
                return value

    def append(self, value: Any) -> None:
        if self.head.link is None:
            self.head.link = Node(value, index=self.head.index + 1)
            self.tail = self.head.link
            self.length += 1
        else:
            self.tail.link = Node(value, index=self.tail.index + 1)
            self.tail = self.tail.link
            self.length += 1

    def remove(self, del_index: int) -> None:
        self.current = self.head
        if self.length < 1:
            print("Список пуст")
            return
        elif self.length <= del_index or del_index < 0:
            raise IndexError("Индекс вне диапазона")
        else:
            while self.current.index != del_index - 1:
                self.current = self.current.link
            self.current.link = self.current.link.link
            self.length -= 1
            while self.current.link is not None:
                self.current = self.current.link
                self.current.index -= 1

    def get(self, searched_index: int) -> Optional[Node]:
        self.current = self.head
        if self.length < 1:
            print("Список пуст")
            return
        elif self.length <= searched_index or searched_index < 0:
            raise IndexError("Индекс вне диапазона")
        else:
            while self.current.index != searched_index:
                self.current = self.current.link
            return self.current.value

    def __str__(self):
        return f"{self.head}"


test_list = LinkedList(10)
print(test_list)
test_list.append(20)
print(test_list)
test_list.append(30)
test_list.append(40)
test_list.append(50)
print(test_list)
test_list.remove(2)
print(test_list)
test_list.remove(2)
print(test_list)
print(test_list.get(2))
print("\n\n")
for i_iter in test_list:
    print(i_iter, end=" ")

# зачтено
