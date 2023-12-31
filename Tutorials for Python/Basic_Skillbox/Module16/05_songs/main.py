violator_songs = [
    ["World in My Eyes", 4.86],
    ["Sweetest Perfection", 4.43],
    ["Personal Jesus", 4.56],
    ["Halo", 4.9],
    ["Waiting for the Night", 6.07],
    ["Enjoy the Silence", 4.20],
    ["Policy of Truth", 4.76],
    ["Blue Dress", 4.29],
    ["Clean", 5.83],
]

# TODO здесь писать код

amount_songs = int(input("Сколько песен выбрать? "))
common_duration = 0

for i in range(amount_songs):
    print(f"Название {i + 1}-й песни:", end=" ")
    serach = input()
    for song in violator_songs:
        if song[0] == serach:
            common_duration += song[1]
            break
    else:
        print("Такой композиции нет в исходном списке :(")

print(f"Общее время звучания песен: {round(common_duration, 2)} минуты")

# зачтено
