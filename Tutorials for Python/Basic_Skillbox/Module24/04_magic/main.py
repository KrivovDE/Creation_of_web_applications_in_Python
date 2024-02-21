# TODO здесь писать код


class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Ground):
            return Dirt()
        else:
            raise ValueError("Сочетание невозможно.")


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Ground):
            return Dust()
        else:
            raise ValueError("Сочетание невозможно.")


class Fire:
    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Ground):
            return Lava()
        else:
            raise ValueError("Сочетание невозможно.")


class Ground:
    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()
        else:
            raise ValueError("Сочетание невозможно.")


class Storm:
    pass


class Steam:
    pass


class Dirt:
    pass


class Lightning:
    pass


class Dust:
    pass


class Lava:
    pass


print(type(Air() + Water()))
print(type(Ground() + Fire()))
