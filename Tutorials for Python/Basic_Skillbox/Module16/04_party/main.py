guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код


answer = ''

while True:
    print(f'Сейчас на вечеринке {len(guests)} человек:', guests)
    answer = input('Гость пришёл или ушёл? ')
    if answer == 'пришёл':
        name = input('Имя гостя: ')
        if len(guests) < 6:
            print(f'Привет, {name}!')
            guests.append(name)
        else:
            print(f'Прости, {name}, но мест нет.')
    elif answer == 'ушёл':
        name = input('Имя гостя: ')
        guests.remove(name)
        print(f'Пока, {name}!')
    elif answer == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    else:
        print('A? Что?')
    print()

# зачтено
