# TODO здесь писать код


reversed_word = ""

word = input("Введите слово: ")

for i in range(-1, -(len(word) + 1), -1):
    reversed_word += word[i]

if word == reversed_word:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")

# зачтено
