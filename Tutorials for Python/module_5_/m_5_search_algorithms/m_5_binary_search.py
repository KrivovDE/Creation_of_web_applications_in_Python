from typing import List


def binary_search(lst: List[int], val: int) -> int:
    first: int = 0
    last: int = len(lst) - 1
    index: int = -1
    while first <= last and index == -1:
        mid = (first + last) // 2
        if lst[mid] == val:
            index = mid
        else:
            if val < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index
from typing import List



binary_search([10, 20, 30, 40, 50], 20)

print(binary_search([4, 4, 4, 4, 4], 4))


