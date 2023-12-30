films = [
    "Крепкий орешек",
    "Назад в будущее",
    "Таксист",
    "Леон",
    "Богемская рапсодия",
    "Город грехов",
    "Мементо",
    "Отступники",
    "Деревня",
]


# TODO здесь писать код


def film_search(request):
    for film in films:
        if request == film:
            return True
    else:
        return False


favorite_films = []
counter = 0
numbers_films = int(input("Сколько фильмов хотите добавить? "))

for _ in range(numbers_films):
    film = input("Введите название фильма: ")
    if film_search(film):
        favorite_films.append(film)
    else:
        print(f"Ошибка: фильма {film} у нас нет :(")
counter = len(favorite_films)

print("Ваш список любимых фильмов:", end=" ")
for name in favorite_films:
    print(name, end="")
    if counter - 1 > 0:
        print(",", end=" ")
        counter -= 1

# зачтено
