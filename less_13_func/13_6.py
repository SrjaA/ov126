
def info_kwargs(**ztr):
    list_keys = list(ztr.keys())
    list_keys.sort()
    for i in list_keys:
        print(i, ':', ztr[i])

d = {'f': 10, 'c': 15, 'b': 4, 'a':19,'d':0}
info_kwargs(**d)