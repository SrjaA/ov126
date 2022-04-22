# Hometask_14_8
# Добавьте в класс Pet дескриптор,
# чтобы нельзя было задать
# отрицательный возраст или 0.
import random
from abc import ABC, abstractmethod

class MyDescript:
    """Дескриптор"""

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError('Cannot be negative or Zero.')
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name



class Pet(ABC):

    age = MyDescript()
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

    @abstractmethod
    def voice(self):
        return 'Животное что-то издаёт...'



class Dog(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def bark(self):
        self.var = 0
        return f'{self.name} лает'

    def voice(self,quantity=0):
        self.var=0
        self.quantity=int(input('Хочешь погавкаю? Скажи, сколько раз:\t'))
        return f'{self.name} гавкнуло {self.quantity} раз'



class Cat(Pet):
    '''Cat_func'''

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def meow(self):
        self.var = 0
        return f'{self.name} мяукает'

    def voice(self):
        self.var=0
        return super().voice()


class Parrot(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def fly(self):
        self.var = 0
        return f'{self.name} летает'

    def voice(self,quantity=0):
        self.var=0
        self.quantity=int(input('Хочешь покаркаю? Скажи, сколько раз:\t'))
        return f'{self.name} каркнуло {self.quantity} раз'

if __name__ == '__main__':

    # rd=Pet('Hlo',5,'Dick')
    # rd.voice()
    cd = Dog('Rex', 98, 'Tomas')
    print(cd.__dict__)
    print()
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
    print(cd.voice())
    cc = Cat('Leo', 5, 'Ann')
    print(cc.run())
    print(cc.voice())
    cp = Parrot('Chik-Chirik', 1, 'Liz')
    print(cp.fly())
    print(cp.voice())


