alphabet = "abcdefg"

# TODO здесь писать код

alphabet_copy = alphabet[:]

print(alphabet_copy)
print(alphabet_copy[::-1])
print(alphabet_copy[::2])
print(alphabet_copy[1::2])
print(alphabet_copy[:1])
print(alphabet_copy[len(alphabet_copy) : len(alphabet_copy) - 2 : -1])
print(alphabet_copy[3:4])
print(alphabet_copy[len(alphabet_copy) - 3 : len(alphabet_copy)])
print(alphabet_copy[3 : 4 + 1])
print(alphabet_copy[4 : 3 - 1 : -1])

# зачтено
