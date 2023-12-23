# TODO здесь писать код

from collections import deque


def can_be_poly(data: str) -> bool:
    deque_str = deque(data)

    while len(deque_str) > 1:
        first_sign = deque_str.pop()
        last_sign = deque_str.popleft()
        if first_sign != last_sign:
            return False
    return True


print(can_be_poly("abcba"))
print(can_be_poly("abbbc"))

# зачтено
