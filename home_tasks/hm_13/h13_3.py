def delet_na_delet(nmbr):
    b = []
    for i in nmbr:
        if i % 2 == 0:
            b.append(i / 2)
    return tuple(b)


c = tuple(map(int, input('Enter your numbers with space:\n').split()))

print(c)
print(f"\033[3m\033[33m{delet_na_delet(c)}")
