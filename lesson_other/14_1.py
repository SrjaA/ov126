class Porshe:
    model='911'
    km=0
    def __init__(self,engine,power,km):
        self.engine=engine
        self.power=power
        self.km=km

    def drive(self,distance):
        dist=self.km+distance
        return f'Car проехал сегодня {self.km},Всево {dist}'


p_1=Porshe(1.6,100,0)
p_2=Porshe(2.5,400,0)

print(p_1.drive(100))
print(p_1.drive(100))
# print(lada.__dict__)
# print(lada.power)
# lada.power=112
# print(lada.power)
# print(lada.color,lada.__dict__)
# lada.color='blue'
# print(lada.color,lada.__dict__)
# print(lada.drive(530))
#
# class Car2:
#      """документация"""
#      print('я машынка')
#
# print(Car2.__doc__)