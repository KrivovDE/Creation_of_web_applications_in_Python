# TODO здесь писать код


import math


def point_check(x, y, r):
    return True if round(math.sqrt(x ** 2 + y ** 2), 2) <= round(r, 2) else False


abscissa = float(input('Введите координаты монетки:\nX: '))
ordinate = float(input('Y: '))
radius = float(input('Введите радиус: '))

if point_check(abscissa, ordinate, radius):
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')

# зачтено
