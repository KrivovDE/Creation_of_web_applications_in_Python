# TODO здесь писать код


def year_search(start_year, finish_year):
    for year in range(start_year, finish_year + 1):
        rank_4 = year // 1000
        rank_3 = (year // 100) % 10
        rank_2 = (year // 10) % 10
        rank_1 = year % 10
        counter_1, counter_2, counter_3, counter_4 = 0, 0, 0, 0
        temp_year = year
        while temp_year != 0:
            if temp_year % 10 == rank_1:
                counter_1 += 1
            elif temp_year % 10 == rank_2:
                counter_2 += 1
            elif temp_year % 10 == rank_3:
                counter_3 += 1
            elif temp_year % 10 == rank_4:
                counter_4 += 1
            temp_year //= 10
        if counter_1 >= 3 or counter_2 >= 3 or counter_3 >= 3 or counter_4 >= 3:
            print(year)


start_year = int(input("Введите первый год: "))
finish_year = int(input("Введите второй год: "))

print(f"Годы от {start_year} до {finish_year} с тремя одинаковыми цифрами:")
year_search(start_year, finish_year)

# зачтено
