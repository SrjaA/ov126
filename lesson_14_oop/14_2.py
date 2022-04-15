class Porsche():
    model = 'Cayman'

    def __init__(self, color, power, max_speed):
        self.color = color
        self.power = power
        self.max_speed = max_speed
        self.mileage = 0

    def drive(self, km):
        print(f'Сегодня вы проехали {km} км')
        print(f'Ваш пробег {self.mileage + km} км')
        self.mileage += km


if __name__ == '__main__':
    cayman_s = Porsche('grey', 350, 285)
    cayman_s.drive(300)
    cayman_s.drive(500)

