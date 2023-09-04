def binary_search(lst: list[int], val: int) -> int:
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


print(binary_search([10, 20, 30, 40, 50], 20))
