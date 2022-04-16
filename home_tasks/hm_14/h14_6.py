# Hometask_14_6
# Создать родительский класс Pet,
# содержащий все общие методы классов Dog, Cat, Parrot.
# Унаследовать Dog, Cat, Parrot от класса Pet.
# Удалить в дочерних классах те методы,
# которые имеются у родительского класса.
# Создать объект каждого класса и вызвать все его методы.
import random


class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master
        self.var = 0

    def run(self):
        self.var = 0
        return f'{self.name} пробежал {random.randint(1, 20)} м'

    def jump(self):
        self.var = 0
        return f'{self.name} прыгнул {random.randint(1, 20)} раз'

    def birthday(self):
        self.age += 1
        return f'{self.name} живёт уже {self.age} дней'

    def sleep(self):
        if self.var == 0:
            self.var = 1
            return f'{self.name} идёт спать'
        else:
            return f'{self.name} уже спиць'


class Dog(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def bark(self):
        self.var = 0
        return f'{self.name} лает'


class Cat(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def meow(self):
        self.var = 0
        return f'{self.name} мяукает'


class Parrot(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def fly(self):
        self.var = 0
        return f'{self.name} летает'


if __name__ == '__main__':
    cd = Dog('Rex', 1, 'Tomas')
    print(cd.bark())
    print(cd.run())
    print(cd.jump())
    print(cd.sleep())
    print(cd.sleep())
    print(cd.birthday())
    print(cd.birthday())
    print(cd.sleep())
    print(cd.bark())
    print(cd.sleep())
    cc = Cat('Leo', 5, 'Ann')
    print(cc.run())
    print(cc.meow())
    cp = Parrot('Chik-Chirik', 1, 'Liz')
    print(cp.fly())
