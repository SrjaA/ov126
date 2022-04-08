# a=int(input())
# b=int(input())
# c=int(input())
#
# def max_number(a,b,c):
#     return max(a,b,c)
# print(max_number(a,b,c))
#
#
#
# def summ_numbers(d):
#     return sum(d)
# d=[2,4,6,'efr','rygr',45,'dfl',67]
# print(summ_numbers(d))

def proizv(f):
    a=1
    for i in f:
        a*=i
    return a
f=[3,4,8,5,1,3]
print(proizv(f))

def count_letters(str):
    a=0
    c=0
    b=0
    for i in str:
        if i.islower() is True:
            c+=1
        elif i.isdigit() is True:
            a+=1
        else:
            b+=1
    return f'строчных - {c}, прописных - {b}, цифров - {a}'
str='gkjRTiowjguk3r854ou2yHSJ9fgn'
print(count_letters(str))

def count_args(*args):
    return len(args)

print(count_args(3,4,8,23,65,34))

def info_kwargs(**ztr):
    return
