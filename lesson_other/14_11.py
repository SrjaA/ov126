class Person:
    age = 0
    sex = 'male'

    def __init__(self, name, lastname, age=1, sex='male'):
        self.name = name
        self.faml = lastname
        self.age = age
        self.sex = sex

    def ages(self, now_year):
        year = now_year - self.age

        if self.sex == 'male' and self.age <= 18:
            return f'Пойдёт в армию череэ {now_year - year}'


katya = Person('katya', 'pozner', 23, 'female')
vasya = Person('vasya', 'cekalo', 15, )
katya.age = 28
katya.sex = 'ronald'
print(katya)
print(katya.__dict__)
print(vasya.ages(2022))
