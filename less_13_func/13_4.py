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