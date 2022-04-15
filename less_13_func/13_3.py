import random
def mult(f):
    res=1
    for i in f:
        res*=i
    return res
d=[random.randint(1,20) for i in range(5)]
print(d)
print(mult(d))

def multi(*e):
    res=1
    for i in e:
        i=int(i)
        res*=i
    return res

print(multi(2,3,85,3,654,865,3))
nums=[int(i) for i in input().split()]
print(multi(*nums))
print(multi(*[int(i) for i in input().split()]))
