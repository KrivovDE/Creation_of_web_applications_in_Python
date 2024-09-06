# TODO здесь писать код

from collections import Counter


def count_unique_characters(mess: str) -> int:
    return len(
        list(
            filter(
                lambda y: y[1] == 1, map(lambda x: x, Counter(mess.lower()).items())
            ),
        ),
    )


# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)

# зачтено
