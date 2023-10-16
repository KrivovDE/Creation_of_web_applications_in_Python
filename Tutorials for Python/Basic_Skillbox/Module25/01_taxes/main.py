# TODO здесь писать код

class Property:
    """
    Базовый класс, описывающий имущество

    Args:
        worth(float): передаётся стоимость имущества

    """

    def __init__(self, worth: float):
        self.__worth = worth

    def get_worth(self):
        """
        Геттер для получения стоимости имущества

        :return: __worth
        :rtype: float
        """
        return self.__worth

    def set_worth(self, worth: float):
        """
        Сеттер для установки стоимости имущества

        :param worth: стоимость имущества
        :type worth: float
        """
        self.__worth = worth

    def tax(self):
        pass


class Apartment(Property):
    """
    Класс Квартира. Родитель: Property

    Args:
        worth(float): передаётся стоимость квартиры

    """

    def __init__(self, worth: float):
        super().__init__(worth)

    def tax(self):
        """
        Метод для расчёта налога на квартиру.

        :return: налог
        :rtype: float
        """

        return round(self.get_worth() / 1000, 2)


class Car(Property):
    """
    Класс Машина. Родитель: Property

    Args:
        worth(float): передаётся стоимость машины

    """

    def __init__(self, worth: float):
        super().__init__(worth)

    def tax(self):
        """
        Метод для расчёта налога на машину.

        :return: налог
        :rtype: float
        """
        return round(self.get_worth() / 200, 2)


class CountryHouse(Property):
    """
    Класс Дача. Родитель: Property

    Args:
        worth(float): передаётся стоимость дачи

    """

    def __init__(self, worth: float):
        super().__init__(worth)

    def tax(self):
        """
        Метод для расчёта налога на дачу.

        :return: налог
        :rtype: float
        """
        return round(self.get_worth() / 500, 2)


request = input('Введите текущий Баланс и '
                'стоимости квартиры, машины, дачи через пробел: ').split(' ')

if len(request) == 4 and all([parm.isdigit() for parm in request]):
    balance = float(request[0])
    apartment_tax = Apartment(float(request[1])).tax()
    car_tax = Car(float(request[2])).tax()
    country_house_tax = CountryHouse(float(request[3])).tax()
    common_tax = apartment_tax + car_tax + country_house_tax
    print('Налог на квартиру - {}\n'
          'Налог на машину - {}\n'
          'Налог на дачу - {}\n'.format(
        apartment_tax, car_tax, country_house_tax
    ))
    credit = balance - common_tax
    if credit < 0.01:
        print('Налогов слишком много, нехватает -', credit * -1)
    else:
        print('Денег достаточно, налоги заплачены.')
else:
    print('Введённые параметры некорректны.')

# зачтено
