
def summ_number(*n):
    return sum(n)
print(f'summ_number:\t', summ_number(*list(map(lambda i:int(i), input('enter two numbers:\t').split()))))