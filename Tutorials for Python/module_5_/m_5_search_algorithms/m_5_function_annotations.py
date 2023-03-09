# price: int = 5
# title: str
#
#
# def indent_right(s: str, width: int) -> str:
#     return " " * (max(0, width - len(s))) + s
#
#
# class Book:
#     title: str
#     author: str
#
#     def __init__(self, title: str, author: str) -> None:
#         self.title = title
#         self.author = author
#
#
# b: Book = Book(title='Fahrenheit 451', author='Bradbury')
# ---------------------------------------------------------------------
from functools import wraps
from typing import Optional, Any, Union, List, Tuple, Dict, Callable, TypeVar, Generic

#
# amount: int
# amount = None
#
# price: Optional[int]
# price = None
# ---------------------------------------------------------------------
# unknown_item: Any = 1
# print(unknown_item)
# print(unknown_item // 0)
# #---------------------------------------------------------------------
# unknown_object: object
# print(unknown_object)
# print(unknown_object.startswith("hello"))
# #---------------------------------------------------------------------
#
#
# def hundreds(x: Union[int, float]) -> int:
#     return (int(x) // 100) % 10
#
# hundreds(100.0)
# hundreds(100)
# hundreds("100")  # Expected type 'Union[int, float]', got 'str' instead
# ---------------------------------------------------------------------

# titles: List[str] = ["hello", "world"]
#
# titles.append(100500)  # Expected type 'str' (matched generic type '_T'), got 'int' instead
#
# titles = ["hello", 1]  # List item 1 has incompatible type "int"; expected "str"
#
# items: List = ["hello", 1]

# ---------------------------------------------------------------------
# price_container: Tuple[int] = (1,)
# price_container = ("hello")  # Expected type 'tuple[int]', got 'str' instead
# price_container = (1, 2)     # Expected type 'tuple[int]', got 'tuple[int, int]' instead
#
# price_with_title: Tuple[int, str] = (1, "hello")
#
# prices: Tuple[int, ...] = (1, 2)
# prices = (1, )
# prices = (1, "str")          # Expected type 'tuple[int, ...]', got 'tuple[int, str]' instead
#
# something: Tuple = (1, 2, "hello")

# ---------------------------------------------------------------------
# book_authors: Dict[str, str] = {"Fahrenheit 451": "Bradbury"}
# book_authors["1984"] = 0  # Incompatible types in assignment (expression has type "int", target has type "str")
# book_authors[1984] = "Orwell"
# ---------------------------------------------------------------------
# def nothing(a: int) -> None:
#     if a == 1:
#         return
#     elif a == 2:
#         return None
#     elif a == 3:
#         return ""  # Expected type 'None', got 'str' instead
#     else:
#         pass

# ---------------------------------------------------------------------
# class LinkedList:
#     data: Any
#     next: LinkedList  # NameError: name 'LinkedList' is not defined
#
#
# class LinkedList:
#     data: Any
#     next: 'LinkedList'


# ---------------------------------------------------------------------
# def help() -> None:
#     print("This is help string")
#
#
# def render_hundreds(num: int) -> str:
#     return str(num // 100)
#
#
# def app(helper: Callable[..., None], renderer: Callable[[int], str]):
#     helper()
#     num = 12345
#     print(renderer(num))
#
# app(help, render_hundreds)
# app(help, help)  # Expected type '(int) -> str', got '() -> None' instead


# ---------------------------------------------------------------------
# T = TypeVar('T')
#
#
# class LinkedList(Generic[T]):
#     data: T
#     next: "LinkedList[T]"
#
#     def __init__(self, data: T):
#         self.data = data
#
#
# head_int: LinkedList[int] = LinkedList(1)
# head_int.next = LinkedList(2)
# head_int.next = 2
# head_int.data += 1
# head_int.data.replace("0", "1")  # Unresolved attribute reference 'replace' for class 'int'
#
# head_str: LinkedList[str] = LinkedList("1")
# head_str.data.replace("0", "1")
#
# head_str = LinkedList[str](1)

# ---------------------------------------------------------------------
# from typing import List, cast
#
#
# def find_first_str(a: List[object]) -> str:
#     index = next(i for i, x in enumerate(a) if isinstance(x, str))
#     return cast(str, a[index])
#
# MyCallable = TypeVar("MyCallable", bound=Callable)
#
# def logged(func: MyCallable) -> MyCallable:
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(func.__name__, args, kwargs)
#         return func(*args, **kwargs)
#
#     return cast(MyCallable, wrapper)
#
# @logged
# def mysum(a: int, b: int) -> int:
#     return a + b
#
# mysum(a=1)  # error: Missing positional argument "b" in call to "mysum"


# ---------------------------------------------------------------------
