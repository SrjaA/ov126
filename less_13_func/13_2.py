import random
def summ_numbers(d):
    return sum(d)
d=[random.randint(1,50) for i in range(5)]
print(d)
print(summ_numbers(d))