# TODO здесь писать код

from abc import ABC


class MyMath(ABC):

    """Абстрактный класс математических операций"""

    _Pi = 3.1415926535

    @classmethod
    def circle_len(cls, radius: float) -> float:
        """Возвращает длину окружности исходя из входного радиуса"""
        return 2 * cls._Pi * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        """Возвращает площадь окружности исходя из входного радиуса"""
        return 2 * cls._Pi * radius**2

    @classmethod
    def cub_vol(cls, fin_length: float) -> float:
        """Возвращает объём куда исходя из длинны ребра"""
        return fin_length**3

    @classmethod
    def surface_area_sphere(cls, radius: float) -> float:
        """Возвращает площадь поверхности сферы исходя из входного радиуса"""
        return 2 * cls._Pi * radius**2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
