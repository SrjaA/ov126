# Напишите декоратор к функции деления, который меняет
# местами делимое и делитель

# In: div(2, 4)
# Out: 2.0


def rev(fun):
    def decor_div(x, y):
        return y / x
    return decor_div

@rev
def div(a, b):
    return a / b

print(div(2, 4))