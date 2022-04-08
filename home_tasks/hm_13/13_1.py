
n=(65, 86, 897, 1055)
def list_numbers(nmbr=n):

    a = []
    for i in nmbr:
        i = str(i)
        sum = 0
        for j in i:
            j = int(j)
            sum += j
        a.append(sum)
        a.sort()
    return tuple(a)

nmb = tuple(map(int, input('Enter your numbers with space:\n').split()))
print(list_numbers(nmb))
