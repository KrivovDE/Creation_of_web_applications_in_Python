# TODO здесь писать код

from random import randint


class Warrior:
    health = 100

    def kick(self):
        if self.health > 0:
            self.health -= 20
            if self.health == 0:
                print("\tGame over - воин мёртв")

    def health_print(self):
        print(f"\tТекущий уровень здоровья - {self.health}")


warrior_1 = Warrior()
warrior_2 = Warrior()

print("Воин №1:")
warrior_1.health_print()
print("Воин №2:")
warrior_2.health_print()
print()

while warrior_1.health > 0 and warrior_2.health > 0:
    if randint(0, 1) == 0:
        print("\nВоин №2 атакует")
        warrior_1.kick()
    else:
        print("\nВоин №1 атакует")
        warrior_2.kick()
    print("\nВоин №1:", end=" ")
    warrior_1.health_print()
    print("Воин №2:", end=" ")
    warrior_2.health_print()
else:
    if warrior_1.health > 0:
        print("\nВоин №1 - победил")
    else:
        print("\nВоин №2 - победил")
