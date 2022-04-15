a = int(input('enter:\n'))
b = int(input('enter:\n'))
c = int(input('enter:\n'))


def max_number(a, b, c):
    return max(a, b, c)


print(f'max_number:\t', max_number(a, b, c))


def maxx_number(*n):
    return max(n)


print(f'max_number:\t', maxx_number(*[int(i) for i in input('enter numbers:\t').split()]))
