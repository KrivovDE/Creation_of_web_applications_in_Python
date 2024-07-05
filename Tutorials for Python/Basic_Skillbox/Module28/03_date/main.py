# TODO здесь писать код


class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def is_date_valid(cls, info_str: str) -> bool:
        day, month, year = info_str.split("-")
        day, month, year = int(day), int(month), int(year)
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year

    @classmethod
    def from_string(cls, info_str: str) -> "Date":
        day, month, year = info_str.split("-")
        return cls(int(day), int(month), int(year))

    def __str__(self):
        return "День: {day}\tМесяц: {month}\tГод: {year}".format(
            day=self.day,
            month=self.month,
            year=self.year,
        )


date = Date.from_string("10-12-2077")
print(date)
print(Date.is_date_valid("10-12-2077"))
print(Date.is_date_valid("40-12-2077"))
