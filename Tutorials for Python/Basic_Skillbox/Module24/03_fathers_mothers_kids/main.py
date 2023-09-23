# TODO здесь писать код

from random import randint

class Parent:

    def __init__(self, name: str, age: int, children_list: list):
        self.name = name
        self.age = age
        self.children_list = children_list

    def who_am_i(self):
        print('Меня зовут {name}, мне {age} годика\nУ меня есть дети:'.format(
            name=self.name, age=self.age))
        for i_child in self.children_list:
            i_child.child_info()

    def feed(self, baby_name):
        for i_child in self.children_list:
            if i_child.name == baby_name:
                i_child.hunger = False
                break
        else:
            print('Нет такого ребёнка')

    def calm_down(self, baby_name):
        for i_child in self.children_list:
            if i_child.name == baby_name:
                i_child.status = Child.status[randint(0, 4)]
                break
        else:
            print('Нет такого ребёнка')

    def child_create(self, child_name: str, child_age: int = 0,
                     child_status: str = 'Орёт', child_hunger: bool = True):
        self.children_list.append(Child(child_name, child_age, self.age,
                                        child_status, child_hunger))
class Child:
    status = {
        0: 'Спит', 1: 'Затих', 2: 'Смеётся', 3: 'Плачет', 4: 'Орёт'
    }

    def __init__(self, child_name: str, child_age: int, patent_age: int,
                 child_status: str = status[4], child_hunger: bool = True):
        if patent_age - 16 > child_age:
            self.name = child_name
            self.age = child_age
            self.status = child_status
            self.hunger = child_hunger
        else:
            raise ValueError('Разница возрастов между ребёнком и родителем'
                  ' не может быть меньше 16 лет')

    def child_info(self):
        print('Имя ребёнка - {child_name}, возраст - {child_age}, '
              'состояние - {child_status}, хочет есть {child_hunger}'.format(
            child_name = self.name, child_age = self.age,
            child_status = self.status, child_hunger = self.hunger
        ))

parent = Parent('Коля', 33, [Child('Олег', 20, 33), Child('Ольга', 3, 33)])
parent.who_am_i()
print('\nКто-нибудь сделайте что-нибудь!\n')
parent.feed('Олег')
parent.calm_down('Ольга')
parent.children_list[0].child_info()
parent.children_list[1].child_info()

# parent.child_create('Алиса')
# parent.who_am_i()

# child = Child('Олег', 5, 33)
# child.child_info()