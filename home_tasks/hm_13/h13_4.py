# Напишите функцию, которая создает список случайных
# элементов. На фход функция принимает кол-во элементов,
# минимальное и максимальное значение
# In: rand_nums(7, 2, 12)
# Out: [12, 6, 9, 2, 11, 5, 8]
import random


def random_list(a, b, c):
    return list(random.sample(range(b, c), a))


print(random_list(*map(lambda i: int(i), input('enter amount and min/max numbers:\t').split())))
