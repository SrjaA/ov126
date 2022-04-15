class Pie:

    baked_pies = 0

    def __init__(self, filling):
        self.filling = filling
        Pie.baked_pies += 1

    def show(self):
        print(f'Вкус пирога: {self.filling}')

    @classmethod
    def cooking(cls):
        print(f'Всего испекли {Pie.baked_pies} пирогa')

    @staticmethod
    def more():
        print(f'Следующий пирог')

if __name__ == 'main':
    p = Pie("banana")
    p.more()
    Pie.more()