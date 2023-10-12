# TODO здесь писать код


round_1 = open('first_tour.txt', 'r', encoding='utf-8')

passing_score = int(round_1.read(2))
round_1.seek(4)
scores = []

for i_data in round_1:
    gamer = i_data.split()
    if int(gamer[2]) > passing_score:
        scores.append((gamer[1][0] + '. ' + gamer[0], gamer[2]))
round_1.close()

round_2 = open('second_tour.txt', 'w', encoding='utf-8')
round_2.write(f'{len(scores)}\n')
for index, payer in enumerate(sorted(scores, reverse=True)):
    round_2.write(f'{index+1}) {payer[0]} {payer[1]}\n')

print('Готовенько!')
round_2.close()