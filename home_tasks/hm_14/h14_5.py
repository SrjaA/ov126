# Hometask_14_5
# Создать три класса: Dog, Cat, Parrot.
# Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор и методы: run, jump,
# birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный
# метод fly, Cat - meow, Dog - bark.
import random


class Dog:

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

    def bark(self):
        self.var = 0
        return f'{self.name} лает'


class Cat:

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

    def meow(self):
        self.var = 0
        return f'{self.name} мяукает'


class Parrot:
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
