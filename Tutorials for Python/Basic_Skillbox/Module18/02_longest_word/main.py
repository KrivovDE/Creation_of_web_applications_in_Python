# TODO здесь писать код


text = input('Введите строку: ').split()
result = [0, '']

for word in text:
    if len(word) > result[0]:
        result = [len(word), word]

print('Самое длинное слово:', result[1])
print('Длина этого слова:', result[0])

# зачтено
