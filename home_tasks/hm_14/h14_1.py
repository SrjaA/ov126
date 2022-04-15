import random


class Dog:
    jump_of_day = 0
    run_of_day = 0

    def __init__(self, height, weight, name, age=1):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f'\033[2m\033[35mХозяин, попрыгаем?\033[0m')
        jump_at_time = 0
        while True:
            if input('Введите 1 для прыжка или нажмите Enter для выхода:\t') == '1':
                jump_at_time += 1
                print(f'{self.name} прыгнул(а) {jump_at_time} раз')
            else:
                print(f'{self.name} устал(а)')
                break
        Dog.jump_of_day += jump_at_time

    def run(self, run_mileage):
        print(f'\033[4mВы прогулялись с {self.name} {run_mileage} km')
        run_mileage_2 = random.randint(1, 10)
        print(f'Потом {self.name} сорвался с цепи и пробежал {run_mileage_2} km\033[0m')
        Dog.run_of_day += (run_mileage + run_mileage_2)
        return Dog.run_of_day

    def bark(self):
        print(f'\033[1m\033[32m{self.name} доволен (или недоволен) и гавкает V●ᴥ●V\033[0m')

    @classmethod
    def change_name(cls, nane, obj):
        print(f'{obj.name} стал {nane}')
        obj.name = nane


if __name__ == '__main__':
    cc = Dog(70, 20, 'Rex', 3)
    print(cc.__dict__)
    Dog.change_name('Tuzik', cc)
    print(cc.__dict__)
    cc.bark()
    cc.bark()
    cc.jump()
    cc.run(2)
    cc.bark()
    cc.jump()
    cc.bark()
    cc.run(5)
    print(f'\033[3m\033[33m{cc.name} за день прыгнул - {Dog.jump_of_day} раз, пробежал - {Dog.run_of_day} km\033[0m')
