# TODO здесь писать код

card_list = []
remaining_card = []
top_card = 0

numbers_card = int(input('Количество видеокарт: '))

for i in range(numbers_card):
    card = int(input(f'{i + 1} Видеокарта: '))
    top_card = card if card > top_card else top_card
    card_list.append(card)

for ver in card_list:
    if ver != top_card:
        remaining_card.append(ver)

print('Старый список видеокарт:', card_list)
print('Новый список видеокарт:', remaining_card)

# зачтено
