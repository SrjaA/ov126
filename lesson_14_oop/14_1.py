

class Person:

    def __init__(self, name, lastname, age=1, sex="male"):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.sex = sex

    def show_year_of_burn(self, current_year):
        return f"{self.name} was born in {current_year - self.age}"


vasya = Person("Vasya", "Pupkin", sex="female")
kate = Person("Kate", "Ololo", 23, "female")
print(kate.show_year_of_burn(2022))
print(vasya.show_year_of_burn(2022))